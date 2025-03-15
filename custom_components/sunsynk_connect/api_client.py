import logging
import json
import aiohttp
from asyncio import TimeoutError
from datetime import (datetime, timedelta, time, timezone)
from threading import RLock

from homeassistant.util.dt import (as_utc, now, as_local, parse_datetime, parse_date)

_LOGGER = logging.getLogger(__name__)

user_agent_value = "malcernie-ha-sunsynk-connect"

class SunsynkConnectApiClient:
  _refresh_token_lock = RLock()
  _session_lock = RLock()

  def __init__(self, username, password, timeout_in_seconds = 20):
    if (username is None):
      raise Exception('username is not set')
    if (password is None):
      raise Exception('password is not set')

    self._username = username
    self._password = password
    self._oauth_url = 'https://api.sunsynk.net/oauth/token'
    self._base_url = 'https://api.sunsynk.net/api/v1'

    self._api_token = None
    self._api_token_expiration = None

    self._timeout = aiohttp.ClientTimeout(total=None, sock_connect=timeout_in_seconds, sock_read=timeout_in_seconds)
    self._default_headers = { "user-agent": f'{user_agent_value}' }

    self._session = None

  async def async_close(self):
    with self._session_lock:
      if self._session is not None:
        await self._session.close()

  def _create_client_session(self):
    if self._session is not None:
      return self._session
    
    with self._session_lock:
      if self._session is not None:
        return self._session
      
      self._session = aiohttp.ClientSession(headers=self._default_headers, skip_auto_headers=['User-Agent'])
      return self._session

  async def async_refresh_token(self):
    """Get the user's refresh token"""
    if (self._api_token_expiration is not None and (self._api_token_expiration - timedelta(minutes=5)) > now()):
      return

    with self._refresh_token_lock:
      # Check that our token wasn't refreshed while waiting for the lock
      if (self._api_token_expiration is not None and (self._api_token_expiration - timedelta(minutes=5)) > now()):
        return

      try:
      client = self._create_client_session()
        url = f'{self._oauth_url}'
        payload = { "username": self._username, "password": self._password, "grant_type": "password", client_id: "openapi"  }
        headers = { integration_context_header: "refresh-token" }
        async with client.post(url, headers=headers, json=payload) as client_response:
          client_response_body = await self.__async_read_response__(client_response, url)
          _LOGGER.debug(f'inverters: {client_response_body}')
          
          if (client_response_body is not None and 
              "msg" in client_response_body and
              client_response_body["msg"].lower() == 'success' and
              "data" in client_response_body and
              "access_token" in client_response_body["data"] and 
              client_response_body["data"]["access_token"] is not None):
            
            self._api_token = client_response_body["data"]["token"]
            self._api_token_expiration = now() + timedelta(hours=1)
          else:
            _LOGGER.error("Failed to retrieve auth token")
      except TimeoutError:
        _LOGGER.warning(f'Failed to connect. Timeout of {self._timeout} exceeded.')
        raise TimeoutException()

  async def async_api_get(self, url):
    await self.async_refresh_token()

    try:
      client = self._create_client_session()
      payload = { }
      headers = { "Authorization": f"Bearer {self._api_token}" }
      _LOGGER.debug(f'url: {url}')
      async with client.get(url, json=payload, headers=headers) as client_response:
        client_response_body = await self.__async_read_response__(client_response, url)
        _LOGGER.debug(f'get: {client_response_body}')

        if (client_response_body is not None and 
            "msg" in client_response_body and
            client_response_body["msg"].lower() == 'success' and
            "data" in client_response_body):
          return client_response_body["data"]
        else:
          _LOGGER.error("Failed to retrieve data")
    
    except TimeoutError:
      _LOGGER.warning(f'Failed to connect. Timeout of {self._timeout} exceeded.')
      raise TimeoutException()
    
    return None

  async def async_api_post(self, url, payload):
    await self.async_refresh_token()

    try:
      client = self._create_client_session()
      headers = { "Authorization": f"Bearer {self._api_token}" }
      _LOGGER.debug(f'url: {url}')
      _LOGGER.debug(f'payload: {payload}')
      return None
      async with client.post(url, json=payload, headers=headers) as client_response:
        client_response_body = await self.__async_read_response__(client_response, url)
        _LOGGER.debug(f'post: {client_response_body}')

        if (client_response_body is not None and 
            "msg" in client_response_body and
            client_response_body["msg"].lower() == 'success' and
            "data" in client_response_body):
          return client_response_body["data"]
        else:
          _LOGGER.error("Failed to retrieve data")
    
    except TimeoutError:
      _LOGGER.warning(f'Failed to connect. Timeout of {self._timeout} exceeded.')
      raise TimeoutException()
    
    return None

async def async_list_inverters(self):
    """List inverters"""
    url = f'{self._base_url}/inverters'
    await api_response = await async_api_get(self, url)
    if (api_response is not None and 
        "infos" in api_response and 
        len(api_response["infos"]) > 0):
      return api_response["infos"]
    else:
      _LOGGER.error("Failed to retrieve inverters")
    return None

  async def async_get_inverter_settings(self, inverter_serial):
    """Get Inverter Settings"""
    url = f'{self._base_url}/inverter/{inverter_serial}/read'
    await api_response = await async_api_get(self, url)
    return api_response

async def async_save_inverter_settings(self, inverter_serial, settings):
    """Save Inverter Settings"""
    settings['sn'] = inverter_serial
    _LOGGER.debug(settings)
    url = f'{self._base_url}/inverter/{inverter_serial}/set'
    await api_response = await async_api_post(self, url, settings)
    return (api_response == None)

  async def async_get_inverter_realtime_output(self, inverter_serial):
    """Get Inverter Ouput"""
    url = f'{self._base_url}/inverter/{inverter_serial}/realtime/output'
    await api_response = await async_api_get(self, url)
    return api_response

  async def async_get_inverter_realtime_input(self, inverter_serial):
    """Get Inverter Input"""
    url = f'{self._base_url}/inverter/{inverter_serial}/realtime/input'
    await api_response = await async_api_get(self, url)
    return api_response

  async def async_get_inverter_realtime_battery(self, inverter_serial):
    """Get Inverter Battery"""
    url = f'{self._base_url}/inverter/battery/{inverter_serial}/realtime?sn={inverter_serial}&lan=en'
    await api_response = await async_api_get(self, url)
    return api_response

  async def async_get_inverter_realtime_grid(self, inverter_serial):
    """Get Inverter Grid"""
    url = f'{self._base_url}/inverter/grid/{inverter_serial}/realtime?sn={inverter_serial}&lan=en'
    await api_response = await async_api_get(self, url)
    return api_response

  async def async_get_inverter_realtime_load(self, inverter_serial):
    """Get Inverter Load"""
    url = f'{self._base_url}/inverter/load/{inverter_serial}/realtime?sn={inverter_serial}&lan=en'
    await api_response = await async_api_get(self, url)
    return api_response

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
        payload = { "username": self._username, "password", "password": self._password, "grant_type": "password", client_id: "openapi"  }
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

  async def async_list_inverters(self, account_id):
    """List inverters"""
    await self.async_refresh_token()

    try:
      client = self._create_client_session()
      url = f'{self._base_url}/inverters'
      payload = { }
      headers = { "Authorization": f"BEARER {self._api_token}" }
      async with client.get(url, json=payload, headers=headers) as client_response:
        client_response_body = await self.__async_read_response__(client_response, url)
        _LOGGER.debug(f'inverters: {client_response_body}')

        if (client_response_body is not None and 
            "msg" in client_response_body and
            client_response_body["msg"].lower() == 'success' and
            "data" in client_response_body and 
            "infos" in client_response_body["data"] and 
            len(client_response_body["data"]["infos"]) > 0):
          return client_response_body["data"]["infos"]
        else:
          _LOGGER.error("Failed to retrieve account")
    
    except TimeoutError:
      _LOGGER.warning(f'Failed to connect. Timeout of {self._timeout} exceeded.')
      raise TimeoutException()
    
    return None

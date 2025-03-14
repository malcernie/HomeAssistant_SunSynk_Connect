class OctopusEnergyApiClient:
  _refresh_token_lock = RLock()
  _session_lock = RLock()

  def __init__(self, api_key, electricity_price_cap = None, gas_price_cap = None, timeout_in_seconds = 20, favour_direct_debit_rates = True):
    if (api_key is None):
      raise Exception('API KEY is not set')

    self._api_key = api_key
    self._base_url = 'https://api.octopus.energy'

    self._graphql_token = None
    self._graphql_expiration = None

    self._product_tracker_cache = dict()

    self._electricity_price_cap = electricity_price_cap
    self._gas_price_cap = gas_price_cap
    self._favour_direct_debit_rates = favour_direct_debit_rates

    self._timeout = aiohttp.ClientTimeout(total=None, sock_connect=timeout_in_seconds, sock_read=timeout_in_seconds)
    self._default_headers = { "user-agent": f'{user_agent_value}/{INTEGRATION_VERSION}' }

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
    if (self._graphql_expiration is not None and (self._graphql_expiration - timedelta(minutes=5)) > now()):
      return

    with self._refresh_token_lock:
      # Check that our token wasn't refreshed while waiting for the lock
      if (self._graphql_expiration is not None and (self._graphql_expiration - timedelta(minutes=5)) > now()):
        return

      try:
        client = self._create_client_session()
        url = f'{self._base_url}/v1/graphql/'
        payload = { "query": api_token_query.format(api_key=self._api_key) }
        headers = { integration_context_header: "refresh-token" }
        async with client.post(url, headers=headers, json=payload) as token_response:
          token_response_body = await self.__async_read_response__(token_response, url)
          if (token_response_body is not None and 
              "data" in token_response_body and
              "obtainKrakenToken" in token_response_body["data"] and 
              token_response_body["data"]["obtainKrakenToken"] is not None and
              "token" in token_response_body["data"]["obtainKrakenToken"]):
            
            self._graphql_token = token_response_body["data"]["obtainKrakenToken"]["token"]
            self._graphql_expiration = now() + timedelta(hours=1)
          else:
            _LOGGER.error("Failed to retrieve auth token")
      except TimeoutError:
        _LOGGER.warning(f'Failed to connect. Timeout of {self._timeout} exceeded.')
        raise TimeoutException()

from decrypto import RSACipher
import requests, re, json
import os

_PATTERN_URL = '^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$'
_PATTERN_IPV4 = '^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$'
_PATTERN_HASH_MD5 = '^[0-9a-f]{32}$'
_PATTERN_HASH_SHA1 = '^[0-9a-f]{40}$'
_PATTERN_HASH_SHA256 = '^[0-9a-f]{64}$'
_PATTERN_DNS = '^[A-Za-z0-9\-\.]+\.[A-Za-z0-9\-\.]+$'


class GeneralAPI:
  convert_to_tuple = lambda self, key_str: tuple(int(x) for x in key_str.split(','))

  def __init__(self, url='', cipher=RSACipher(), route_filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials.json')):
    if not self.__isurl__(url):
      raise ValueError('This value isn\'t a valid URL')
    
    self._cipher = cipher
    self._filename = route_filename

    with open(self._filename, 'r') as jf:
      data = json.load(jf)
      public_key = data.get('public_key', None)
      api_key = data.get('api_key', None)
    
    if not api_key:
      raise Exception('API key not load correctly')
    
    if not public_key:
      public_key, secret_key = self.__generate_keys__()
      data['public_key'] = str(public_key)[1:-1]
      data['private_key'] = str(secret_key)[1:-1]
      with open(self._filename, 'w') as jf:
        json.dump(data, jf)

    if type(public_key) == str:
      public_key = self.convert_to_tuple(public_key)
    
    self._api_key = self._cipher.encrypt(str(api_key), public_key)
    self._url = url[:-1] if url.endswith('/') else url
  
  def __isurl__(self, url: str):
    return re.fullmatch(_PATTERN_URL, url)
  

  def __isdns__(self, dns: str):
    return re.fullmatch(_PATTERN_DNS, dns)

  def __ishash__(self, hash: str):
    isvalid = re.fullmatch(_PATTERN_HASH_MD5, hash) or re.fullmatch(_PATTERN_HASH_SHA1, hash)
    return isvalid or re.fullmatch(_PATTERN_HASH_SHA256, hash)

  def __isipv4__(self, ip: str):
    if re.fullmatch(_PATTERN_IPV4, ip):
      for x in ip.split('.'):
        if not 0<=int(x)<256:
          return False
    return re.fullmatch(_PATTERN_IPV4, ip)
      

  def __getresponse__(self, short_url, headers=None, **kwargs):
    full_url = '{}{}'.format(self._url, short_url) if short_url.startswith('/') else '{}/{}'.format(self._url, short_url) 
    if headers:
      response = requests.get(full_url, headers=headers, **kwargs)
    else:
      response = requests.get(full_url, **kwargs)
    return response
  
  def __getapikey__(self):
    with open(self._filename, 'r') as jf:
      data = json.load(jf)
      secret_key = data.get('private_key', None)
      
    if not data or not secret_key:
      raise ImportError('json data isn\'t load correctly.')

    secret_key = self.convert_to_tuple(secret_key)
    return self._cipher.decrypt(self._api_key, secret_key)


  def __generate_keys__(self):
    cipher = self._cipher if self._cipher else RSACipher()
    keys = cipher.generate_keys(23, 31)
    return keys['public_key'], keys['private_key']
import requests, re

_PATTERN_URL = '^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$'
_PATTERN_IPV4 = '^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$'
_PATTERN_HASH_MD5 = '^[0-9a-f]{32}$'
_PATTERN_HASH_SHA1 = '^[0-9a-f]{40}$'
_PATTERN_HASH_SHA256 = '^[0-9a-f]{64}$'
_PATTERN_DNS = '^[A-Za-z0-9\-\.]+\.[A-Za-z0-9\-\.]+$'


class GeneralAPI:

  def __init__(self, url=''):
    if not self.__isurl__(url):
      raise ValueError('This value isn\'t a valid URL')

    self._url = url[:-1] if url.endswith('/') else url

  @staticmethod
  def __isurl__(url): return re.fullmatch(_PATTERN_URL, url)

  @staticmethod
  def __isdns__(dns): return re.fullmatch(_PATTERN_DNS, dns)
    
  @staticmethod
  def __ishash__(hash): return re.fullmatch(_PATTERN_HASH_MD5, hash) or re.fullmatch(_PATTERN_HASH_SHA256, hash) or re.fullmatch(_PATTERN_HASH_SHA1, hash)
    
  @staticmethod
  def __isipv4__(ip): return re.fullmatch(_PATTERN_IPV4, ip)

  @staticmethod
  def hash_type(hash):
    if re.fullmatch(_PATTERN_HASH_MD5, hash):
      return 'md5'
    elif re.fullmatch(_PATTERN_HASH_SHA1, hash):
      return 'sha1'
    elif re.fullmatch(_PATTERN_HASH_SHA256, hash):
      return 'sha256'
    else:
      return 'unknown'
  

  def __getresponse__(self, short_url, headers=None, **kwargs):
    full_url = '{}{}'.format(self._url, short_url) if short_url.startswith('/') else '{}/{}'.format(self._url, short_url) 
    if headers:
      response = requests.get(full_url, headers=headers, **kwargs)
    else:
      response = requests.get(full_url, **kwargs)
    return response
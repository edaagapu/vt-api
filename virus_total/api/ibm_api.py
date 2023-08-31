from .base import GeneralAPI
from urllib.parse import quote_plus

_URL = 'https://api.xforce.ibmcloud.com/'


class IBMAPI(GeneralAPI):
  def __init__(self):
    super().__init__(url=_URL)

  def __getkwargs__(self, credentials):
    return {'auth': (credentials.get('llave'), credentials.get('contrasenia'))}


  def get_hash_information(self, hash:str, **kwargs):
    return super().__getresponse__(f'/malware/{hash}', **kwargs)


  def get_ip_information(self, ip:str, **kwargs):
    if not super().__isipv4__(ip):
      raise ValueError('This value isn\'t a valid IPv4')
    return super().__getresponse__(f'/api/ipr/{ip}', **kwargs)


  def get_url_information(self, url:str, **kwargs):
    if not super().__isurl__(url):
      raise ValueError('This value isn\'t a valid URL')
    safe_url = quote_plus(url)
    return super().__getresponse__(f'/api/url/{safe_url}', **kwargs).json()
  
  
  def get_dns_information(self, dns:str, **kwargs):
    if not super().__isdns__(dns):
      raise ValueError('This value isn\'t a valid DNS')
    return super().__getresponse__(f'/api/ipr/{dns}', **kwargs)

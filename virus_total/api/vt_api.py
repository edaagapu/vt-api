from .base import GeneralAPI
import base64

_URL = 'https://www.virustotal.com/api/v3/'

class VTAPI(GeneralAPI):
  def __init__(self):
    super().__init__(url=_URL)

  def __getkwargs__(self, credentials):
    return {'headers': {'x-apikey': credentials.get('llave')}}


  def get_hash_information(self, hash:str, **kwargs):
    return super().__getresponse__(f'/files/{hash}', **kwargs)


  def get_ip_information(self, ip:str, **kwargs):
    if not super().__isipv4__(ip):
      raise ValueError('This value isn\'t a valid IPv4')
    return super().__getresponse__(f'/ip_addresses/{ip}', **kwargs)


  def get_url_information(self, url:str, **kwargs):
    if not super().__isurl__(url):
      raise ValueError('This value isn\'t a valid URL')
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    return super().__getresponse__(f'/urls/{url_id}', **kwargs)


  def get_dns_information(self, dns:str, **kwargs):
    if not super().__isdns__(dns):
      raise ValueError('This value isn\'t a valid domain')
    return super().__getresponse__(f'/domains/{dns}', **kwargs)

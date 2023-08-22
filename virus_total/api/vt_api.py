from .base import GeneralAPI
import base64


_URL = 'https://www.virustotal.com/api/v3/'

class VTAPI(GeneralAPI):
  def __init__(self):
    super().__init__(url=_URL)

  def get_hash_information(self, hash:str, credentials:dict):
    headers = {'x-apikey': credentials.get('llave')}
    return super().__getresponse__(f'/files/{hash}', headers)


  def get_ip_information(self, ip:str, credentials:dict):
    headers = {'x-apikey': credentials.get('llave')}
    if not super().__isipv4__(ip):
      raise ValueError('This value isn\'t a valid IPv4')
    return super().__getresponse__(f'/ip_addresses/{ip}', headers)


  def get_url_information(self, url:str, credentials:dict):
    if not super().__isurl__(url):
      raise ValueError('This value isn\'t a valid URL')
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    headers = {'x-apikey': credentials.get('llave')}
    return super().__getresponse__(f'/urls/{url_id}', headers=headers)


  def get_dns_information(self, dns:str, credentials:dict):
    if not super().__isdns__(dns):
      raise ValueError('This value isn\'t a valid domain')
    headers = {'x-apikey': credentials.get('llave')}
    return super().__getresponse__(f'/domains/{dns}', headers=headers)

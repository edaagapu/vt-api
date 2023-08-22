from .base import GeneralAPI
from urllib.parse import quote_plus
import os, json

_URL = 'https://api.xforce.ibmcloud.com/'


class IBMAPI(GeneralAPI):
  def __init__(self):
    super().__init__(url=_URL)


  def get_hash_information(self, hash:str, credentials: dict):
    return super().__getresponse__(f'/malware/{hash}',auth=(credentials.get('llave'), credentials.get('contrasenia')))


  def get_ip_information(self, ip:str, credentials: dict):
    if not super().__isipv4__(ip):
      raise ValueError('This value isn\'t a valid IPv4')
    return super().__getresponse__(f'/api/ipr/{ip}',auth=(credentials.get('llave'), credentials.get('contrasenia')))


  def get_url_information(self, url:str, credentials: dict):
    if not super().__isurl__(url):
      raise ValueError('This value isn\'t a valid URL')
    safe_url = quote_plus(url)
    return super().__getresponse__(f'/api/url/{safe_url}',auth=(credentials.get('llave'), credentials.get('contrasenia'))).json()
  
  
  def get_dns_information(self, dns:str, credentials: dict):
    if not super().__isdns__(dns):
      raise ValueError('This value isn\'t a valid DNS')
    return super().__getresponse__(f'/api/ipr/{dns}',auth=(credentials.get('llave'), credentials.get('contrasenia')))


from .base import GeneralAPI
from urllib.parse import quote_plus
import os, json

_URL = 'https://api.xforce.ibmcloud.com/'

# MD5 ^[0-9a-f]{32}$
# SHA-1 ^[0-9a-f]{40}$
# SHA-256 ^[0-9a-f]{64}$
# Domain ^[A-Za-z0-9\-\.]+\.[A-Za-z0-9\-\.]+$

class IBMAPI(GeneralAPI):
  def __init__(self):
    super().__init__(url=_URL, route_filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials_IBM.json'))

  def __getapikey__(self):
    raw_credentials = super().__getapikey__().replace('\'', '"')
    return json.loads(raw_credentials)


  def get_hash_information(self, hash:str):
    credentials = self.__getapikey__()
    return super().__getresponse__(f'/malware/{hash}',auth=(credentials.get('key'), credentials.get('password')))


  def get_ip_information(self, ip:str):
    credentials = self.__getapikey__()
    if not super().__isipv4__(ip):
      raise ValueError('This value isn\'t a valid IPv4')
    return super().__getresponse__(f'/api/ipr/{ip}',auth=(credentials.get('key'), credentials.get('password')))


  def get_url_information(self, url:str):
    credentials = self.__getapikey__()
    if not super().__isurl__(url):
      raise ValueError('This value isn\'t a valid URL')
    safe_url = quote_plus('https://www.ibm.com/smarterplanet')
    return super().__getresponse__(f'/api/url/{safe_url}',auth=(credentials.get('key'), credentials.get('password'))).json()
  
  
  def get_dns_information(self, dns:str):
    credentials = self.__getapikey__()
    if not super().__isdns__(dns):
      raise ValueError('This value isn\'t a valid IPv4')
    return super().__getresponse__(f'/api/ipr/{dns}',auth=(credentials.get('key'), credentials.get('password')))

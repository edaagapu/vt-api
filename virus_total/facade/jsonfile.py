from .base import Facade
import json
from datetime import datetime
from os.path import join

class JSONFacade(Facade):
  def open(self):
    return super().open('Abrir archivo JSON', (('Archivo JSON', '*.json'), ))


  def load(self, path):
    return open(path)


  def res_file(self, **kwargs):
    return super().res_file('Guardar fichero', '.json', **kwargs)


  def save(self, path, **kwargs):
    data = kwargs.get('data', {})
    with open(join(path, datetime.now().strftime('%d%m%Y_%H%M%S.json')), 'w') as json_file:
      json_file.write(json.dumps(data))


  def custom_process(self, headers, data, **kwargs):
    results = []
    for info in data:
      obj = {}
      for index, header in enumerate(headers):
        obj[header] = info[index]
      results.append(obj)
    return {'results': results}

from base import Facade
import json

class JSONFacade(Facade):
  def __init__(self):
    super().__init__()
    

  def open(self):
    super().open('Abrir archivo JSON', (('Archivo JSON', '*.json'), ))
    with open(self.path,) as json_file:
      self.src_file = json.load(json_file)


  def save(self, same_route, initialdir, **kwargs):
    super().save(same_route, 'Guardar fichero', '.json', initialdir=initialdir)
    data = kwargs.get('data', {})
    with open(self.path, 'w') as json_file:
      json_file.write(json.dumps(data))


  def custom_process(self, headers, data, **kwargs):
    results = []
    for info in data:
      obj = {}
      for index, header in enumerate(headers):
        obj[header] = info[index]
      results.append(obj)
    return {'results': results}

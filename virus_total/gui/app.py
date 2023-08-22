from tkinter import Tk, Menu, messagebox as MessageBox
from .components import ApplicationFrame, ImportationFrame
from .views import SettingsView
from os.path import join, dirname, abspath
from encrypt import JWTEncrypt
from api import *
import datetime
from openpyxl import load_workbook, Workbook

_ICON_FILE = join(dirname(abspath(__file__)), 'icons\main.ico')

class AppController:
  def set_path(self, path):
    self.appFrame.path_text.set(path)

  def select_provider(self, provider):
    if provider == 'IBM':
      return IBMAPI()
    elif provider == 'VT':
      return VTAPI()
    
  def import_data(self):
    wb = load_workbook(self.appFrame.path_text.get())
    ws = wb.active
    return list(map(lambda cell: cell.value, ws['A']))
  
  def classify_to_dict(self, values, is_classified=False):
    if is_classified:
      r_results = values
    else:
      r_results = self.classify(values)
    
    results = {
      'dns': [],
      'hash': {
        'md5': [],
        'sha1': [],
        'sha256': [],
        'unknown': []
      },
      'ip': [],
      'unknown': [],
      'url': [],
    }

    for value, value_type in r_results:
      if 'hash' in value_type.lower():
        results['hash'][value_type.lower().split('-')[1].strip()].append(value)
      else:
        results[value_type.lower()].append(value)
    return results


  def classify(self, values):
    results = []
    for value in values:
      if VTAPI.__isipv4__(value):
        results.append((value, 'IP'))
      elif VTAPI.__ishash__(value):
        results.append((value, f'Hash - {VTAPI.hash_type(value)}'))
      elif VTAPI.__isdns__(value):
        results.append((value, 'DNS'))
      elif VTAPI.__isurl__(value):
        results.append((value, 'URL'))
      else:
        results.append((value, 'Unknown'))
    return results

  def run_api(self):
    encrypt = JWTEncrypt()
    key = encrypt.load_key()
    settings = encrypt.load_settings(key)

    providers = list(map(lambda x: x.split('_')[0].upper(),filter(lambda x: 'key' in x, settings.keys())))

    full_path = join(settings.get('export_path'), datetime.datetime.now().strftime('%d%m%Y_%H%M%S.xlsx'))

    wb = Workbook()
    ws = wb.get_sheet_by_name('Sheet')
    wb.remove(ws)
    values = self.import_data()
    sheetnames = ['Original'] + providers
    for sheetname in sheetnames:
      wb.create_sheet(sheetname)
    
    c_values = self.classify(values)
    ws = wb.get_sheet_by_name('Original')
    for value in c_values:
      ws.append(value)
    # print(self.classify_to_dict(c_values, True))
    
    for provider in providers:
      provider_keys = settings.get('%s_keys'.format(provider.lower()))
      ws = wb.get_sheet_by_name(provider)
      api = self.select_provider(provider)
      
      # ws['A1'] = 'Hello'
    wb.save(full_path)
 
class App(Tk, AppController):
  in_work = False

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.title('Cerberus')
    self.create_widgets()
    self.create_menubar()

    self.config(menu=self.menubar, width=500, height=500)
    self.iconbitmap(_ICON_FILE)

  def create_menubar(self):
    menu_items = {
      'Archivo': [('Importar archivo', self.impFrame.import_file), '/', ('Salir', self.destroy)],
      'Configuración': [('Propiedades', self.run_api)],
      'Ayuda': ['Ayuda', '/', 'Acerca de']
    }

    self.menubar = Menu(self)

    for item in menu_items.keys():
      submenu = Menu(self.menubar, tearoff=0)
      for subitem in menu_items[item]:
        if type(subitem) == str:
          if subitem == '/':
            submenu.add_separator()
          else:
            submenu.add_command(label=subitem)
        elif type(subitem) == tuple:
          submenu.add_command(label=subitem[0], command=subitem[1])
      self.menubar.add_cascade(label=item, menu=submenu)

  def create_widgets(self):
    feature = {'bg': '#E9E9E9', 'bd': 1, 'relief': 'solid'}
    self.appFrame = ApplicationFrame(self, color=feature.get('bg'))
    self.impFrame = ImportationFrame(self, color=feature.get('bg'))
    self.appFrame.config(**feature)
    self.impFrame.config(**feature)

  def destroy(self):
    result = True
    while (SettingsView.in_use):
      self.impFrame.destroy()
    if self.__class__.in_work:
      result = MessageBox.askokcancel('Salir', '¿Desea salir de la aplicación sin terminar de ejecutar el proceso?')
    if result:
      super().destroy()


if __name__ == '__main__':
  app = App()
  app.mainloop()
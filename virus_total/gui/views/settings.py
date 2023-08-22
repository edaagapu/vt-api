from tkinter import Toplevel, PhotoImage, Listbox, StringVar, filedialog as FileDialog, messagebox as MessageBox
from tkinter.ttk import Button, Style, Label, Scrollbar
from os.path import join, dirname, abspath
from .c_dialog import CustomDialog
from encrypt import JWTEncrypt

_ICON_FILEPATH = join(dirname(dirname(abspath(__file__))), 'icons')

class SettingsController:
  def change_export_path(self):
    self._settings['export_path'] = self._export_path.get()
    self.__class__.has_change = True


  def __add_key__(self, key, app):
    token = self.encrypt.encrypt(data_dict=key, key=self._key)
    if not self._settings.get(f'{app}_keys', None):
      self._settings[f'{app}_keys'] = []
    self._settings[f'{app}_keys'].append(token)
    self.__class__.has_change = True
    return token


  def __remove_key__(self, index, app):
    r_value = self._settings[f'{app}_keys'][index]
    self._settings[f'{app}_keys'].remove(r_value)
    self.__class__.has_change = True


class SettingsView(Toplevel, SettingsController):
  in_use = False
  has_change = False
  get_icon = lambda self, icon: join(_ICON_FILEPATH, icon)

  def __init__(self, *args, **kwargs):
    self.encrypt = kwargs.pop('encrypt', None)
    if not self.encrypt:
      self.encrypt = JWTEncrypt()
    super().__init__(*args, **kwargs)
    self.title('Configuración')
    self.config(width=500, height=500)
    self.resizable(width=False, height=False)
    self.geometry('+600+10')
    self.config(background='#E9E9E9')
    self.create_vars()
    self.create_widgets()
    self.insert_elements()
    self.iconbitmap(self.get_icon('main.ico'))
    self.__class__.in_use = True
    

  def create_vars(self):
    self._key = self.encrypt.load_key()
    self._settings = self.encrypt.load_settings(self._key)
    self.icons = [PhotoImage(file=self.get_icon('logout.png').encode('unicode_escape')).subsample(25,25)]
    self.listInfo = []
    self.intButtons = []
    self.scrollbars = []
    self._apps = ('vt', 'ibm')
    self._export_path = StringVar(value=self._settings.get('export_path'))
    

  def create_widgets(self, color='#E9E9E9'):
    titles = ('Llave(s) Virus Total: ', 'Llave(s) IBM X-Change: ')
    infButtons = [
      ((self.get_icon('filepath.png'), self.change_export_path),),
      ((self.get_icon('plus.png'), lambda: self.add_key(self._apps[0], 1)) ,(self.get_icon('minus.png'), lambda: self.remove_key(self._apps[0], 1))),
      ((self.get_icon('plus.png'), lambda: self.add_key(self._apps[1], 2)) ,(self.get_icon('minus.png'), lambda: self.remove_key(self._apps[1], 2))),
    ]
    self.general_style = Style()
    self.general_style.configure('CGeneral.TLabel', background=color, font = ('Calibri', 10))

    self.listInfo.append(Label(self, textvariable=self._export_path,  style='CGeneral.TLabel', wraplength=198, anchor='nw'))
    self.listInfo[0].place(x=150, y=10, width=215, height=100)

    label = Label(self, text='Ruta de archivos exportados:', style='CGeneral.TLabel', wraplength=120, anchor='nw')
    label.place(x=10, y=10, width=120, height=50)
    
    for index, title in enumerate(titles):
      label = Label(self, text=title, style='CGeneral.TLabel', wraplength=120, anchor='nw')
      label.place(x=10, y=120+(index*110), width=120, height=50)
      
      self.listInfo.append(Listbox(self, background=color))
      self.scrollbars.append(Scrollbar(self, orient='vertical', command=self.listInfo[-1].yview))
      self.scrollbars[-1].place(x=350, y=120+(index*110), width=15, height=100)
      self.listInfo[-1].config(yscrollcommand=self.scrollbars[-1].set)
      self.listInfo[-1].place(x=150, y=120+(index*110), width=200, height=100)

    for index, btn_source in enumerate(infButtons):
      for index_t, btn_info in enumerate(btn_source):
        self.icons.append(PhotoImage(file=self.get_icon(btn_info[0]).encode('unicode_escape')).subsample(40,40))
        self.intButtons.append(Button(self, image=self.icons[-1], compound='center', command=btn_info[1]))
        self.intButtons[-1].place(x=370+(45*index_t), y=15+(110*index), width=40, height=40)
    self.btnQuit_style = Style()
    self.btnQuit_style.configure('SettingsQuit.TButton', font = ('Calibri', 10))

    self.btnQuit = Button(self, image=self.icons[0], style='SettingsQuit.TButton', compound='left', text='Salir', command=self.destroy)
    self.btnQuit.place(x=420, y=460, width=70, height=30)

  def insert_elements(self):
    for index, app in enumerate(self._apps):
      list_keys = self._settings.get(f'{app}_keys', None)
      if list_keys:
        self.listInfo[index+1].insert('end', *[f'{app.upper()} {i+1}' for i in range(len(list_keys))])

  def change_export_path(self):
    self._export_path.set(FileDialog.askdirectory(title='Escoger ruta de exportación'))
    super().change_export_path()


  def add_key(self, app, index):
    if app == 'vt':
      labels = ['Llave: ']
    elif app == 'ibm':
      labels = ['Llave: ', 'Contrasenia: ']
    results = CustomDialog(self, labels).show()
    
    if len(results) == len(labels):
      key = {}
      for e_index, label in enumerate(labels):
        key[label.lower().split(':')[0]] = results[e_index]
      self.__add_key__(key, app)
      if self.listInfo[index].size():
        number = int(self.listInfo[index].get('end').split(' ')[-1])
        self.listInfo[index].insert('end', f'{app.upper()} {number+1}')
      else:
        self.listInfo[index].insert('end', f'{app.upper()} 1')
  

  def remove_key(self, app, index):
    e_indexes = self.listInfo[index].curselection()
    for e_index in e_indexes[::-1]:
      self.__remove_key__(e_index, app)
    self.listInfo[index].delete(e_indexes)


  def destroy(self):
    if self.__class__.has_change:
      result = MessageBox.askyesno('Salir', '¿Desea guardar los cambios que realizo en la configuración?')
      if result:
        self.save_key()
        self.save_settings()
      else:
        self.load_key()
        self.load_settings()
    self.__class__.in_use = False
    self.__class__.has_change = False
    super().destroy()

from tkinter import Frame, PhotoImage
from controller import ImportationController
from tkinter.ttk import Button, Style
from os.path import join, dirname, abspath

_ICON_PATH = join(dirname(dirname(abspath(__file__))), 'icons')

class ImportationFrame(Frame, ImportationController):
  create_icon = lambda self, image_name: self.images.append(PhotoImage(file=join(_ICON_PATH, image_name).encode('unicode_escape')).subsample(30,30))

  def __init__(self, master=None, color='#FFFFFF', *args, **kwargs):
    super().__init__(master, *args, **kwargs)
    self.master = master
    self.create_vars()
    self.create_widgets(color)
    self.place(relwidth=0.98, relheight=0.23, relx=0.01, rely=0.76)

  def create_vars(self):
    self.settingsView = None
    self.buttons = []
    self.images = []

  def create_widgets(self, color):
    self.button_style = Style()
    self.button_style.configure('IF.TButton', color=color, font = ('Calibri', 10), borderwidth='1', )
    features_buttons = (
      { 'icon': 'import.png', 'text' : 'Importar Archivo', 'command': self.importFile},
      { 'icon': 'settings.png', 'text' : 'Configuración', 'command': self.openSettingsView},
      { 'icon': 'info.png', 'text' : 'Manual', 'command': self.openHelpHyperlink},
    )
    
    for index, feature in enumerate(features_buttons):
      self.create_icon(feature.pop('icon'))
      self.buttons.append(Button(self, image=self.images[index], style='IF.TButton', compound='left', **feature))
      self.buttons[index].place(relx=0.05+(0.3*index), rely=0.1, relheight=0.3, relwidth=0.27)
    
    self.create_icon('logout.png')
    self.buttons.append(Button(self, image=self.images[-1], compound='left', text='Salir', style='IF.TButton', command=self.master.destroy))
    self.buttons[-1].place(relx=0.8, rely=0.65, relheight=0.3, relwidth=0.15)

  

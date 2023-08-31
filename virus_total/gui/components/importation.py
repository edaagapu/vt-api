from tkinter import Frame, PhotoImage, filedialog as FileDialog, messagebox as MessageBox
from tkinter.ttk import Button, Style
from os.path import join, dirname, abspath
from gui.views import SettingsView
import webbrowser

_ICON_PATH = join(dirname(dirname(abspath(__file__))), 'icons')

class ImportationController:
  def open_settings_view(self):
    if not SettingsView.in_use:
      try:
        SettingsView(self)
      except Exception as error:
        MessageBox.showerror('Error', error)

  def import_file(self):
    return FileDialog.askopenfilename(
      title='Abrir un fichero',
      filetypes=(('Archivos JSON', '*.json'), ('Archivos Excel (2007-*)', '*.xlsx'), ('Archivos CSV', '*.csv'))
    )
  
  def open_help_hyperlink(self):
    webbrowser.open('https://www.google.com/')


class ImportationFrame(Frame, ImportationController):
  create_icon = lambda self, image_name: self.images.append(PhotoImage(file=join(_ICON_PATH, image_name).encode('unicode_escape')).subsample(30,30))

  def __init__(self, master=None, color='#FFFFFF', *args, **kwargs):
    super().__init__(master, *args, **kwargs)
    self.master = master
    self.create_vars()
    self.create_widgets(color)
    self.place(relwidth=0.98, relheight=0.23, relx=0.01, rely=0.76)
    self.master.geometry('+0+0')

  def create_vars(self):
    self.settingsView = None
    self.buttons = []
    self.images = []

  def create_widgets(self, color):
    self.button_style = Style()
    self.button_style.configure('IF.TButton', color=color, font = ('Calibri', 10), borderwidth='1', )
    features_buttons = (
      { 'icon': 'import.png', 'text' : 'Importar Archivo', 'command': self.import_file},
      { 'icon': 'settings.png', 'text' : 'Configuración', 'command': self.open_settings_view},
      { 'icon': 'info.png', 'text' : 'Manual', 'command': self.open_help_hyperlink},
    )
    
    for index, feature in enumerate(features_buttons):
      self.create_icon(feature.pop('icon'))
      self.buttons.append(Button(self, image=self.images[index], style='IF.TButton', compound='left', **feature))
      self.buttons[index].place(relx=0.05+(0.3*index), rely=0.1, relheight=0.3, relwidth=0.27)
    
    self.create_icon('logout.png')
    self.buttons.append(Button(self, image=self.images[-1], compound='left', text='Salir', style='IF.TButton', command=self.master.destroy))
    self.buttons[-1].place(relx=0.8, rely=0.65, relheight=0.3, relwidth=0.15)

  def import_file(self):
    filepath = super().import_file()
    self.master.set_path(filepath)

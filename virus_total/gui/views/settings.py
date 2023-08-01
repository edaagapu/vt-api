from tkinter import Toplevel, Button
from controller import SettingsController
from os.path import join, dirname, abspath

_ICON_FILE = join(dirname(dirname(abspath(__file__))), 'icons\main.ico')

class SettingsView(Toplevel, SettingsController):
  in_use = False

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.title('Configuración')
    self.config(width=300, height=200)
    self.create_vars()
    self.create_widgets()
    self.iconbitmap(_ICON_FILE)
    self.__class__.in_use = True

  def create_vars(self):
    pass

  def create_widgets(self):
    self.btnQuit = Button(self, text='Quit', fg='red', command=self.destroy)
    self.btnQuit.place(relx=0.8, rely=0.85, relwidth=0.18, relheight=0.14)

  def destroy(self):
    self.__class__.in_use = False
    super().destroy()

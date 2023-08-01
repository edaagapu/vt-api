from tkinter import Toplevel, Button, Tk, StringVar
from controller import SettingsController

class SettingsView(Toplevel, SettingsController):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.title('Configuración')
    self.config(width=300, height=200)
    self.create_vars()
    self.create_widgets()

  def create_vars(self):
    pass

  def create_widgets(self):
    self.btnQuit = Button(self, text='Quit', fg='red', command=self.destroy)
    self.btnQuit.place(x=75, y=75)

  def destroy(self):
    super().destroy()

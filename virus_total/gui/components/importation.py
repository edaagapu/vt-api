from tkinter import Frame, Button, StringVar, messagebox as MessageBox
from controller import ImportationController
from settings import SettingsView

class ImportationFrame(Frame, ImportationController):
  def __init__(self, master=None, *args, **kwargs):
    super().__init__(master, *args, **kwargs)
    self.master = master
    self.create_vars()
    self.create_widgets()
    self.place(relwidth=0.98, height=200, y=210, relx=0.01, rely=0.01)

  def create_vars(self):
    self.hi = StringVar(self.master, 'Hello World! (Click me)')

  def create_widgets(self):
    self.settingsView = None
    self.buttons = []
    features_buttons = [
      ({ 'text' : 'Importar Archivo', 'command': self.openSettingsView},{'x': 100, 'y': 10}),
      ({ 'text' : 'Configuración', 'command': self.openSettingsView},{'x': 50, 'y': 10}),
      ({ 'text' : 'Manual', 'command': self.openSettingsView},{ 'relx': 0.9, 'y': 150}),
      ({ 'text' : 'Salir', 'command': self.destroy_view},{ 'x': 10, 'y': 10}),
    ]
    
    for feature, place in features_buttons:
      self.buttons.append(Button(self, **feature))
      self.buttons[-1].place(**place)

  def openSettingsView(self):
    if not self.settingsView:
      self.settingsView = SettingsView(self)
  
  def destroy_view(self):
    result = MessageBox.askokcancel('Salir', '¿Desea salir de la aplicación sin guardar?')
    if result:
      super().destroy()
      self.master.destroy()

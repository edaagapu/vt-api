from tkinter import Frame, Button, StringVar, messagebox as MessageBox
from controller import ApplicationController
from settings import SettingsView

class ApplicationFrame(Frame, ApplicationController):
  def __init__(self, master=None, *args, **kwargs):
    super().__init__(master, *args, **kwargs)
    self.master = master
    self.create_vars()
    self.create_widgets()
    self.place(relwidth=0.98, height=200, relx=0.01, rely=0.01)

  def create_vars(self):
    self.hi = StringVar(self.master, 'Hello World! (Click me)')

  def create_widgets(self):
    self.settingsView = None

    settings = { 'textvariable' : self.hi, 'command': self.openSettingsView, 'width': 20, 'height': 2}

    self.btnHi = Button(self, **settings)
    self.btnHi.place(x=10, y=10)

    self.btnQuit = Button(self, text='Quit', fg='red', command=self.destroy_view)
    self.btnQuit.place(relx=0.9, y=150)

  def openSettingsView(self):
    if not self.settingsView:
      self.settingsView = SettingsView(self)
  
  def destroy_view(self):
    result = MessageBox.askokcancel('Salir', '¿Desea salir de la aplicación sin guardar?')
    if result:
      super().destroy()
      self.master.destroy()

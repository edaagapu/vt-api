from tkinter import Frame, Button, Tk, StringVar
from settings import SettingsView
from components import ApplicationFrame, ImportationFrame

class Main(Tk):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.config(width=500, height=500)
    self.title('Cerberus')
    self.create_widgets()

  def create_widgets(self):
    self.appFrame = ApplicationFrame(self, bg='blue')
    self.impFrame = ImportationFrame(self, bg='yellow')



if __name__ == '__main__':
  app = Main()
  app.mainloop()
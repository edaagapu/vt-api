from tkinter import Tk, Menu, messagebox as MessageBox
from components import ApplicationFrame, ImportationFrame
from os.path import join, dirname, abspath
from views import SettingsView

_ICON_FILE = join(dirname(abspath(__file__)), 'icons\main.ico')


class App(Tk):
  in_work = False

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.create_menubar()
    self.config(menu=self.menubar, width=500, height=500)
    self.title('Cerberus')
    self.create_widgets()
    self.iconbitmap(_ICON_FILE)

  def create_menubar(self):
    menu_items = {
      'Archivo': ['Importar archivo', '/', ('Salir', self.destroy)],
      'Configuración': ['Personalización', '/', 'Propiedades'],
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
from views import SettingsView
from tkinter import filedialog as FileDialog
import webbrowser

class ImportationController:
  def openSettingsView(self):
    if not SettingsView.in_use:
      SettingsView(self)

  def importFile(self):
    return FileDialog.askopenfilename(
      title='Abrir un fichero',
      filetypes=(('Archivos JSON', '*.json'), ('Archivos Excel (2007-*)', '*.xlsx'), ('Archivos CSV', '*.csv'))
    )
  
  def openHelpHyperlink(self):
    webbrowser.open('https://www.google.com/')
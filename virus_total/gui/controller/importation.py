from views import SettingsView
from tkinter import filedialog as FileDialog, messagebox as MessageBox
import webbrowser

class ImportationController:
  def openSettingsView(self):
    if not SettingsView.in_use:
      try:
        SettingsView(self)
      except Exception as error:
        MessageBox.showerror('Error', error)

  def importFile(self):
    return FileDialog.askopenfilename(
      title='Abrir un fichero',
      filetypes=(('Archivos JSON', '*.json'), ('Archivos Excel (2007-*)', '*.xlsx'), ('Archivos CSV', '*.csv'))
    )
  
  def openHelpHyperlink(self):
    webbrowser.open('https://www.google.com/')
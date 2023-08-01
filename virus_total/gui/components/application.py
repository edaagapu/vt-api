from tkinter import Frame, StringVar, IntVar, Label, Text, VERTICAL
from controller import ApplicationController
from tkinter.ttk import Progressbar, Scrollbar


class ApplicationFrame(Frame, ApplicationController):
  def __init__(self, master=None, color='#FFFFFF',  *args, **kwargs):
    super().__init__(master, *args, **kwargs)
    self.master = master
    self._featuresBars = ( 'Virus Total',  'IBM X-Change' )
    self.create_vars()
    self.create_widgets(color)
    self.place(relwidth=0.98, relheight=0.74, relx=0.01, rely=0.01)

  def create_vars(self):
    self.logText = StringVar(self.master, 'Hello World! (Click me)')
    self.progressNumbers = [IntVar(self.master, 100) for _ in self._featuresBars]

  def create_widgets(self, color):
    self.settingsView = None
    self.progressBars = []
    self.txtProgress = Text(self, font=('Consolas', 8), background=color, padx=10, pady=10)
    self.txtProgress.config(state='disabled')
    
    self.txtProgress.place(relx=0.52, rely=0.03, relheight=0.94, relwidth=0.42)

    self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.txtProgress.yview)
    self.scrollbar.place(relx=0.95, rely=0.03, relheight=0.94)
    self.txtProgress.config(yscrollcommand=self.scrollbar.set)

    for index,t_label in enumerate(self._featuresBars):
      Label(self, text=f'{t_label} ({self.progressNumbers[index].get()}%):', anchor='w', bg=color).place(relx=0.02, rely=0.1+(0.26*index), relwidth=0.46, relheight=0.04)
      self.progressBars.append(Progressbar(self, maximum=100.1))
      self.progressBars[index].step(self.progressNumbers[index].get())
      self.progressBars[index].place(relx=0.02, rely=0.16+(0.26*index), relwidth=0.46, relheight=0.08)


from tkinter import Toplevel, StringVar, Label, Entry, Button, messagebox as MessageBox

class CustomDialog(Toplevel):
  in_use = False

  def __init__(self, parent, labels):
    Toplevel.__init__(self, parent)
    self.labels = []
    self.entries = []
    self.vars = []

    for index, label in enumerate(labels):
      self.vars.append(StringVar())
      self.labels.append(Label(self, text=label, anchor='e'))
      self.labels[index].place(relx=0.05, y=10+(index*40), relwidth=0.40, height=20)
      self.entries.append(Entry(self, textvariable=self.vars[index]))
      self.entries[index].place(relx=0.5, y=10+(index*40), relwidth=0.45, height=20)
    
    self.ok_button = Button(self, text='Enviar', command=self.on_ok)
    self.ok_button.place(relx=0.55, rely=0.80, relwidth=0.4, height=30)

  
  def on_ok(self):
    if self.is_empty():
      MessageBox.showwarning('Campos vacíos', 'Debe llenar todos los campos')
      self.focus_force()
    else:
      self.destroy()
      self.__class__.in_use = False


  def is_empty(self):
    for var in self.vars:
      if not var.get():
        return True
    return False


  def show(self):
    self.wm_deiconify()
    self.wait_window()
    if self.is_empty():
      return []
    else:
      return [var.get() for var in self.vars]
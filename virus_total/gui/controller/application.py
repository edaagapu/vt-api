class ApplicationController:
  def set_text(self):
    self.txtProgress.config(state='normal')
    self.txtProgress.delete('1.0', 'end')
    self.txtProgress.insert('1.0', self.progressText.get())
    self.txtProgress.config(state='disabled')
  
  def append_text(self):
    self.txtProgress.config(state='normal')
    self.txtProgress.insert('end', self.progressText.get())
    self.txtProgress.config(state='disabled')
  
  def get_text(self):
    return self.txtProgress.get(1.0, 'end-1c')
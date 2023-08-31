from tkinter import filedialog as FileDialog

class Facade:
  def __init__(self):
    self.path = ''
    self.src_file = None


  def open(self, title, filetypes):
    self.path = FileDialog.askopenfilename(title=title,filetypes=filetypes)


  def save(self, same_route, title, defaultextension, data=None, **kwargs):
    if not same_route:
      self.path = FileDialog.asksaveasfilename(title=title, defaultextension=defaultextension, **kwargs)


  def __extract_data__(self, data):
    if type(data[0]) == list or type(data[0] == tuple):
      headers = data[0]
      t_data = data[1:]
    elif type(data[0]) == dict:
      headers = data[0].keys()
      t_data = []
      for info in data:
        t_data.append([info.get(header) for header in headers])
    else:
      raise TypeError('The information hasn\'t in correct type')
    return headers, t_data


  def custom_process(self, headers, data, **kwargs):
    return None

  def process_data(self, data, is_saved=True, same_route=True, initialdir='', **kwargs):
    headers, t_data =  super().__extract_data__(data)
    data = self.custom_process(headers, data=t_data, **kwargs)
    if is_saved:
      self.save(same_route, initialdir, data)
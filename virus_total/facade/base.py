from tkinter import filedialog as FileDialog

class Facade:
  def open(self, title, filetypes):
    return FileDialog.askopenfilename(title=title,filetypes=filetypes)


  def load(self, path):
    return None


  def res_file(self, title, defaultextension, **kwargs):
    return FileDialog.asksaveasfilename(title=title, defaultextension=defaultextension, **kwargs)


  def save(self, path):
    pass


  def __extract_data__(self, data):
    if type(data[0]) == list or type(data[0]) == tuple:
      headers = data[0]
      t_data = data[1:]
    elif type(data[0]) == dict:
      headers = tuple(data[0].keys())
      t_data = []
      for info in data:
        t_data.append([info.get(header) for header in headers])
    else:
      raise TypeError('The information hasn\'t in correct type')
    print(headers)
    print(t_data)
    print('*'*40)
    return headers, t_data


  def custom_process(self, headers, data, **kwargs):
    return None

  def process_data(self, data, initialdir='', **kwargs):
    headers, t_data =  self.__extract_data__(data)
    print(headers)
    print(t_data)
    data = self.custom_process(headers, data=t_data, **kwargs)
    return data
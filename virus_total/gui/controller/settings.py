from .__encrypt__ import encrypt, decrypt, get_key, get_reverse_key

class SettingsController:
  def load_key(self, fp_key='.key'):
    try:
      with open(fp_key, 'r') as f_key:
        self._key = get_key(f_key.read())
    except FileNotFoundError:
      self._key = 'nHtoFqfAtYjSGG6QawGR9HEBrvepmFbNf4mx0jNL21c1k23z95'


  def save_key(self, fp_key='.key'):
    with open(fp_key, 'w') as f_key:
      f_key.write(get_reverse_key(self._key))


  def save_settings(self, fp_settings='.settings'):
    with open(fp_settings, 'w') as f_settings:
      if not self._settings:
        self._settings = {}
      encoded = encrypt(data_dict=self._settings, key=self._key)
      f_settings.write(encoded)


  def load_settings(self, fp_settings='.settings'):
    try:
      with open(fp_settings, 'r') as f_settings:
        token = f_settings.read()
      self._settings = decrypt(token=token, key=self._key)
    except FileNotFoundError:
      self._settings = {'export_path': 'C:\\'}


  def change_export_path(self):
    self._settings['export_path'] = self._export_path.get()
    self.__class__.has_change = True


  def __add_key__(self, key, app):
    token = encrypt(data_dict=key, key=self._key)
    if not self._settings.get(f'{app}_keys', None):
      self._settings[f'{app}_keys'] = []
    self._settings[f'{app}_keys'].append(token)
    self.__class__.has_change = True
    return token


  def __remove_key__(self, index, app):
    r_value = self._settings[f'{app}_keys'][index]
    self._settings[f'{app}_keys'].remove(r_value)
    self.__class__.has_change = True

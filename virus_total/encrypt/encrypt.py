import jwt

class JWTEncrypt:
  def __init__(self, **kwargs):
    pass

  def __encrypt_jwt__(self, data_dict, key, algorithm='HS256'):
    return jwt.encode(data_dict, key, algorithm)


  def __decrypt_jwt__(self, token, key, algorithms=['HS256']):
    return jwt.decode(token, key, algorithms)


  def encrypt(self, **kwargs):
    return self.__encrypt_jwt__(**kwargs)


  def decrypt(self, **kwargs):
    return self.__decrypt_jwt__(**kwargs)


  def get_key(self, r_key):
    key = ''
    for n in range(0,len(r_key),3):
      key += chr(int(r_key[n:n+3]))
    return key


  def get_reverse_key(self, key):
    r_key = ''
    for c in key:
      number = ord(c)
      r_key += f'{number:03d}'
    return r_key
  

  def load_key(self, fp_key='.key'):
    try:
      with open(fp_key, 'r') as f_key:
        return self.get_key(f_key.read())
    except FileNotFoundError:
      return 'nHtoFqfAtYjSGG6QawGR9HEBrvepmFbNf4mx0jNL21c1k23z95'


  def save_key(self, key, fp_key='.key'):
    with open(fp_key, 'w') as f_key:
      f_key.write(self.encrypt.get_reverse_key(key))


  def save_settings(self, key, settings, fp_settings='.settings'):
    with open(fp_settings, 'w') as f_settings:
      encoded = self.encrypt(data_dict=settings, key=key)
      f_settings.write(encoded)


  def load_settings(self, key, fp_settings='.settings'):
    try:
      with open(fp_settings, 'r') as f_settings:
        token = f_settings.read()
      return self.decrypt(token=token, key=key)
    except FileNotFoundError:
      return {'export_path': 'C:\\'}
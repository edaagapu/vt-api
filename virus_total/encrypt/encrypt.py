import jwt

class JWTEncrypt:
  def __init__(self):
    pass

  def __encryptJWT__(self, data_dict, key, algorithm='HS256'):
    return jwt.encode(data_dict, key, algorithm)


  def __decryptJWT__(self, token, key, algorithms=['HS256']):
    return jwt.decode(token, key, algorithms)


  def encrypt(self, **kwargs):
    return self.__encryptJWT__(**kwargs)


  def decrypt(self, **kwargs):
    return self.__decryptJWT__(**kwargs)


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
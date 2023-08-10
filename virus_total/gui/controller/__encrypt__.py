import jwt

def __encryptJWT__(data_dict, key, algorithm='HS256'):
  return jwt.encode(data_dict, key, algorithm)


def __decryptJWT__(token, key, algorithms=['HS256']):
  return jwt.decode(token, key, algorithms)


def encrypt(**kwargs):
  return __encryptJWT__(**kwargs)


def decrypt(**kwargs):
  return __decryptJWT__(**kwargs)


def get_key(r_key):
  key = ''
  for n in range(0,len(r_key),3):
    key += chr(int(r_key[n:n+3]))
  return key


def get_reverse_key(key):
  r_key = ''
  for c in key:
    number = ord(c)
    r_key += f'{number:03d}'
  return r_key
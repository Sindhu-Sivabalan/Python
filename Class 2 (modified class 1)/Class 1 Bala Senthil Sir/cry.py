from cryptography.fernet import Fernet

mykey=Fernet.generate_key()
cipher=Fernet(mykey)

enctxt=cipher.encrypt(b'welcome123')
print(enctxt)

dtext=cipher.decrypt(enctxt)
print(dtext)

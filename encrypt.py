import pyAesCrypt

password = input('Введите пароль для шифрования файла: ')

# encrypt
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

# decrypt
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)
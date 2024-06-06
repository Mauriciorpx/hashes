from socket import *
import hashlib

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

word = input('Escriba una palabra de 4 letras: ')

if len(word) != 4:
    print('Error: La palabra debe tener 4 letras.')
    exit()

hashed_word = hashlib.md5(word.encode()).hexdigest()

clientSocket.send(hashed_word.encode())

modifiedSentence = clientSocket.recv(1024)
print('Recibido del servidor: ', modifiedSentence.decode())

clientSocket.close()
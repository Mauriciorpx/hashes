from socket import *
import hashlib
import itertools
import time

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Servidor TCP Listo')

while True:
    connectionSocket, addr = serverSocket.accept()
    hashed_word = connectionSocket.recv(1024).decode()

    start_time = time.time()

    decrypted_word = ""
    for combination in itertools.product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", repeat=4):
        word = ''.join(combination)
        hashed_combination = hashlib.md5(word.encode()).hexdigest()
        if hashed_combination == hashed_word:
            decrypted_word = word
            break

    end_time = time.time()
    elapsed_time = end_time - start_time

    connectionSocket.send(decrypted_word.encode())
    print("Palabra descifrada enviada al cliente:", decrypted_word)
    print("Tiempo transcurrido:", elapsed_time)

    connectionSocket.close()
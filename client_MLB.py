from socket import *

theHostname = '127.0.0.1'
portNum     = 4567
client  = socket(AF_INET, SOCK_STREAM)
client.connect((theHostname, portNum))
sentInfo = input("Enter MLB Team name (CAPITALIZED): ")
client.send(sentInfo.encode())
while True:
    charsArrive = client.recv(1024)
    print(charsArrive.decode())

    if not charsArrive:
        break

client.close()

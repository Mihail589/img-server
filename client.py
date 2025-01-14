import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.0.4', 1111))

flag = True
while flag:
    msg = client.recv(1000000)
    #print(msg.decode('utf-8'))
    if len(msg) != 0:
        with open("img.png", "wb") as file:
            print("Проверка")
            file.write(msg)
client.close()
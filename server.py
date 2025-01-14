import socket
import cv2
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.0.4', 1111))

server.listen()

client, address = server.accept()

flag = True
cam = cv2.VideoCapture(0)
ret_val, img = cam.read()
cv2.imwrite("Data.png", img)
print(type(img))
with open("Data.png", "rb") as file:
    client.send(file.read())
client.close()
server.close()
import socket

HOST = '172.19.74.136'
PORT = 8089
ADDR = (HOST,PORT)
BUFSIZE = 4096
videoclip = "/root/ekta/video/Demo_video.mp4"

bytes = open(videoclip).read()

print len(bytes)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(bytes)

client.close()

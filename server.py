import socket

HOST = ''
PORT = 8089
ADDR = (HOST,PORT)
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)
server.listen(5)

print 'listening ...'

while True:
    conn, addr = server.accept()
    print 'client connected ... ', addr
    myfile = open('out.mp4', 'w')
    
    while True:
        data = conn.recv(BUFSIZE)
        if not data:
            break
        myfile.write(data)
        print 'writing file ....'

    myfile.close()
    print 'finished writing file'
    conn.close()
    print 'client disconnected'

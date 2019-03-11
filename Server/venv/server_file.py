import  socket
import struct
def recvall(conn, length):
    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf

def sending_and_reciveing():
    s = socket.socket()
    print('socket created ')
    port = 1234
    s.bind(('127.0.0.1', port)) #bind port with ip address
    print('socket binded to port ')
    s.listen(5)#listening for connection
    print('socket listensing ... ')

    while True:
        client, addr = s.accept()  # when port connected
        print("\ngot connection from ", addr)

        print 'got connected from', addr
        length = recvall(client, 262144)
        if not length: break
        print(length)
        with open('image.jpg', 'wb') as image_file:
            image_file.write(length)
        client.send('Thanks')  # echo


sending_and_reciveing()#calling the function to run server
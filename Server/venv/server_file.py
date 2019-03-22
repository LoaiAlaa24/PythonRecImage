import  socket
import struct
def recvall(conn, length,buf):

    while len(buf) < length:
        print(len(buf))
        data = conn.recv(524288)
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
    i = 0 ;
    while True:
        i+=1
        print(i)
        if(i==1):
            client, addr = s.accept()  # when port connected
            print("\ngot connection from ", addr)

        print 'got image from', addr
        buf=b""
        length=""
        length = recvall(client, 524288,buf)
        if not length:
            break
        print("--------------------------")
        print(length)
        with open('image'+str(i)+'.jpg', 'wb') as image_file:
            image_file.write(length)
        # client.send('Thanks')  # echo


sending_and_reciveing()#calling the function to run server
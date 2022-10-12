from socket import *
import time
from multiprocessing.context import Process
import sys

class FTimer_Client(Process):
    def __init__(self,HOST,PORT):
        super().__init__()
        self.HOST = HOST
        self.PORT = PORT
        pass

    def run_client(self):
        clientmode(self.HOST,self.PORT)

def clientmode(HOST,PORT):
    # HOST = '0.0.0.0'
    # PORT = 7000

    if(PORT>65535 or PORT<1024):
        print("Error: port number must be in the range 1024 to 65535")
        return 
    
    msgdata = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"


    clientsocket = socket(AF_INET,SOCK_STREAM)
    clientsocket.connect((HOST,PORT))

    senddata = "hello tcp"
    print('send:'+senddata)
    clientsocket.send(senddata.encode())

    recvdata = clientsocket.recv(1024)
    print('recv: ' + recvdata.decode())

    clientsocket.close()

def servermode(PORT):
    HOST = '0.0.0.0'
    #PORT = 7000

    serversocket = socket(AF_INET,SOCK_STREAM)
    serversocket.bind((HOST,PORT))
    serversocket.listen(5)

    print('server start at: %s:%s' % (HOST, PORT))
    print('wait for connection...')

    while True:
        conn , addr = serversocket.accept()
        print('connected by ' + str(addr))

        recvdata = conn.recv(1024)
        print('recv: ' + recvdata.decode())

        senddata = 'echo ' + recvdata.decode()
        conn.send(senddata.encode())
        conn.close()



def main():
    if(str(sys.argv[1])=='-c'):
        client = FTimer_Client(str(sys.argv[3]),int(str(sys.argv[5])))
        #clientmode(str(sys.argv[3]),int(str(sys.argv[5])),int(str(sys.argv[7])))
        client.daemon = True
        client.start()
        time.sleep(int(str(sys.argv[7])))
        client.terminate()
        
    elif(str(sys.argv[1])=='-s'):
        servermode(int(str(sys.argv[3])))
    else:
        print("Error Mode!")

if __name__ == '__main__':
    main()
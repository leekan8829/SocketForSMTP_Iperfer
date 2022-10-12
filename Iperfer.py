from socket import *
import time
import sys

def clientmode(HOST,PORT,TIME):
    #if port is not in range then return
    if(PORT>65535 or PORT<1024):
        print("Error: port number must be in the range 1024 to 65535")
        return 


    buffer = 1000
    senddata = b'0' * buffer

    #open socket
    clientsocket = socket(AF_INET,SOCK_STREAM)
    clientsocket.connect((HOST,PORT))

    now_time = time.time()
    pkgcount = 0

    while(time.time()-now_time<TIME):
        clientsocket.send(senddata)
        pkgcount = pkgcount + 1

    #close socket
    clientsocket.close()

    totalBytes = pkgcount * buffer
    bandwidth = totalBytes/1000/1000*8/TIME
    totalBytes = totalBytes /1000
    if (totalBytes>10000):
        totalBytes=totalBytes/1000
        print("sent=" + str(totalBytes) + "MB" + " rate=" + str(round(bandwidth, 3)) + " Mbps")
        return
    else:
        print("sent=" + str(totalBytes) + "KB" + " rate=" + str(round(bandwidth, 3)) + " Mbps")
        return

def servermode(PORT):
    if(PORT>65535 or PORT<1024):
        print("Error: port number must be in the range 1024 to 65535")
        return 
    
    HOST = '0.0.0.0'

    serversocket = socket(AF_INET,SOCK_STREAM)
    serversocket.bind((HOST,PORT))
    serversocket.listen(5)

    print('server start at: %s:%s' % (HOST, PORT))
    print('wait for connection...')

    while True:
        conn , addr = serversocket.accept()
        start = time.time()
        pkgcount = 0

        while True:
            recvdata = conn.recv(1000)
            if recvdata:
                pkgcount = pkgcount + len(recvdata)
                del recvdata
                continue      
            conn.close()
            end = time.time()

            exeTime = end - start 
            bandwidth = pkgcount / 1000 / 1000 * 8 /exeTime
            pkgcount = pkgcount /1000
            if (pkgcount>10000):
                pkgcount=pkgcount/1000
                print("sent=" + str(pkgcount) + "MB" + " rate=" + str(round(bandwidth, 3)) + " Mbps")
                break
            else:
                print("sent=" + str(pkgcount) + "KB" + " rate=" + str(round(bandwidth, 3)) + " Mbps")
                break
    
        serversocket.close()
        
        return

def main():
    arg_dict = {}

    for index, arg in enumerate(sys.argv):
        try:
            if arg == "-c":
                arg_dict["mode"] = "client"
            elif arg == "-s":
                arg_dict["mode"] = "server"
            elif arg == "-h":
                arg_dict["host"] = sys.argv[index + 1]
            elif arg == "-p":
                port = int(sys.argv[index + 1])
                arg_dict["port"] = port
            elif arg == "-t":
                arg_dict["time"] = float(sys.argv[index + 1])
        except:
            print("Error: missing or additional arguments")
            return

    if( "mode" in arg_dict):
        if arg_dict["mode"] == "client":
            if ("host" not in arg_dict) or ("port" not in arg_dict) or ("time" not in arg_dict):
                print("Error: missing or additional arguments")
                return
            clientmode(arg_dict["host"],arg_dict["port"],arg_dict["time"])
        elif arg_dict["mode"] == "server":
            if ("port" not in arg_dict) or (len(sys.argv) != 4):
                print("Error: missing or additional arguments")
                return
            servermode(arg_dict["port"])
    else:
        print("Error: missing or additional arguments")
        return


if __name__ == '__main__':
    main()
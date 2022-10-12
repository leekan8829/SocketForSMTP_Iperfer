from socket import *
import time

endmsg = "\r\n.\r\n"

mailserver = ("mail.ntust.edu.tw",25)
mailserver = ("smtp.mailtrap.io",2525)
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)

'''
encode(): str->bytes

decode(): bytes->str(default:utf-8)
'''
recv = recv.decode() 

print("Message after connection request:"+recv)

if recv[:3] != '220':
    print("220 reply not received from server.")
else:
    print("220 mail.ntust.edu.tw")


helocommand = "EHLO Kan\r\n"
# helocommand = input("input msg")
clientSocket.send(helocommand.encode())

recv = clientSocket.recv(1024)
recv = recv.decode()

if recv[:3] != '250':
    print("250 reply not received from server.")
else:
    print(recv)

AUTHCommand = "AUTH LOGIN\r\n"
clientSocket.send(AUTHCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)

AUTHCommand = "MzhmZTcyNjJlOTNlY2M=\r\n"
clientSocket.send(AUTHCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)

AUTHCommand = "YzcxMWNhMWRkMWQ0NWI=\r\n"
clientSocket.send(AUTHCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)

print("Send")
#fromCommand = "MAIL FROM:<kan@mail.ntust.edu.tw>\r\n"
fromCommand = "MAIL FROM:<to@example.com>\r\n"
clientSocket.send(fromCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)

print("RCPT")
#toCommand = "RCPT TO:<M11115057@mail.ntust.edu.tw>\r\n"
toCommand = "RCPT TO:<to@example.com>\r\n"
clientSocket.send(toCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)

print("DATA")
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)


msg = "To: to@example.com \r\n"
clientSocket.send(msg.encode())

msg = "From: from@example.com \r\n"
clientSocket.send(msg.encode())

msg = "Subject: Hello world!\r\n"
clientSocket.send(msg.encode())

clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)

quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)

clientSocket.close()

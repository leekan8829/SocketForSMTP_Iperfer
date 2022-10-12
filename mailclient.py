from socket import *
import time

'''
This is Iperfer by python
'''


endmsg = "\r\n.\r\n"

mailserver_name = str(input("smtp server name: "))
mailserver_port = int(input("smtp server port: "))
mailserver = (mailserver_name,mailserver_port)

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


#helocommand = "EHLO Kan\r\n"
helocommand = input("input command: ")
clientSocket.send(helocommand.encode())
helocommand = "\r\n"
clientSocket.send(helocommand.encode())

recv = clientSocket.recv(1024)
recv = recv.decode()

if recv[:3] != '250':
    print("250 reply not received from server.")
else:
    print(recv)


#input MAIL From 
fromMail = str(input("MAIL FROM: "))
fromCommand = "MAIL FROM:<"+fromMail+">\r\n"
clientSocket.send(fromCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)

#input MAIL TO 
toMail = str(input("RCPT TO: "))
toCommand = "RCPT TO:<"+toMail+">\r\n"
clientSocket.send(toCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)

#SEND DATA!
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)


msg = "To: "+toMail+" \r\n"
clientSocket.send(msg.encode())

msg = "From: "+fromMail+" \r\n"
clientSocket.send(msg.encode())

#input Mail sbject
subject = str(input("Subject: "))
msg = "Subject: "+subject+"\r\n"
clientSocket.send(msg.encode())

#input Mail content
content = str(input("Content: "))
msg = "\r\n " + content + "\r\n"
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
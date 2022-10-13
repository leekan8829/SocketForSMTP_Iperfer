# SMTP_Client and Iperfer
- SMTP_Client
- Iperfer

# SMTP_Client
## 執行程式
### 在windows or Linux command line中輸入:
    python3 mailclient.py
即可執行,在執行過程中會有輸入提示

### 功能
可輸入MailSever Name以及MailSever Port之後即可發送EHLO/MAILF ROM/RCP TO/DATA等等指令
### 執行中時:
    1.輸入 mailserver name
    2.輸入 mailserver port
    3. connect成功的話會顯示 220 severname
    4.輸入:EHLO "隨便文字不包含雙引號"
    5.成功的話伺服器會回傳 250 msg
    6.輸入寄送者地址:from@example.com
    7.輸入收件者地址:to@example.com
    8.輸入指令:DATA
    9.----可以開始輸入訊息----
    10.輸入信件主旨:This is test Mail.
    11.輸入信件內容:This is test content.
    12.寄送信件
    13.END
    
## MailServer
    目前測試過可以用的mail server有:
    Mailtrap: https://mailtrap.io/
    但這個Mail需要額外用Authlogin方式登入,作業版本所附上的我並沒有支援Authlogin.
    
# Iperfer
## 功能:
- 可用來測試client和server間的網路傳送頻寬
- 指令輸入錯誤會有提示
## Mode:
**There are two mode in this program**
### 1.client_mode
#### 功能說明
***client mode 可以設定所要連接server的HOST,PORT,以及規定要在多少秒內持續傳送封包,在傳送結束後會顯示他傳了多大SIZE的封包以及他的bandwidth.***
- SERVER_HOST預設為 0.0.0.0
- SERVER_PORT必須在1024<PORT<65535這個範圍,否則會顯示錯誤

#### 執行指令為:
    python3 Iperfer.py -c -h hostip -p portnumber -t time

### 2.server_mode
#### 功能說明
***server mode 可以設定所要開啟的Server Port,接著會開始接收封包到在socket傳送完封包後,會顯示他接收了多大SIZE的封包以及他的bandwidth.***
- SERVER_PORT必須在1024<PORT<65535這個範圍,否則會顯示錯誤

#### 執行指令為:
    python3 Iperfer.py -s -p portnumber
    

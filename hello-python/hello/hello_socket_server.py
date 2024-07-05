#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import thread

s = socket.socket()

host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口
s.listen(5)   # 等待客户端连接

clients = {}


def recive(c):
    try:
        while True:
            msg = c.recv(1024)
            if msg.startswith("###"):
                clients[c]=msg.replace("###","").strip()
            else:
                send(msg,c)
    except :
        print "c down。。。"
        clients.pop(c)

def send(msg,client):
    for c in clients:
#         if c == client:
#             continue
        c.send(clients[client]+":::"+msg)
    
while True:
    c, addr = s.accept()     # 建立客户端连接。
    print '连接地址：', addr
    try:
        thread.start_new_thread(recive,(c,))
    except BaseException, e:
        print e
        print "Error: unable to start thread"
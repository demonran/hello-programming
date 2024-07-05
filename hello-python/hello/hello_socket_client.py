#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket  # 导入 socket 模块




class Client:
    def __init__(self,username):
        self.s = socket.socket()         # 创建 socket 对象
        host = socket.gethostname() # 获取本地主机名
        port = 12345   
        self.s.connect((host, port))             # 设置端口好
        self.send("###"+username)
        
    #接收消息
    def receive(self):
        return self.s.recv(1024)
        
    def send(self,msg):
        self.s.send(msg)
    
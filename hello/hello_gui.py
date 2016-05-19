#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkconstants import RIGHT, END, LEFT, SEL_LAST
from Tkinter import Entry, Label, Frame
import Tkinter
import thread
import time

from hello_socket_client import Client


root = Tkinter.Tk()
registPanel = None
send_text = None
rec_text = None
entry =None

client = None

def send_msg():
    
    msg = send_text.get("1.0",END)
    send_text.delete("1.0",END)
    client.send(msg.encode(encoding='UTF-8'))

def recieve(client):
    while True:
        rec_msg_text = client.receive()
        t = rec_msg_text.partition(":::")
        rec_text.insert(END, t[0] +"\t" 
                        +time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +'\n'
                        +t[2]+"\n")
        

    
def go_main():
    global client
    
    username = entry.get().encode(encoding='UTF-8')
   
    registPanel.destroy()
    
    client = Client(username)
    thread.start_new_thread(recieve,(client,))
   
    root.title(username)
    mainPanel()
    
    

def regist():
    global registPanel
    global entry
    
    
    registPanel = Frame(root)
    label = Label(registPanel,text="请输入用户名：")
    entry =Entry(registPanel)
    confirm_btn = Tkinter.Button(registPanel,text="确认",fg="Blue",command=go_main)
    registPanel.pack()
    label.pack();
    entry.pack(side=LEFT)
    confirm_btn.pack(side = RIGHT)
  
    
def mainPanel():
    
    global send_text
    global rec_text
    
    # 接受消息
    rec_text = Tkinter.Text(root, foreground="blue")

    send_text = Tkinter.Text(root,background="green", foreground="blue",height=3)

    send_btn = Tkinter.Button(root,text="发送",fg="Blue",command=send_msg)
    send_btn._name="发送"
    
    
#     rec_text.tag_add("here", "*.0", SEL_LAST)
#     rec_text.tag_add("start", "1.8", "1.13")
#     rec_text.tag_config("here", background="yellow", foreground="blue")
#     rec_text.tag_config("start", background="black", foreground="green")

    rec_text.pack()
    send_text.pack()
    send_btn.pack(side = RIGHT)
    

regist()

    # 进入消息循环
root.mainloop()

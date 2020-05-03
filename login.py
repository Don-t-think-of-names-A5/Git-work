# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:52:17 2019

@author: KanQingbo
"""

from tkinter import *
from tkinter.messagebox import *
from sign_up import *
from home_windows import *
def login_window():
    import tkinter
    import tkinter as tk
    import os
    import os.path
    import sqlite3
    
    root=tkinter.Tk()
    #root=tkinter.Toplevel()
    img = os.getcwd() + '\\images'
    dat = os.getcwd() + '\\data'
    root.title('English-Study-System-登陆界面') 
    root.geometry('600x400+600+300') 
    root.resizable(False,False)
    photo=tkinter.PhotoImage(file=img + "\\login.png")
    label=tkinter.Label(root,image=photo)  #图片
    label.pack()
    def yanzheng():
        username = entry1.get()
        password = entry2.get()
        #print(username,password)
        cn=sqlite3.connect('English_study_system.db')
        cur=cn.cursor()
        n = cur.execute('select * from user')
        a = n.fetchall()
        c = 0
        d = 0
        for i in a:
            if i[0] == username:
                c = 1
                if i[1] == password:
                    d = 1
                break
        if username == "" or password == "":
            tkinter.messagebox.showerror('Error', '您好像忘了输入什么东西!')
        elif c == 0:
            tkinter.messagebox.showerror('Error', '该用户名尚未注册!')
        elif c == 1 and d == 0:
            tkinter.messagebox.showerror('Error', '您输入的账号和密码不匹配!')
        else:
            tkinter.messagebox.showinfo('Welcome', '您已登陆成功!')
            user = str(username)
            with open(dat +'\\username.txt', 'w',encoding='utf-8') as file:
                file.write(user)
            root.destroy()
            home_windows()
    button1 = tkinter.Button(root,text='登陆',bg = 'lightcyan',fg = 'green',activebackground = 'orange', command=yanzheng)
    button1.place(x=120, y=280, width=160, height=35)

    button2 = tkinter.Button(root,text='注册',bg = 'wheat',fg = 'red',activebackground = 'red', command=usr_sign_up)
    button2.place(x=320, y=280, width=160, height=35)

    lb1 = tkinter.Label(root,text="用户：",fg = 'indigo', bg = 'white')
    lb1.place(x = 180, y = 135, width = 50, height = 35)

    with open('data/username.txt', 'r', encoding='utf-8') as file:
            a = file.read()
    name = tk.StringVar()
    entry1 = tkinter.Entry(root,width=200, bd = 0, bg = 'white', textvariable=name)
    entry1.insert(0,str(a))
    entry1.place(x = 230, y=135,width=200,height=35)

 
    lb2 = tkinter.Label(root,text="密码：",fg = 'indigo', bg = 'white')
    lb2.place(x = 180, y = 180, width = 50, height = 35)
    
    entry2 = tkinter.Entry(root,width=200, bd = 0, bg = 'white', show='*')
    
            
    entry2.place(x = 230,y = 180,width=200,height = 35)


    cn=sqlite3.connect('English_study_system.db')
    cur=cn.cursor()
    #showinfo("logo","数据库连接成功,单击确定继续操作")
    try:
        cur.execute('create table user(username char(16)PRIMARY key, password char (16))')
        #showinfo("logo","数据表创建成功")
    except:
            #showinfo("logo","现在可以开始报名")
            p = 1

    cn.close()
    root.mainloop()

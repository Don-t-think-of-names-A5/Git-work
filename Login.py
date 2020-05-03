'''
大作业
大学英语学习系统
创建时间：19-12-9
'''
import tkinter
#import tkinter.messagebox
#import tkinter.simpledialog
#import tkinter.colorchooser
from tkinter import *
from tkinter.messagebox import *
from MainPage import * 

#连接数据库
import sqlite3
cn = sqlite3.connect('data//EnStudy.db') #若没有数据库会自动创建
cur=cn.cursor() 

#showinfo("Connect","数据库连接成功,单击确定继续操作")

'''
登陆界面
'''
def LoginPage():
    #如果没有数据库的时候进行初始化
    cur.execute("create table IF NOT EXISTS user ('Name' char(20) PRIMARY KEY,'Password' char(16))")
    n = cur.execute("select * from user")
    a = n.fetchall()
    flag = 0
    for i in a :
        if (i[0] == "Admin"):
            flag = 1
    if flag == 0:
        cur.execute("insert into user VALUES('Admin','admin')")
        cur.execute('create table En_Admin_words ("English" char(50) PRIMARY KEY,"Types" char(50), "Chinese" char(50), "SearchCount" int(1000))')
        cur.execute("insert into En_Admin_words VALUES('test','n.名词','测试','1')")
        cn.commit()
    #登陆子函数
    def login():
        if nameEntry.get() == "" or pwEntry.get() == "":
            showwarning(title="不能为空", message="输入不能为空！")
            return
        elif " " in nameEntry.get() or " " in pwEntry.get():
            showwarning(title="No Space", message="输入不能含有空格！")
            return
        import sqlite3
        cn = sqlite3.connect('data//EnStudy.db')
        cur=cn.cursor()
        b = list()
        user = nameEntry.get()
        b.append(user)
        user = pwEntry.get()
        b.append(user)
        n = cur.execute('select * from user')
        a = n.fetchall()
        flag1=0
        flag2=0
        for i in a:
            if i[0]==b[0] and i[1]==b[1]:
                flag1=1
                flag2=1
                break
            elif i[0]==b[0] and i[1]!=b[1]:
                flag1=1
                #flag2=0
                break
        if flag1==1 and flag2==1:
            showinfo("登录成功","登录成功！\n开始尽情的学习吧！")
            with open("data//user.txt",'w+', encoding='utf-8')as f:
                f.write(b[0])
            root.destroy()
            MainPage()
        else:
            if flag1==0:
                showwarning("登录失败","您还未加入我们的学习哦！")
                return
            elif flag1==1 and flag2==0:
                showwarning("登陆失败","忘记密码啦，再好好想想！")
                return
    #注册子函数
    def register():
        if nameEntry.get() == "" or pwEntry.get() == "":
            showwarning(title="不能为空", message="请您输入账号密码后注册！")
            return
        elif " " in nameEntry.get() or " " in pwEntry.get():
            showwarning(title="No Space", message="输入不能含有空格！")
            return
        import sqlite3
        cn = sqlite3.connect('data//EnStudy.db')
        cur=cn.cursor()
        b = list()
        user = nameEntry.get()
        b.append(user)
        user = pwEntry.get()
        b.append(user)
        n = cur.execute('select * from user')
        a = n.fetchall()
        flag=0
        for i in a:
            if i[0]==b[0]:
                flag=1
                break
        if flag==1:
            showwarning("注册失败","这里有人和你想一块咯（账号已存在）！")
            return
        else:
            confirm=askyesno(title="确定密码",message="确定使用该密码吗？\n密码为：%s"%b[1])
            print(confirm)
            if(confirm):
                n=cur.execute('insert into user VALUES (?,?)', b)
                showinfo("注册成功","注册成功，欢迎加入学习！")
                sss = "En_" + b[0] + "_words"
                cn.execute('create table '+ sss + '("English" char(50) PRIMARY KEY,"Types" char(50), "Chinese" char(50), "SearchCount" int(1000))')
                cn.commit()
                cn.close()
            else:
                pwEntry.delete(0,END)
    
    root=tkinter.Tk()
    #root=tkinter.Toplevel()
    
    #窗口标题
    root.title('大学英语学习系统--Login')
    #窗口初始大小和位置
    root.geometry('400x300+800+300')
    #不允许改变窗口大小
    root.resizable(False,False)
    
    #图片显示
    welcome = tkinter.PhotoImage(file="data//welcome.png")
    labelt = tkinter.Label(root, image = welcome)
    labelt.pack()
    
    #输入框
    name=tkinter.Label(root,text=" 账号：",bg = 'white')
    nameEntry=tkinter.Entry(root,bd=0,relief = tkinter.GROOVE,exportselection=0)  #justify='center'可以居中显示输入的文字
    name.place(x=90,y=140,height = 30,width=50)
    nameEntry.place(x=140,y=140,height = 30,width=170)
    password=tkinter.Label(root,text=" 密码：",bg = 'white')
    pwEntry=tkinter.Entry(root,bd=0,relief = tkinter.GROOVE,show='*',exportselection=0)
    password.place(x=90,y=180,height = 30,width=50)
    pwEntry.place(x=140,y=180,height = 30,width=170)
    with open("data//user.txt",encoding='utf-8')as f:
        username = f.readline()
    if username != "":
        nameEntry.insert(INSERT,username)
    #登录注册按钮
    #label = tkinter.Label(root, text = '欢迎来到\n大学生英语学习系统', font = ('楷体'))
    #label.place(x = 150, y = 20)
    loginbt=tkinter.Button(root,text='登录',command=login,font=('隶书'),bg='lightsteelblue',relief=tkinter.GROOVE) 
    loginbt.place(x=90,y=230,width = 90, height = 30)
    rebt=tkinter.Button(root,text='注册',command=register,font=('隶书'),bg='lightsteelblue',relief=tkinter.GROOVE) 
    rebt.place(x=220,y=230,width=90,height=30)
    
    #循环显示窗口
    root.mainloop()


import tkinter
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from sign_up import *

def usr_sign_up():
    def sign_to_Hongwei_Website():
        
        # 以下三行就是获取我们注册时所输入的信息
        np = entry_usr_pwd.get()
        npf = entry_usr_pwd_confirm.get()
        nn = entry_new_name.get()
        # 这里是打开我们数据库，将注册信息读出
        import sqlite3
        cn = sqlite3.connect('English_study_system.db')
        cur=cn.cursor()
        n = cur.execute('select * from user')
        a = n.fetchall()
        c = 0
        
        # 这里就是判断，如果两次密码输入不一致，则提示Error, Password and confirm password must be the same!
        if np != npf:
            tkinter.messagebox.showerror('Error', '两次输入的密码不一致!')
 
        # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
        elif nn == "" or np == "" or npf == "":
            tkinter.messagebox.showerror('Error', '您好像忘了输入什么东西!')
        else:
            for i in a:
                if i[0] == nn:
                    c = 1
                    break
            if c == 1:    
                tkinter.messagebox.showerror('Error', '该用户名已被使用!')
 
        #最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
            else:
                b = []
                b.append(nn)
                b.append(np)
                n = cur.execute('insert into user VALUES (?,?)', b)
                cn.commit()
                cn.close()
                tkinter.messagebox.showinfo('Welcome', '您已注册成功!')
                # 然后销毁窗口。
                window_sign_up.destroy()
 
    # 定义长在窗口上的窗口
    
    window_sign_up = tk.Tk()
    window_sign_up.geometry('300x200+750+400')
    window_sign_up.title('System-注册界面')
    
    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(window_sign_up, text='用户名: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.
 
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='请输入密码: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=130, y=50)
 
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='再次输入密码').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=130, y=90)
    
    # 下面的 sign_to_Hongwei_Website
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='注册', command=sign_to_Hongwei_Website)
    btn_comfirm_sign_up.place(x=180, y=120)
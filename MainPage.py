# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:03:15 2019

@author: WMY
"""

import tkinter
import xlrd
from tkinter import *
from tkinter import Tk, filedialog
from view import * #菜单栏对应的各个子页面 
import Login
'''
导入excel表格
'''
def openfile():#打开对话窗口，选择文件，导入单词表
    root = Tk()
    root.withdraw()
    def import_words():
        print(str(c[0]))
        xls = xlrd.open_workbook(str(c[0]))  #获取到表格
        table = xls.sheets()[0] #获取表格的第一个sheet
        data = list()  # 准备将所有数据存入列表
        n = table.nrows  # 得到数据行数
        import sqlite3
        cn = sqlite3.connect("data//EnStudy.db")
        cur = cn.cursor()
        with open("data//user.txt",encoding='utf-8')as f:
                username = f.readline()
        sss = "En_" + username + "_words"
        print(sss)
        #cn.execute("DROP TABLE IF EXISTS " + sss)  #删除旧的用户单词表
        #cn.execute('create table '+ sss + '("English" char(50) PRIMARY KEY,"Types" char(50), "Chinese" char(50), "SearchCount" int(1000))')
        for i in range(1, n):
            data = table.row_values(i)  #一行中的四个数据
            print(data)
            if len((cur.execute("select * from " + sss + " where English = '"+str(data[0])+"'")).fetchall()) == 0 :
                cur.execute("insert into " + sss + " VALUES (?,?,?,?)", data)
        cn.commit()
        cn.close()
    c = filedialog.askopenfilenames(filetypes=[('xlsx', '*.xlsx'),('xls', '*.xls')]) #打开文件
    if len(c) == 0:
        print('你没有选择任何文件')
    else:
        print(c)
        confirm = askyesno(title="确定?",message="导入将跳过已存在的单词，确定吗？")
        if confirm:
            import_words()
        else:
            showinfo("取消操作","您已取消操作。")
    root.destroy()

import xlwt
from xlwt import *
import xlsxwriter

"""
导出excel表格
"""
def savefile():
    def write_in():
        if nameE1.get() == "" :
            showwarning("错误","空文件不能导出哦！")
            return
        import sqlite3
        cn = sqlite3.connect("data//EnStudy.db")
        cur = cn.cursor()
        with open("data//user.txt",encoding='utf-8')as f:
                username = f.readline()
        sss = "En_" + username + "_words"
        n = cur.execute('select * from ' + sss)
        All = n.fetchall()
        workbook = xlwt.Workbook()  # 新建一个工作簿
        sheet = workbook.add_sheet("WordsSheet")  # 在工作簿中新建一个表格
        index = len(All)  #获取有多少行数据
        sheet.write(0, 0, "English")  #这四行为给表格第一行加入属性名
        sheet.write(0, 1, "Types")
        sheet.write(0, 2, "Chinese")
        sheet.write(0, 3, "SearchCount")
        for i in range(0, index):  #从第一行遍历到最后一行
            for j in range(0, len(All[i])):
                sheet.write(i+1, j, All[i][j])  # 像表格中写入数据（对应的行和列）
        workbook.save(nameE1.get()+".xls")  # 保存工作簿并以输入的信息命名
        print("xls格式表格写入数据成功！")
        showinfo("成功","导出成功！")
        temp.destroy()
    temp = Tk()
    temp.title('导出表格')
    temp.geometry("300x200+400+300") #设置窗口大小 
    temp.resizable(False,False)
    title1=tkinter.Label(temp,text="请输入要备份的表格名字：",font=('隶书', 14))
    nameE1=tkinter.Entry(temp,text="单词备份",bg = 'white')
    nameE1.insert(INSERT,"单词备份")
    name1=tkinter.Label(temp,text=".xls")
    title1.place(x = 30, y = 30)
    nameE1.place(x=50,y=80,height = 30,width=150)
    name1.place(x=200,y=80,height = 30,width=30)
    Button(temp, text = '确定',command=write_in,font = ("隶书",14),relief=tkinter.GROOVE).place(x = 100,y = 130)
    temp.mainloop()
'''
主窗口
'''
def MainPage():
    root = Tk()
    root.title('大学英语学习系统')
    root.geometry("1000x700+500+200") #设置窗口大小 
    root.resizable(False,True)
    inputPage = InputFrame() # 创建不同Frame，添加界面类 
    searchPage = SearchFrame()  #查询界面类
    aboutPage = AboutFrame()  #关于界面类
    homePage = HomeFrame() #欢迎主界面类
    with open("data//user.txt",encoding='utf-8')as f:
        username = f.readline()
    Label(root, text = "欢迎您：",font=('隶书', 14)).place(x = 800, y = 10)
    Label(root, text = username,font=('隶书', 14)).place(x = 870, y = 10)
    homePage.pack() #默认显示欢迎主界面
    def inputData():  #用函数控制哪些界面显示与不显示，并绑定在menubar的不同按钮上
        inputPage.pack() 
        searchPage.pack_forget() 
        aboutPage.pack_forget() 
        homePage.pack_forget()
  
    def searchData(): 
        inputPage.pack_forget() 
        searchPage.pack() 
        aboutPage.pack_forget() 
        homePage.pack_forget()
  
    def aboutDisp(): 
        inputPage.pack_forget() 
        searchPage.pack_forget() 
        aboutPage.pack() 
        homePage.pack_forget()
    
    def home():
        inputPage.pack_forget() 
        searchPage.pack_forget() 
        aboutPage.pack_forget() 
        homePage.pack()
        
    def logout():
        root.destroy()
        Login.LoginPage()
    
    #修改密码窗口和函数
    def changepw(): 
        window = tkinter.Tk()
        window.title('修改密码')
        window.geometry('400x300+300+100')
        window.resizable(False,False)
        tkinter.Label(window,text="修改密码",font=('隶书')).place(x=150,y=40)
        name=tkinter.Label(window,text="账号：",bg = 'white')
        nameE=tkinter.Label(window,text=username,bg = 'white')
        name.place(x=70,y=100,height = 30,width=100)
        nameE.place(x=160,y=100,height = 30,width=200)
        password1=tkinter.Label(window,text="请输入密码：",bg = 'white')
        pwEntry1=tkinter.Entry(window,bd=0,relief = tkinter.GROOVE,show='*',justify='center',exportselection=0)
        password1.place(x=70,y=140,height = 30,width=100)
        pwEntry1.place(x=160,y=140,height = 30,width=200)
        password2=tkinter.Label(window,text="请再次输入密码：",bg = 'white')
        pwEntry2=tkinter.Entry(window,bd=0,relief = tkinter.GROOVE,show='*',justify='center',exportselection=0)
        password2.place(x=70,y=180,height = 30,width=100)
        pwEntry2.place(x=160,y=180,height = 30,width=200)
        def change_sqlpwd():
            if pwEntry1.get() == "" or pwEntry2.get() == "":
                showwarning(title="不能为空", message="请您输入密码后修改！")
                return
            elif " " in pwEntry1.get() or " " in pwEntry2.get():
                showwarning(title="No Space", message="输入不能含有空格！")
                return
            elif pwEntry1.get() != pwEntry2.get():
                showwarning(title="不一致", message="两次输入密码不一致！")
                return
            import sqlite3
            cn = sqlite3.connect('data//EnStudy.db')
            cur=cn.cursor()
            b = list()
            b.append(pwEntry1.get())
            b.append(username)
            n=cur.execute('update user set Password = ? where Name = ?', b)
            cn.commit()
            cn.close()
            showinfo(title="成功", message="密码修改成功！")
            window.destroy()
        Button(window, text='确定', font = "楷体", command=change_sqlpwd).place(x=170,y=220) 
#    删库函数
#    def removeData():
#        with open("data//user.txt",encoding='utf-8')as f:
#            username = f.readline()
#        if (username != "Admin"):
#            showwarning("错误","您并非管理员，不能删除数据库！\n请联系Admin。")
#        else:
#            if(askyesno("确定吗","这将清空所有数据，此操作无法撤回！")):
#                import os
#                import sqlite3
#                cn = sqlite3.connect('EnStudy.db')
#                cn.close()
#                showwarning("删除成功","注意：数据库已删除！\n系统即将退出，点击确定退出系统。\n期待您的下次使用！")
#                root.destroy()
#                os.remove("data//user.txt")
#                os.remove("data//EnStudy.db")
    menubar = Menu(root)
    menubar.add_cascade(label="主界面",command=home,font=('隶书', 10))
    menubar.add_cascade(label="导入单词表",command=openfile,font=('隶书', 10))
    menubar.add_cascade(label="导出单词表",command=savefile,font=('隶书', 10))
    menubar.add_cascade(label="添加单词",command=inputData,font=('隶书', 10))
    menubar.add_cascade(label="查询所有单词",command=searchData,font=('隶书', 10))
    usermenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="用户",menu=usermenu,font=('隶书', 10))
    usermenu.add_command(label="修改密码",command=changepw,font=('隶书', 15))
    usermenu.add_command(label="退出登录",command=logout,font=('隶书', 15))
    #usermenu.add_command(label="删除数据库",command=removeData,font=('隶书', 15))
    menubar.add_cascade(label="关于",command=aboutDisp,font=('隶书', 10))
    menubar.add_cascade(label="退出系统",command=root.destroy,font=('隶书', 10))
    root.config(menu=menubar)  # 显示菜单
    

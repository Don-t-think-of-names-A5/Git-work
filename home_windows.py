import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from tkinter.messagebox import *
import login
import re
import os
import os.path
def home_windows():
    import sqlite3
    import tkinter as tk  # 使用Tkinter前需要先导入
    import tkinter.messagebox
    import pickle
    import os
    import os.path
    img = os.getcwd() + '\\images'
    print(img)
    home_window = tk.Tk()
    home_window.geometry('1280x720+300+150')
    home_window.title('English-Study-System-主界面')
    home_window.resizable(False,False)
    
    
    def login1():
        home_window.destroy()
        login.login_window()
    def password_change():
        def sign_to_Hongwei_Website():
            # 以下三行就是获取我们注册时所输入的信息
            np = entry_usr_pwd.get()
            npf = entry_usr_pwd_confirm.get()
            nn = entry_new_name.get()
            # 这里是打开我们数据库，将注册信息读出
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
                window_sign_up.destroy()
            else:
                for i in a:
                    if i[0] == nn:
                        c = 1
                        break
                if c == 0:    
                    tkinter.messagebox.showerror('Error', '该用户尚未注册，不可修改密码!')
 
        #最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
                else:
                    b = []
                    b.append(np)
                    b.append(nn)
                    n = cur.execute('update user set password = ? where username = ?', b)
                    cn.commit()
                    cn.close()
                    tkinter.messagebox.showinfo('Accept', '您的密码已修改成功!')
                    # 然后销毁窗口。
                    window_sign_up.destroy()
        window_sign_up = tk.Tk()
        window_sign_up.geometry('300x200+760+200')
        window_sign_up.title('System-修改密码')
        with open('data/username.txt', 'r', encoding='utf-8') as file:
            a = file.read()
        name = tk.StringVar()
        tk.Label(window_sign_up, text='用户名: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
        entry_new_name = tk.Entry(window_sign_up, textvariable=name)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_new_name.insert(0,str(a))
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
        btn_comfirm_sign_up = tk.Button(window_sign_up, text='修改', command=sign_to_Hongwei_Website)
        btn_comfirm_sign_up.place(x=180, y=120)
    def display():
        window_sign_up = tk.Tk()
        window_sign_up.geometry('720x360+580+200')
        window_sign_up.title('查看单词表')
        window_sign_up.resizable(False,False)
        cn=sqlite3.connect('English_study_system.db')
        cur=cn.cursor()
        #showinfo("logo","数据库连接成功,单击确定继续操作")
        try:
            cur.execute('create table word_table(words char(16), sex char(16), chinese char(16), count int(100), realise char(3),primary key(words,sex))')
            showinfo("logo","数据表创建成功")
        except:
            p = 1
        cn.close()
        columns = ("单词","词性","解释","查询次数","生词")
        table=ttk.Treeview(window_sign_up, show = 'headings', columns = columns)#表格
        table.column("单词",width=100,anchor='center')
        table.column("词性",width=100,anchor='center')
        table.column("解释",width=100,anchor='center')
        table.column("查询次数",width=100,anchor='center')
        table.column("生词",width=100,anchor='center')
        
        table.heading("单词",text="单词-word")  #显示表头
        table.heading("词性",text="词性-sex") 
        table.heading("解释",text="汉语-chinese") 
        table.heading("查询次数",text="查询次数-count") 
        table.heading("生词",text="生词-strange")
        cn = sqlite3.connect('English_study_system.db')
        cur=cn.cursor()
        n = cur.execute('select * from word_table')
        a = n.fetchall()
        t = 0
        for i in a:
            t+=1
            table.insert("",t,values=(i[0],i[1],i[2],i[3],i[4]))
        table.place(x = 4, y = 4, width = 710, height = 350)
    def add_words():
        def sex_option1():
            n2 = 'n.名词'
            n1 = word_entry.get()
            n3 = chinese_entry.get()
            if n2 == "" or n3 == "":    
                tkinter.messagebox.showerror('Error', '您好像忘了输入什么东西!')
            else:
                 cn = sqlite3.connect('English_study_system.db')
                 cur=cn.cursor()
                 d = []
                 d.append(n1)
                 d.append(n2)
                 d.append(n3)
                 d.append(0)
                 d.append('no')
                 n = cur.execute('insert into word_table VALUES (?,?,?,?,?)', d)
                 cn.commit()
                 cn.close()
                 if tkinter.messagebox.askyesno('Accept','添加单词成功'):
                     window_add.destroy()
                     add_words()
                 else:
                     window_add.destroy()
        def sex_option2():
            n2 = 'v.动词'
            n1 = word_entry.get()
            n3 = chinese_entry.get()
            if n2 == "" or n3 == "":    
                tkinter.messagebox.showerror('Error', '您好像忘了输入什么东西!')
            else:
                 cn = sqlite3.connect('English_study_system.db')
                 cur=cn.cursor()
                 d = []
                 d.append(n1)
                 d.append(n2)
                 d.append(n3)
                 d.append(0)
                 d.append('no')
                 n = cur.execute('insert into word_table VALUES (?,?,?,?,?)', d)
                 cn.commit()
                 cn.close()
                 if tkinter.messagebox.askyesno('Accept','添加单词成功'):
                     window_add.destroy()
                     add_words()
                 else:
                     window_add.destroy()
        def sex_option3():
            n2 = 'adj.形容词'
            n1 = word_entry.get()
            n3 = chinese_entry.get()
            if n2 == "" or n3 == "":    
                tkinter.messagebox.showerror('Error', '您好像忘了输入什么东西!')
            else:
                 cn = sqlite3.connect('English_study_system.db')
                 cur=cn.cursor()
                 d = []
                 d.append(n1)
                 d.append(n2)
                 d.append(n3)
                 d.append(0)
                 d.append('no')
                 n = cur.execute('insert into word_table VALUES (?,?,?,?,?)', d)
                 cn.commit()
                 cn.close()
                 if tkinter.messagebox.askyesno('Accept','添加单词成功'):
                     window_add.destroy()
                     add_words()
                 else:
                     window_add.destroy()
        def sex_option4():
            n2 = 'adv.副词'
            n1 = word_entry.get()
            n3 = chinese_entry.get()
            if n2 == "" or n3 == "":    
                tkinter.messagebox.showerror('Error', '您好像忘了输入什么东西!')
                window_add.destroy()
            else:
                 cn = sqlite3.connect('English_study_system.db')
                 cur=cn.cursor()
                 d = []
                 d.append(n1)
                 d.append(n2)
                 d.append(n3)
                 d.append(0)
                 d.append('no')
                 n = cur.execute('insert into word_table VALUES (?,?,?,?,?)', d)
                 cn.commit()
                 cn.close()
                 if tkinter.messagebox.askyesno('Accept','添加单词成功'):
                     window_add.destroy()
                     add_words()
                 else:
                     window_add.destroy()
        window_add= tk.Tk()
        window_add.geometry('400x120+750+200')
        window_add.title('添加单词')
        window_add.resizable(False,False)
        word_Label=tk.Label(window_add,text='输入单词：')
        word_Label.place(x = 30, y = 10)
        
        word_entry=tk.Entry(window_add)
        word_entry.place(x = 30, y = 30)
        
        chinese_Label=tk.Label(window_add,text='单词汉语：')
        chinese_Label.place(x = 200, y = 10)
        
        chinese_entry=tk.Entry(window_add)
        chinese_entry.place(x = 200, y = 30)
        
        sex1 = tk.Radiobutton(window_add,text='n.名词',command=sex_option1)                 
        sex1.place(x = 10, y = 70)
        sex2 = tk.Radiobutton(window_add,text='v.动词',command=sex_option2)                 
        sex2.place(x = 200, y = 70)
        sex3 = tk.Radiobutton(window_add,text='adj. 形容词',command=sex_option3)                 
        sex3.place(x = 90, y = 70)
        sex4 = tk.Radiobutton(window_add,text='adv. 副词',command=sex_option4)                 
        sex4.place(x = 280, y = 70)
    def dr_word():
        def dr():
            cn = sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            with open(cc, 'r') as file:
                b = file.read()
            #print(b)
            d = []
            str0 = ""
            str1 = ""
            str2 = ""
            flag = 0
            for i in b:
                if   (i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z') and flag == 0:
                    str0 += i
                elif (i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z') and flag == 1:
                    str1 += i
                elif i != '\t' and i != '\n' and flag == 2:
                    str2 += i
                    #print("str2:",str2)
                elif i == '\t' and flag == 0:
                    d.append(str0)
                    flag = 1
                    #print(d)
                    str0 = ""
                elif i == '\t' and flag == 1:
                    if str1 == "n":
                        sex1 = 'n.名词'
                    elif str1 == 'v':
                        sex1 = 'v.动词'
                    elif str1 == 'adj':
                        sex1 = 'adj.形容词'
                    elif str1 == 'adv':
                        sex1 = 'adv.副词'
                    else:
                        sex1 = ""
                    d.append(sex1)
                    flag = 2
                    #print(d)
                    str1 = ""
                elif i == '\t' or i == '\n' and flag == 2:
                    d.append(str2)
                    flag = 0
                    #print("2:",d)
                    str2 = ""
                    d.append(0)
                    d.append('no')
                    try:
                        n = cur.execute('insert into word_table VALUES (?,?,?,?,?)', d)
                    except:
                        tkinter.messagebox.showerror('Error', '您导入的数据重复，请检查!')
                    d = []
                else:
                    continue
            cn.commit()
            cn.close()
        c = filedialog.askopenfilenames()
        print(c)
        cc = str(c[0])
        dr()
        tkinter.messagebox.showinfo('Accept', '数据已经导入成功!')
    def cx_word():
        def cx1():
            cx11 = e1.get()
            if cx11 == '':
                tkinter.messagebox.showerror('Error', '您好像忘了输入什么东西!')
                window_sign_up.destroy()
                
            cn=sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            #showinfo("logo","数据库连接成功,单击确定继续操作")
            try:
                cur.execute('create table word_table(words char(16), sex char(16), chinese char(16), count int(100), realise char(3),primary key(words,sex))')
                showinfo("logo","数据表创建成功")
            except:
                p = 1
            cn.close()
            columns = ("单词","词性","解释","查询次数","生词")
            table=ttk.Treeview(window_sign_up, show = 'headings', columns = columns)#表格
            table.column("单词",width=100,anchor='center')
            table.column("词性",width=100,anchor='center')
            table.column("解释",width=100,anchor='center')
            table.column("查询次数",width=100,anchor='center')
            table.column("生词",width=100,anchor='center')
        
            table.heading("单词",text="单词-word")  #显示表头
            table.heading("词性",text="词性-sex") 
            table.heading("解释",text="汉语-chinese") 
            table.heading("查询次数",text="查询次数-count") 
            table.heading("生词",text="生词-strange")
            cn = sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            
            n = cur.execute('select * from word_table')
            a = n.fetchall()
            t = 0
            for i in a:
                if(re.search(cx11,i[0])):    
                    t+=1
                    table.insert("",t,values=(i[0],i[1],i[2],i[3],i[4]))
                    n1 = cur.execute("update word_table set count = count+1 where words = '"+i[0]+"'")
                    cn.commit()
            table.place(x = 4, y = 100, width = 710, height = 445)
        def cx2():
            cx11 = e2.get()
            if cx11 == '':
                tkinter.messagebox.showerror('Error', '您好像忘了输入什么东西!')
                window_sign_up.destroy()
            cn=sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            #showinfo("logo","数据库连接成功,单击确定继续操作")
            try:
                cur.execute('create table word_table(words char(16), sex char(16), chinese char(16), count int(100), realise char(3),primary key(words,sex))')
                showinfo("logo","数据表创建成功")
            except:
                p = 1
            cn.close()
            columns = ("单词","词性","解释","查询次数","生词")
            table=ttk.Treeview(window_sign_up, show = 'headings', columns = columns)#表格
            table.column("单词",width=100,anchor='center')
            table.column("词性",width=100,anchor='center')
            table.column("解释",width=100,anchor='center')
            table.column("查询次数",width=100,anchor='center')
            table.column("生词",width=100,anchor='center')
        
            table.heading("单词",text="单词-word")  #显示表头
            table.heading("词性",text="词性-sex") 
            table.heading("解释",text="汉语-chinese") 
            table.heading("查询次数",text="查询次数-count") 
            table.heading("生词",text="生词-strange")
            cn = sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            
            n = cur.execute('select * from word_table')
            a = n.fetchall()
            t = 0
            for i in a:
                if(re.search(cx11,i[2])):
                    t+=1
                    table.insert("",t,values=(i[0],i[1],i[2],i[3],i[4]))
                    n1 = cur.execute("update word_table set count = count+1 where words = '"+i[0]+"'")
                    cn.commit()
            table.place(x = 4, y = 100, width = 710, height = 445)
        def cx3():
            cn=sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            #showinfo("logo","数据库连接成功,单击确定继续操作")
            try:
                cur.execute('create table word_table(words char(16), sex char(16), chinese char(16), count int(100), realise char(3),primary key(words,sex))')
                showinfo("logo","数据表创建成功")
            except:
                p = 1
            cn.close()
            columns = ("单词","词性","解释","查询次数","生词")
            table=ttk.Treeview(window_sign_up, show = 'headings', columns = columns)#表格
            table.column("单词",width=100,anchor='center')
            table.column("词性",width=100,anchor='center')
            table.column("解释",width=100,anchor='center')
            table.column("查询次数",width=100,anchor='center')
            table.column("生词",width=100,anchor='center')
        
            table.heading("单词",text="单词-word")  #显示表头
            table.heading("词性",text="词性-sex") 
            table.heading("解释",text="汉语-chinese") 
            table.heading("查询次数",text="查询次数-count") 
            table.heading("生词",text="生词-strange")
            cn = sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            
            n = cur.execute('select * from word_table')
            a = n.fetchall()
            t = 0
            for i in a:
                if i[4] == 'yes':
                    t+=1
                    table.insert("",t,values=(i[0],i[1],i[2],i[3],i[4]))
                    n1 = cur.execute("update word_table set count = count+1 where words = '"+i[0]+"'")
                    cn.commit()
            table.place(x = 4, y = 100, width = 710, height = 445)
        def cx4():
            cn=sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            #showinfo("logo","数据库连接成功,单击确定继续操作")
            try:
                cur.execute('create table word_table(words char(16), sex char(16), chinese char(16), count int(100), realise char(3),primary key(words,sex))')
                showinfo("logo","数据表创建成功")
            except:
                p = 1
            cn.close()
            columns = ("单词","词性","解释","查询次数","生词")
            table=ttk.Treeview(window_sign_up, show = 'headings', columns = columns)#表格
            table.column("单词",width=100,anchor='center')
            table.column("词性",width=100,anchor='center')
            table.column("解释",width=100,anchor='center')
            table.column("查询次数",width=100,anchor='center')
            table.column("生词",width=100,anchor='center')
        
            table.heading("单词",text="单词-word")  #显示表头
            table.heading("词性",text="词性-sex") 
            table.heading("解释",text="汉语-chinese") 
            table.heading("查询次数",text="查询次数-count") 
            table.heading("生词",text="生词-strange")
            cn = sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            
            n = cur.execute('select * from word_table')
            a = n.fetchall()
            t = 0
            for i in a:
                if i[4] == 'no':
                    t+=1
                    table.insert("",t,values=(i[0],i[1],i[2],i[3],i[4]))
                    n1 = cur.execute("update word_table set count = count+1 where words = '"+i[0]+"'")
                    cn.commit()
            table.place(x = 4, y = 100, width = 710, height = 445)
        window_sign_up = tk.Tk()
        window_sign_up.geometry('718x550+590+200')
        window_sign_up.title('查询单词')
        window_sign_up.resizable(False,False)
        l1 = tk.Label(window_sign_up, text = '输入单词查询:',font = 60).place(x = 10, y = 10,width = 160, height = 35)
        e1 = tk.Entry(window_sign_up)
        e1.place(x = 190, y = 10, width = 160, height = 35)
        b1 = tk.Button(window_sign_up, text = '查询',bg = 'wheat',fg = 'red',activebackground = 'red',command = cx1)
        b1.place(x = 400, y = 10, width = 100, height = 35)
        
        l2 = tk.Label(window_sign_up, text = ' 输入汉语查询：',font = 60).place(x = 10, y = 55,width = 160, height = 35)
        e2 = tk.Entry(window_sign_up)
        e2.place(x = 190, y = 55, width = 160, height = 35)
        b2 = tk.Button(window_sign_up, text = '查询',bg = 'wheat',fg = 'red',activebackground = 'red',command = cx2)
        b2.place(x = 400, y = 55, width = 100, height = 35)
        

        b3 = tk.Button(window_sign_up, text = '查询生词',bg = 'lightcyan',fg = 'green',activebackground = 'orange',command = cx3)
        b3.place(x = 550, y = 10, width = 120, height = 35)
        b4 = tk.Button(window_sign_up, text = '查询非生词',bg = 'lightcyan',fg = 'green',activebackground = 'orange',command = cx4)
        b4.place(x = 550, y = 55, width = 120, height = 35)
    def xg_word():
        def xg1():
            xg11 = e1.get()
            xg22 = e2.get()
            cn = sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            try:
                n = cur.execute("update word_table set chinese = '"+xg22+"'"+" where words = '"+xg11+"'")
                cn.commit()
                cn.close()
                if tkinter.messagebox.askyesno('Accept','删除单词成功,点击‘是’继续修改'):
                     window_sign_up.destroy()
                     xg_word()
                else:
                     window_sign_up.destroy()
            except:
                tk.messagebox.showwarning('Warning','没有找到该单词')
                window_sign_up.destroy()
                xg_word()
        def xg2():
            xg11 = e3.get()
            xg22 = 'yes'
            cn = sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            try:
                n = cur.execute("update word_table set realise = '"+xg22+"'"+" where words = '"+xg11+"'")
                cn.commit()
                cn.close()
                if tkinter.messagebox.askyesno('Accept','删除单词成功,点击‘是’继续修改'):
                     window_sign_up.destroy()
                     xg_word()
                else:
                     window_sign_up.destroy()
            except:
                tk.messagebox.showwarning('Warning','没有找到该单词')
                window_sign_up.destroy()
                xg_word()
        def xg3():
            xg11 = e3.get()
            xg22 = 'no'
            cn = sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            try:
                n = cur.execute("update word_table set realise = '"+xg22+"'"+" where words = '"+xg11+"'")
                cn.commit()
                cn.close()
                if tkinter.messagebox.askyesno('Accept','删除单词成功,点击‘是’继续修改'):
                     window_sign_up.destroy()
                     xg_word()
                else:
                     window_sign_up.destroy()
            except:
                tk.messagebox.showwarning('Warning','没有找到该单词')
                window_sign_up.destroy()
                xg_word()
        window_sign_up = tk.Tk()
        window_sign_up.geometry('718x150+590+200')
        window_sign_up.title('修改单词')
        window_sign_up.resizable(False,False)
        
        l1 = tk.Label(window_sign_up, text = '输入单词:',font = 80).place(x = 20, y = 10,width = 110, height = 35)
        e1 = tk.Entry(window_sign_up)
        e1.place(x = 132, y = 10, width = 160, height = 35)
        
        l2 = tk.Label(window_sign_up, text = '输入汉语：',font = 80).place(x = 300, y = 10,width = 110, height = 35)
        e2 = tk.Entry(window_sign_up)
        e2.place(x = 400, y = 10, width = 160, height = 35)
        
        b1 = tk.Button(window_sign_up, text = '修改',bg = 'wheat',fg = 'red',activebackground = 'red',command = xg1)
        b1.place(x = 600, y = 10, width = 100, height = 35)
        
        l2 = tk.Label(window_sign_up, text = '输入单词:',font = 80).place(x = 20, y = 60,width = 110, height = 35)
        e3 = tk.Entry(window_sign_up)
        e3.place(x = 132, y = 60, width = 160, height = 35)
        b2 = tk.Button(window_sign_up, text = '标记为生词',bg = 'lightcyan',fg = 'green',activebackground = 'orange',command = xg2)
        b2.place(x = 310, y = 60, width = 100, height = 35)
        b3 = tk.Button(window_sign_up, text = '标记非生词',bg = 'lightcyan',fg = 'red',activebackground = 'orange',command = xg3)
        b3.place(x = 450, y = 60, width = 100, height = 35) 
    def delete_word():
        def delete():
            de11 = word_entry.get()
            cn = sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            print(de11)
            try:
                n = cur.execute("delete from word_table where words = '"+de11+"'")
                cn.commit()
                cn.close()
                if tkinter.messagebox.askyesno('Accept','删除单词成功,点击‘是’继续删除'):
                     window_delete.destroy()
                     delete_word()
                else:
                     window_delete.destroy()
            except:
                tk.messagebox.showwarning('Warning','没有找到该单词')
                window_delete.destroy()
                delete_word()
                
        window_delete= tk.Tk()
        window_delete.geometry('380x100+740+200')
        window_delete.title('删除单词')
        window_delete.resizable(False,False)
        word_Label=tk.Label(window_delete,text='输入单词：', font = 20)
        word_Label.place(x = 30, y = 30)
        word_entry=tk.Entry(window_delete)
        word_entry.place(x = 130, y = 30, width = 150, height = 30)
        b1 = tk.Button(window_delete, text = '删除', font = 20,bg = 'lightblue',fg =  'tomato',activebackground = 'orange',command = delete)
        b1.place(x = 300, y = 30,width = 60, height = 30)
        
    def study():
        def check():
            cn = sqlite3.connect('English_study_system.db')
            cur=cn.cursor()
            n = cur.execute('select * from word_table')
            a = n.fetchall()
            if word1== ent1.get():
                no = 'no'
                n = cur.execute("update word_table set realise = 'no' where words = '"+word1+"'")
                cn.commit()
                cn.close()
                tk.messagebox.showinfo("Accept","您的拼写正确！！")
                study()
            else:
                n = cur.execute("update word_table set realise = 'yes' where words = '"+word1+"'")
                cn.commit()
                cn.close()
                tk.messagebox.showwarning("Wrong","您的拼写错误！！")
        import random
        cn = sqlite3.connect('English_study_system.db')
        cur=cn.cursor()
        n = cur.execute('select * from word_table')
        a = n.fetchall()
        t = 0
        for i in a:
            t = t + 1
        n = cur.execute('select * from word_table')
        a = n.fetchall()
        word1 = ""
        china1 = ""
        sex1 = ""
        tt = random.randint(0,t-1)
        t = -1
        for i in a:
            t = t + 1
            if tt == t:
                word1 = i[0]
                sex1 = i[1]
                china1 = i[2]
                break
        lab1 = tk.Label(home_window,fg = 'black', bg = 'white',text = "单词汉语："+china1, font = 40)
        lab1.place(x = 550, y = 150, width = 200, height = 50)
        lab2 = tk.Label(home_window,fg = 'black', bg = 'white',text = "单词词性："+sex1, font = 40)
        lab2.place(x = 550, y = 250, width = 200, height = 50)
        ent1 = tk.Entry(home_window, font = ('隶书',18),	justify = 'center')
        ent1.place(x = 550, y = 350, width = 200, height = 50)
        but1 = tk.Button(home_window,text = "检查拼写",bg = 'lightcyan',fg = 'green',activebackground = 'orange', command = check)
        but1.place(x = 550, y = 450, width = 200, height = 50)
        
    menubar = tk.Menu(home_window) 
    menubar.add_cascade(label='  主界面  ')
    menubar.add_cascade(label='  添加单词  ', command = add_words)
    menubar.add_cascade(label='  导入单词  ', command = dr_word)
    menubar.add_cascade(label='  查询单词  ', command = cx_word)
    menubar.add_cascade(label='  查看单词表  ', command = display)
    menubar.add_cascade(label='  修改单词  ', command = xg_word)
    menubar.add_cascade(label='  删除单词  ', command = delete_word)
    menubar.add_cascade(label='  修改密码  ', command = password_change)
    menubar.add_cascade(label='  退出账号  ', command = login1)
    menubar.add_cascade(label='  退出系统  ', command = home_window.destroy)
    home_window.config(menu=menubar)
    
    log = Image.open('images//index.png')
    photo1 = ImageTk.PhotoImage(log)
    
    img1 = Label(home_window,image=photo1)
    img1.image=photo1
    img1.place(x = 0, y = 0)
    button1 = tkinter.Button(home_window,text='开始学习',bg = 'wheat',fg = 'red',activebackground = 'red', command=study)
    button1.place(x=550, y=550, width=200, height=50)
    

    
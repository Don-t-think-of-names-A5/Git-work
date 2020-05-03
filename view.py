"""
Created on Thu Dec 12 2019

@author: WMY
"""
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import MainPage

#添加与修改类
class InputFrame(Frame): # 继承Frame类 
 def __init__(self, value=None): 
  Frame.__init__(self, value) 
  self.root = value #定义内部变量root 
#  self.English = StringVar() 
#  self.Types = StringVar() 
#  self.Chinese = StringVar() 
  self.createPage() 
 
 def createPage(self): 
  def cleanup():
      English.delete(0, END)
      Types.delete(0, END)
      Chinese.delete(0, END)
  def insert():
#      ll = list()
#      ll.append(English.get())
#      print(type(ll[0]))
      if English.get() == "" or Types.get() == "" or Chinese.get() == "":
          showwarning(title="不能为空", message="请您输入全部内容后添加！")
          return
#      elif type(ll[0]) == int:
#          showinfo("错了吧","您有数字的英语单词嘛？")
#          return
      with open("data//user.txt",encoding='utf-8')as f:
          username = f.readline()
      sss = "En_" + username + "_words"
      import sqlite3
      cn = sqlite3.connect('data//EnStudy.db')
      cur = cn.cursor()
      n = cur.execute('select * from ' + sss)
      a = n.fetchall() #这是一个保存着每一行数据的列表，第一行第一列的数据即a[0][0]
      flag = 0 #标记是否覆盖
      tmp = True #标记点了是否
      for i in a:
          if i[0] == English.get():
              tmpstr = "词性为“"+i[1]+"”的单词“"+i[0]+"”已存在，在表中释义为“" + i[2] + "”，覆盖吗？"
              tmp = askyesno("已存在",tmpstr)
              if tmp:
                  sql = "update "+sss+" set Types = '"+Types.get()+"' , Chinese = '"+Chinese.get()+"' where English = '"+i[0]+"'"
                  #print(sql)
                  cur.execute(sql) #注意sql语句中=后边的字符串要用引号引起来，所以这里要用两个引号，syntax错误注意空格
                  showinfo("覆盖成功","单词已覆盖。")
                  flag = 1 #表示覆盖了，后边便不用添加
              break
      if flag == 0 and tmp == True: #表示点了是 覆盖后flag便置为1，或者点了否tmp置为false，二者都不会进入该语句。只有默认值0和true时会进入
          b = list()
          b.append(English.get())
          b.append(Types.get())
          b.append(Chinese.get())
          cur.execute('insert into '+sss+' VALUES (?,?,?,0)', b)
          showinfo("成功","添加成功！")
      cn.commit()
      cn.close()
  Label(self, text='添加单词/短语', font = "楷体").grid(row = 0, columnspan = 4, pady = 10) 
  Label(self, text = '例：account  n.名词;v.动词  计算,帐目,说明;说明,认为',font =('微软雅黑',11)).place(x=90, y = 50,width = 360) 
  Label(self, text = '（多种词性和释义用";"分隔,短语词性请写"短语"二字）',font =('微软雅黑',11)).place(x=90, y=90, width = 350) 
  Label(self).grid(row=1, stick=W, pady=20) 
  #Label(self).grid(row=2, stick=W, pady=20) 
  Label(self, text = '单词/短语内容: ', font = "楷体").grid(row=3, stick=W, pady=10) 
  English = Entry(self, width=50)
  English.grid(row=3, column=1, columnspan = 3, stick=E) 
  Label(self, text = '单词/短语词性: ', font = "楷体").grid(row=4, pady=10) 
  Types = Entry(self, width=50)
  Types.grid(row=4, column=1, columnspan = 3, stick=E) 
  Label(self, text = '单词/短语释义: ', font = "楷体").grid(row=5, pady=10) 
  Chinese = Entry(self, width=50)
  Chinese.grid(row=5, column=1, columnspan = 3, stick=E) 
  Button(self, text='清空', font = "楷体",relief=tkinter.GROOVE, command=cleanup).grid(row=7,column = 0, columnspan=2, pady=10) 
  Button(self, text='录入', font = "楷体",relief=tkinter.GROOVE, command=insert).grid(row=7,column=2, columnspan=2, pady=10) 
  Label(self, text = '          注：在此可以输入要修改的单词和内容，\n        提示是否覆盖，点击是便可将单词修改成功。',font =('微软雅黑',11)).grid(row = 8, columnspan = 4)

#查询界面类  
class SearchFrame(Frame): # 继承Frame类 
 def __init__(self, value=None): 
  Frame.__init__(self, value) 
  self.root = value #定义内部变量root 
  self.createPage() 
 
 def createPage(self):
  En = Entry(self, relief=tkinter.GROOVE)
  En.grid(row = 1, column = 0, pady = 10)
  Ty = Entry(self, relief=tkinter.GROOVE)
  Ty.grid(row = 1, column = 1, pady = 10)
  Ch = Entry(self, relief=tkinter.GROOVE)
  Ch.grid(row = 1, column = 2, pady = 10)
  import sqlite3
  cn = sqlite3.connect('data//EnStudy.db')
  cur = cn.cursor()
  with open("data//user.txt",encoding='utf-8')as f:
      username = f.readline()
  sss = "En_" + username + "_words"
  def selectAll():
      n = cur.execute('select * from ' + sss)
      global All
      All = n.fetchall()
      if All:
          global a
          a = All
          insert()
      else:
          if(askyesno("导入吗","您的单词表是空的，现在导入吗？")):
              MainPage.openfile() #跳转到导入函数
              selectAll()

  def selectEn(): #查询英语
      if En.get() == "" :
          showinfo("错误","请输入要查询的英语单词或短语。")
          return
      global a
      a = list()
      for i in All:
          if i[0] == En.get():
              a.append(i)
              cur.execute("update "+sss+" set SearchCount=SearchCount+1 where English = '"+i[0]+"'")
      cn.commit()
      insert()
  def selectTy(): #查询词性
      if Ty.get() == "" :
          showinfo("错误","请输入要查询的词性。")
          return
      global a
      a = list()
      for i in All:
          if Ty.get() in i[1]:
              a.append(i)
              cur.execute("update "+sss+" set SearchCount=SearchCount+1 where English = '"+i[0]+"'")  #增加查询次数（用主码匹配）
      cn.commit()
      insert()
  def selectCh(): #查询释义
      if Ch.get() == "" :
          showinfo("错误","请输入要查询的中文释义。")
          return
      global a
      a = list()
      for i in All:
          if Ch.get() in i[2]:
              a.append(i)
              cur.execute("update "+sss+" set SearchCount=SearchCount+1 where English = '"+i[0]+"'")
      cn.commit()
      insert()
  def insert():
      x=tree.get_children()
      for item in x:
          tree.delete(item)
      t = 0
      for i in a:
          tree.insert("",t,values=(t+1,i[0],i[1],i[2],i[3])) #插入数据
          t = t + 1
      tree.grid(row = 3, columnspan = 3, pady = 10)
  Label(self, text='单词/短语查询', font = "楷体").grid(row = 0, column = 1, pady = 10)
  Button(self, text = '查询所有',command=selectAll,font = ("楷体",16),relief=tkinter.GROOVE).grid(row = 0, column = 2, pady = 10)
  Button(self, text = '查找英文',command=selectEn,font = ("楷体",16),relief=tkinter.GROOVE).grid(row = 2, column = 0, pady = 10)
  Button(self, text = '查找词性',command=selectTy,font = ("楷体",16),relief=tkinter.GROOVE).grid(row = 2, column = 1, pady = 10)
  Button(self, text = '查找释义',command=selectCh,font = ("楷体",16),relief=tkinter.GROOVE).grid(row = 2, column = 2, pady = 10)
  tree=ttk.Treeview(self,height=22,show="headings")#表格
  tree["columns"]=("序号","单词短语","词性","释义","查询次数")
  #表示列,不显示
  tree.column("序号",width=50) 
  tree.column("单词短语",width=100)   
  tree.column("词性",width=100)
  tree.column("释义",width=200)
  tree.column("查询次数",width=100)
 
  tree.heading("序号",text="序号—NO.") 
  tree.heading("单词短语",text="单词/短语-Words&Phrases")  #显示表头
  tree.heading("词性",text="词性-Part of speech")
  tree.heading("释义",text="释义-Paraphrase")
  tree.heading("查询次数",text="查询次数-Count")
  
  selectAll() #默认显示所有单词
  #设置滚动条
  Vsbar = ttk.Scrollbar(self, orient = VERTICAL,command=tree.yview)
  tree.configure(yscrollcommand=Vsbar.set)
  
  Vsbar.grid(row = 3, column = 3, sticky = NS)
  
  def delete(): #删除单词函数
      del_data = tree.focus() #获取到表格中目前选中的单词行，返回为字典类型
      del_list = list()
      del_list = tree.item(del_data)['values'] #将键为values的值（即表格中选中行的内容）保存到列表中
      if del_list:  #判断列表是否为空即判断用户是否点击了列表里的行
          print(del_list[1])
          import sqlite3
          cn = sqlite3.connect('data//EnStudy.db')
          cur = cn.cursor()
          with open("data//user.txt",encoding='utf-8')as f:
              username = f.readline()
          sss = "En_" + username + "_words"
          cur.execute("delete from "+ sss + " where English = '" + str(del_list[1]) +"'")
          cn.commit()
          cn.close()
          showinfo("成功","删除成功。")
          selectAll()
      else:
          showwarning("未选择","请选择要删除的单词，然后点击删除！")
  Label(self, text = "从上面表格选择想要删除的\n单词，然后点击下面的按钮。").grid(row = 4, column = 1,sticky = E)
  Button(self, text = '删除单词',command=delete,font = ("楷体",16),relief=tkinter.GROOVE).grid(row = 4, column = 2, sticky = E, pady = 10)
  # grid 的 sticky 参数，它可以用 N， E， S， W 表示上右下左，它决定了这个组件是从哪个方向开始的，
  #点击属性排序
  def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)  # 排序方式
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
  for col in tree["column"]:  # 绑定函数，使表头可排序
    tree.heading(col, text=col, command=lambda _col=col: treeview_sort_column(tree, _col, False))

#关于界面类
class AboutFrame(Frame): # 继承Frame类 
 def __init__(self, value=None): 
  Frame.__init__(self, value) 
  self.root = value #定义内部变量root 
  self.createPage() 
  
 def createPage(self): 
  cv1=Canvas(self,bg='whitesmoke',width=1000,height=50) #生成彩条
  cv2=Canvas(self,bg='black',width=900,height=40)
  cv3=Canvas(self,bg='Deepskyblue',width=800,height=30)
  cv4=Canvas(self,bg='Aqua',width=700,height=20)
  cv5=Canvas(self,bg='DeepPink',width=600,height=10)
  #img=PhotoImage(file='about.gif')
  #cv1.create_image((100,100),image=img)
  cv1.pack()
  cv2.pack(pady=0)
  cv3.pack(pady=0)
  cv4.pack(pady=0)
  cv5.pack(pady=0)
  Label(self, text='关于', font = ("幼圆",16),compound = CENTER).pack() 
  Label(self, text='About\n', font = ("Rockwell",12),compound = CENTER).pack() 
  Label(self, text="制作者：王明阳", font = ("幼圆",16),compound = CENTER).pack()
  Label(self, text="Made by WMY\n", font = ("Rockwell",12),compound = CENTER).pack()
  Label(self, text="2019年12月", font=("幼圆",16),compound = CENTER).pack()
  Label(self, text="December 2019", font=("Rockwell",12),compound = CENTER).pack()
  cv5=Canvas(self,bg='DeepPink',width=600,height=10)
  cv5.pack(pady=0)
  #图片显示

#欢迎主界面类
class HomeFrame(Frame): # 继承Frame类 
 def __init__(self, value=None): 
  Frame.__init__(self, value) 
  self.root = value #定义内部变量root 
  self.createPage() 
  
 def createPage(self): 
  def startstudy(): #点击学习函数
   tt = Tk()
   tt.title("匹配学习")
   #tt.geometry("400x400+200+200")
   tt.resizable(False,False)
   import random
   import sqlite3
   cn = sqlite3.connect('data//EnStudy.db')
   cur = cn.cursor()
   with open("data//user.txt",encoding='utf-8')as f:
      username = f.readline()
   sss = "En_" + username + "_words"
   n = cur.execute("select * from "+sss)
   a = n.fetchall()
   if len(a) < 3:
       tt.destroy()
       showinfo("ComeOn","您的单词库不足3个无法学习哦，\n请先添加足够单词后学习~")
   else:
       ran_num = random.randint(0,len(a)-1) #随机生成一个序号作为题目
       qus = a.pop(ran_num) #获取到该行内容并弹出列表，以便后面生成错误选项
       wrong1 = random.randint(0,len(a)-1)
       qusw1 = a.pop(wrong1)
       wrong2 = random.randint(0,len(a)-1)
       qusw2 = a.pop(wrong2)
       que = [] #用来存储按钮的顺序
       while(len(que)<3): #生成随机的按钮位置
           x=random.randint(1,3)
           if x not in que:
               que.append(x)
   def panduan(data):
       if data == qus[2]:
           showinfo("正确","回答正确！")
           tt.destroy()
           startstudy()
       else:
           showwarning("错误","回答错误！")
   def closewindow():
       tt.destroy()
   Label(tt,text=" ",font=('楷体',14)).grid(row = 0,column = 0,pady=20) #控制边距
   Label(tt,text=" ",font=('楷体',14)).grid(row = 0, column = 2,pady=20) #控制边距
   Label(tt,text=qus[0]+"\n"+qus[1],font=('楷体',14)).grid(row = 0, column = 1,pady=20)
   Button(tt,text=qus[2],font=('隶书',14),command=lambda:panduan(qus[2]),relief=tkinter.GROOVE).grid(row = que[0], column = 1,pady=20)
   Button(tt,text=qusw1[2],font=('隶书',14),command=lambda:panduan(qusw1[2]),relief=tkinter.GROOVE).grid(row = que[1], column = 1,pady=20)
   Button(tt,text=qusw2[2],font=('隶书',14),command=lambda:panduan(qusw2[2]),relief=tkinter.GROOVE).grid(row = que[2], column = 1,pady=20)
   Label(tt,text="\n请从上面选择正确选项",font=('楷体',14)).grid(row = 4,column = 1,pady=20)
   Button(tt,text="退出学习",font=('隶书',12),bg="white",command=closewindow,relief=tkinter.GROOVE).grid(row = 5, column = 1,pady=20)
   tt.mainloop()
  Label(self, text = "                                            ", font = "隶书").grid(row=0, column = 3) 
  Label(self, text = "⬆请看向这里！\n字有点小将就看啦\n（。＾▽＾）", font=('隶书')).grid(row = 1, column = 0)
  Label(self, text = "    \n\n\n\nฅʕ•̫͡•ʔฅ", font=('隶书',20)).grid(row = 2, column = 1)
  Label(self, text = "   ┏━━━━━━━━┓", font=('隶书',20)).grid(row = 3, column = 1)
  Label(self, text = "    欢迎来到大学英语学习平台！\n(ง •_•)ง", font=('隶书',26)).grid(row = 4, column = 1)
  Label(self, text = " ", font=('隶书',20)).grid(row = 5, column = 1)
  Button(self, text = "点击学习",font=('隶书',16),command=startstudy,relief=tkinter.GROOVE,bg='azure',fg='gold',activebackground='lightcyan').grid(row = 6, column = 1)
  #Label(self, text = "┏Made By WMY┓", font=('隶书',14)).grid(row = 5, column = 1)
  #Label(self, text = "┏━━━━━━━━┓", font=('隶书',14)).grid(row = 6, column = 1)
  #.place(x=0,y=10,height=90,width=260)
  
 
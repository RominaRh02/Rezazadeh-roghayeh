import sqlite3
import tkinter
try:
    cnt=sqlite3.connect('d:/shop.db')
    print("opened database successfully!")
except:
    print("Error!")

#---------------------creat users table---------------------
##query='''CREATE TABLE users
##    (ID INTEGER PRIMARY KEY,
##    users CHAR(25) NOT NULL,
##    password CHAR(25) NOT NULL,
##    addr CHAR(50) NOT NULL
##    )'''
##cnt.execute(query)
##cnt.close()

#----------------------------------insert data to users table--------------
##query='''INSERT INTO users (user,password,addr)
##    VALUES ("admin","123456789","rasht")'''
##cnt.execute(query)
##cnt.commit()
##cnt.close()
#----------------------------------functions-----------------------------


def login():
    global user
    global pas
    user=txt_user.get()
    pas=txt_pass.get()
    query='''SELECT id FROM  users WHERE user=? AND password=? '''
    result=cnt.execute(query,(user,pas))
    rows=result.fetchall()
    if(len(rows)==0):
        lbl_msg.configure(text="wrong username or password!",fg="red")
        return
    btn_login.configure(state="disabled")
    lbl_msg.configure(text="welcome to your account!",fg="green")
    btn_delete.configure(state="normal")
    btn_logout.configure(state="normal")

def submit():
    global txt_user2
    global txt_pass2
    global txt_addr
    global lbl_msg2
    win2=tkinter.Toplevel(win)
    win2.geometry("300x300")
    
    lbl_user2=tkinter.Label(win2,text="username: ")
    lbl_user2.pack()

    txt_user2=tkinter.Entry(win2,width=15)
    txt_user2.pack()

    lbl_pass2=tkinter.Label(win2,text="password: ")
    lbl_pass2.pack()

    txt_pass2=tkinter.Entry(win2,width=15)
    txt_pass2.pack()

    lbl_addr=tkinter.Label(win2,text="address: ")
    lbl_addr.pack()

    txt_addr=tkinter.Entry(win2,width=15)
    txt_addr.pack()

    lbl_msg2=tkinter.Label(win2,text="")
    lbl_msg2.pack()

    btn_submit2=tkinter.Button(win2,text="Submit",command=submit2)
    btn_submit2.pack(pady=10)
    
    
    win2.mainloop()

def submit2():
    global txt_user2
    global txt_pass2
    global txt_addr
    global lbl_msg2
    user2=txt_user2.get()
    pas2=txt_pass2.get()
    addr=txt_addr.get()
    query='''SELECT id FROM users WHERE user=?'''
    result=cnt.execute(query,(user2,))
    rows=result.fetchall()

    if(len(rows)!=0):
        lbl_msg2.configure(text="you have an account!",fg="red")
        return
    if(len(user2)==0):
        lbl_msg2 .configure(text="fill in the user!",fg="red")
        return
    if(len(pas2)<8):
        lbl_msg2.configure(text="the length of the password must be more than eight characters!                  ",fg="red")
        return
    query2='''INSERT INTO users(user,password,addr)
    VALUES(?,?,?)'''
    cnt.execute(query2,(user2,pas2,addr))
    cnt.commit()
    lbl_msg2.configure(text="submit done!!!",fg="green")
    btn_submit.configure(state="disabled")

def logout():
    user3=txt_user.get()
    pas3=txt_pass.get()

    query='''SELECT id FROM users WHERE user=? AND password=?'''
    result=cnt.execute(query,(user3,pas3))
    rows3=result.fetchall()

    if(len(rows3)!=0):
        lbl_msg.configure(text="you are logout",fg="green")
        btn_login.configure(state="normal")
        btn_logout.configure(state="disabled")
    else:
        lbl_msg.configure(text="wrong user or password",fg="red")
        

def delete():
    global lbl_msg4
    win3=tkinter.Toplevel(win)
    win3.geometry("300x300")

    lbl_msg3=tkinter.Label(win3,text="Are you sure?")
    lbl_msg3.pack()

    btn_yes=tkinter.Button(win3,text="YES",command=yes)
    btn_yes.pack(pady=6)

    btn_no=tkinter.Button(win3,text="NO",command=no)
    btn_no.pack(pady=6)

    lbl_msg4=tkinter.Label(win3,text="")
    lbl_msg4.pack()
def yes():
    global lbl_msg4
    global user
    global pas
    
    query='''DELETE FROM users WHERE user=? AND password=?'''
    cnt.execute(query,(user,pas))
    cnt.commit()
    lbl_msg4.configure(text="your account has been deleted",fg="green")
    btn_delete.configure(state="disabled")
    btn_login.configure(state="normal")
    btn_logout.configure(state="disabled")
    
def no():
    global lbl_msg4
    lbl_msg4.configure(text="your account was not deleted",fg="red")
    return


   
###------------------------------Main-------------------------

win=tkinter.Tk()
win.geometry("400x300")

lbl_user=tkinter.Label(text="username: ")
lbl_user.pack()

txt_user=tkinter.Entry(width=25)
txt_user.pack()

lbl_pass=tkinter.Label(text="password: ")
lbl_pass.pack()

txt_pass=tkinter.Entry(width=25)
txt_pass.pack()

lbl_msg=tkinter.Label(text="")
lbl_msg.pack()

btn_login=tkinter.Button(text="Login",command=login)
btn_login.pack(pady=10)

btn_submit=tkinter.Button(text="Submit",command=submit)
btn_submit.pack(pady=10)

btn_delete=tkinter.Button(text="Delete",command=delete)
btn_delete.pack(pady=10)
btn_delete.configure(state="disabled")

btn_logout=tkinter.Button(text="logout",command=logout)
btn_logout.pack(pady=10)
btn_logout.configure(state="disabled")

win.mainloop()

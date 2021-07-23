from tkinter import *
#from tkinter.ttk import *
from main import *
#master = Tk()
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Banking Form')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

#def openNewWindow():
#    newWindow = Toplevel(master)
#    newWindow.title("display")
#    newWindow.geometry("200x200")
#    Label(newWindow, text="user").pack()
#label = Label(master, text="This will open a new window")
#label.pack(pady = 10)

#next = Button(master, text="Next", command = openNewWindow())

#signup
login = Button(tkWindow, text="login" , command=read_one_user).grid(row=5, column=0)
signup = Button(tkWindow, text="Sign Up", command=insert_user).grid(row=6, column=0)



#tkWindow.mainloop()

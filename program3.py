from tkinter import *
from functools import partial

def validateLogin(Name, Times):
	print("Name you want to print : ",Name.get())
	print("no. of times you want to print : ", Times.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('800x500')  
tkWindow.title('Name printer unlimited.exe')

#username label and text entry box
NameLabel = Label(tkWindow, text="Name you want to print: ").grid(row=1, column=1)
Name =   StringVar()
NameEntry = Entry(tkWindow, textvariable=Name).grid(row=1, column=2)  

#password label and password entry box
TimesLabel = Label(tkWindow,text="no. of time you want to print: ").grid(row=3, column=1)  
Times = IntVar()
TimesEntry = Entry(tkWindow, textvariable=Times, show='*').grid(row=3, column=2)  

validateLogin = partial(validateLogin, Name, Times)

#login button
printButton = Button(tkWindow, text="Print it", command= validateLogin ).grid(row=5, column=1)   

tkWindow.mainloop()













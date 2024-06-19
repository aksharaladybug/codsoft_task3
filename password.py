import tkinter as tk
import random
def passwordgen(strength="easy"):
    string1="abcdefghijklmnopqrstuvwxyz"
    string2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string3="1234567890"
    string4="!@#$%^&*()<>?.,_-+=|\{[}]"
    inputofuser=int(length.get())
    passwordgenerated=""#to initialise it to empty string
    if strength=="easy":     
        string5=string1+string2
    elif strength=="medium":
        string5=string1+string2+string3
    elif strength=="strong":
        string5=string1+string2+string3+string4
    for i in range(0,inputofuser):
        passwordgenerated+=random.choice(string5)
    label.config(text=passwordgenerated)#to show generated password on the label
window=tk.Tk()
window.title("Password generator")
window.geometry('280x380')
window.configure(background="light yellow")
lengthlabel=tk.Label(window,text="Enter length of string:",font=("Arial",20),borderwidth=5)
lengthlabel.grid(row=0,column=0,padx=20,pady=20)
length=tk.Entry(window)
length.grid(row=0,column=1,columnspan=5,padx=20,pady=20)
easybutton=tk.Button(window,text="Easy",width=10,height=3,bg="light green",font=("Arial",20),command=lambda:passwordgen("easy"),activebackground="green",activeforeground="white")
easybutton.grid(row=1,column=0,padx=20,pady=20)
mediumbutton=tk.Button(window,text="Medium",width=10,height=3,bg="light green",font=("Arial",20),command=lambda:passwordgen("medium"),activebackground="green",activeforeground="white")
mediumbutton.grid(row=1,column=1,padx=20,pady=20)
strongbutton=tk.Button(window,text="Strong",width=10,height=3,bg="light green",font=("Arial",20),command=lambda:passwordgen("strong"),activebackground="green",activeforeground="white")
strongbutton.grid(row=1,column=2,padx=20,pady=20)
genpass=tk.Button(window,width=15,height=3,text="Generate password",bg="light green",font=("Arial",20),command=lambda:passwordgen("easy"))
#lambda used only when the function that has to be called when button pressed has to have arguments passed
genpass.grid(row=2,column=0,columnspan=2,padx=20,pady=20)
label=tk.Label(window,width=30,height=3,bg="light yellow",text="",font=("Arial",20))
label.grid(row=3,column=0,columnspan=2,padx=20,pady=20)
window.mainloop()
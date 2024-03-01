from tkinter import *
import os
def restart():
    os.system("shutDown /r /t 1")
def restart_time():
    os.system("ShutDown /r /t 20")
def LogOut():
    os.system("ShutDown -1")
def shutDown():
    os.system("ShutDown /s /t 1")
st=Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="blue")

r_button=Button(st,text="Restart",font=("Time Roman New",30,"bold"),
                relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=40,width=200)
r_button=Button(st,text="Restart_time",font=("Time Roman New",20,"bold"),
                relief=RAISED,cursor="plus",command=restart_time)
r_button.place(x=150,y=170,height=40,width=200)
r_button=Button(st,text="LogOut",font=("Time Roman New",20,"bold"),
                relief=RAISED,cursor="plus",command=LogOut)
r_button.place(x=150,y=270,height=40,width=200)
r_button=Button(st,text="shutDown",font=("Time Roman New",20,"bold"),
                relief=RAISED,cursor="plus",command=shutDown)
r_button.place(x=150,y=370,height=40,width=200)

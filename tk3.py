import tkinter
import threading
from time import sleep

root = tkinter.Tk()
root.title("Tcl/Tk")
root.geometry("640x400+100+100")
root.resizable(False, False)

count=0
flag = False


def countUP():
    global count, flag
    while flag:
        count +=1
        label.config(text=str(count))
        sleep(0.01)


def running():
    global flag
    flag = True
    thr = threading.Thread(target=countUP, args=None)
    thr.start()


def stopping():
    global flag
    flag = False


label = tkinter.Label(root, text="0")
label.pack()

button1 = tkinter.Button(
    root,
    text='Run',
    width=5,
    height=2,
    overrelief="solid",
    command=countUP,
    repeatdelay=500,
    repeatinterval=25)

button2 = tkinter.Button(
    root,
    text='Run',
    width=5,
    height=2,
    overrelief="solid",
    command=running,
    repeatdelay=500,
    repeatinterval=25)

button1.pack(side=tkinter.LEFT)
button2.pack(side=tkinter.LEFT)

root.mainloop()
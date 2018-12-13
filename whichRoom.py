from tkinter import *
import requests
import sys

def checkedFun():
    fobject=open("gpFile2.txt","w")
    fobject.write(var.get())
    fobject.close()

def exitWindow():
    window2.destroy()

try:
    fobject=open("gpFile.txt","r")
    token=fobject.readline()
    fobject.close()
except:
    print("Files missing! Please rum GitterPythonMain.py")
    sys.exit()

i=0
window2=Tk()
window2.title("Choose the room")
window2.geometry("500x500+50+50")
frame3=Frame(window2)

url="https://api.gitter.im/v1/rooms?access_token="+token
room=requests.get(url).json()
var=StringVar()
lbl=Label(frame3,text="You are part of these rooms\nPlease choose the room whose messages you wish to see.",fg="green",font=("Arial",12),anchor="n",justify="center")
lbl.pack(fill="both")
try:
    while (room[i]['id']):
        print(room[i]['name'])
        window2.update_idletasks()
        radio=Radiobutton(frame3,text=room[i]['name'],variable=var,value=room[i]['name']+"\n"+room[i]['id'],anchor="w",justify="left",command=checkedFun)
        var.set(1)
        radio.pack(fill="x")
        i=i+1
except:
    print("Reached the end")
save=Button(frame3,text="Fetch my messages",font=("Arial",12),justify="center",command=exitWindow)
save.pack()
frame3.pack(fill="both")
window2.mainloop()

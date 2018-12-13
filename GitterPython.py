from tkinter import *
import requests
window = Tk()
window.title("GitterApp")
window.geometry("800x600+50+50")

try:
    fobject=open("gpFile.txt","r")
    token=fobject.readline()
    fobject.close()

    fobject=open("gpFile2.txt","r")
    roomName=fobject.readline()
    roomid=fobject.readline()
    fobject.close()

    canvas=Canvas(window,bg="lightgray")
    scrollbar=Scrollbar(window,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    frame=Frame(canvas)

    txt = Label(frame,text="Welcome to GitterPython\nRoomName: "+roomName,bg="lightgray",font=("consolas",12),fg="red")
    txt.pack(fill="x")
    window.update_idletasks() #Used to update idletasks
    content=""
    temp=""

    i=0
    url="https://api.gitter.im/v1/rooms/"+roomid
    url=url+"/chatMessages?access_token="+token

    msg=requests.get(url).json()
    try:
        while (msg[i]['text']):
            if(msg[i]['unread']):
                color="darkred"
            else:
                color="blue"
            content=content+"\n*****************************\nMessage from: "+msg[i]['fromUser']['displayName']+"\n"
            content=content+"Username: "+msg[i]['fromUser']['username']+"\n*****************************\n\n"
            for p in msg[i]['text']:
                try:
                    content=content+p
                    temp=temp+p
                    window.update_idletasks() #Used to update idletasks
                    if(p=='\n'):
                        temp=""
                    if(len(temp)>(window.winfo_width()/5.5)):
                        temp=""
                        content=content+"\n"
                except:
                    print(" UCS-2 codec here")

            content=content+"\n\n"
            txt.pack(fill="x")
            if(i%2==0):
                txt = Label(frame,text=content,anchor="w",justify=LEFT,fg=color,bg="lightgray")
            else:
                txt = Label(frame,text=content,anchor="w",justify=LEFT,fg=color,bg="gray")
            content=""
            i=i+1
            #print(len(content))
    except:
        print("\n\nReached the end")
    frame.pack(fill="both")
    canvas.pack(fill="both")
    canvas.create_window((0,0),window=frame,anchor='nw')
    canvas.configure(scrollregion=canvas.bbox("all"),width=800,height=600)
    window.mainloop()

except:
    print("Files missing! Please rum GitterPythonMain.py")
    window.destroy()

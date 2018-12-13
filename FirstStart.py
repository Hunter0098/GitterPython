from tkinter import *
import tkinter.messagebox
window=Tk()
window.geometry("800x500+50+50")
frame1=Frame(window)
lbl1=Label(frame1,text="\nWelcome to GitterPython one time setup",font=("Arial", 16),fg="red")
lbl1.pack(fill="x")
lbl2=Label(frame1,text="\nLet's get a few things setup together :-)\n",font=("Arial", 16),fg="green")
lbl2.pack(fill="x")
lbl3=Label(frame1,text="\tPlease enter your access-token here: \t",font=("Arial", 14),fg="green")
lbl3.pack(side=LEFT)
entry1=Entry(frame1,bd=2,font=("Arial",14))
entry1.pack(side=LEFT)
frame1.pack(fill="both")
def doneFun():
    if(entry1.get()==""):
        tkinter.messagebox.showinfo("Error","Token can't be empty.")
    else:
        fobject=open("gpFile.txt","w")
        fobject.write(entry1.get())
        fobject.close()
        window.destroy()
frame2=Frame(window)
lbl4=Label(frame2,text="\nOnce done please click proceed\n",anchor="n",justify="center",font=("Arial", 14),fg="green")
lbl4.pack(fill="both")
button1=Button(frame2,text="Proceed",command=doneFun,font=("Arial",14),fg="blue")
button1.pack(fill="y")
frame2.pack(fill="both")
window.mainloop()


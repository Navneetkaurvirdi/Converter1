import tkinter as tk
from tkinter import*
import pyttsx3

engine=pyttsx3.init()


def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()



root=Tk()
textv=StringVar()

root.config(bg="cornsilk3")
obj=LabelFrame(root, text="Text to speech", font=30, bd=2, bg="bisque2", fg="black")
obj.pack(fill="both", expand="yes", padx=30, pady=30)

lbl=Label(obj, text="Text", font=30, bg="bisque2", fg="bisque4")
lbl.pack(side=tk.LEFT, padx=5)

text=Entry(obj, textvariable=textv, font=30, width=30, bd=8)
text.pack(side=tk.LEFT, padx=10)


btn=Button(obj, text="Speak", bg="bisque4", fg="white",font=20, command=speaknow, activebackground="cornsilk3" )
btn.pack(side=LEFT,  padx=10)

root.title("text to speech")
root.resizable(False, False)
root.geometry("600x300")
mainloop()


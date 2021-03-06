import pyshortners
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

win = tk.Tk()
win.title("URL shortner")
def short():
    url = entry_url.get()
    shortend_url = pyshortners.Shortener()
    showinfo("Shortend URL",f"{shortend_url.tinyurl.short(url)}")

url_label = tk.Label(win,text="Enter URL Here :  ")
url_label.grid(row=0,column=0)

entry_url = tk.Entry(win,width=30,bg="#69BEF6",bd=2) 
entry_url.grid (row=0,column=1,padx=5,pady=5)

button = ttk.Button(win,text="Short",command=short)
button.grid(row=1,column=0,columnspan=2)

win.mainloop()

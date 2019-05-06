from tkinter import*
import tkinter as tk
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('feedback.db')
c = conn.cursor()


def check():
    faculty = nameE.get()
    print(faculty)
    subject = subjectE.get()
    print(subject)
    c.execute("SELECT AVG(score) FROM feedback WHERE faculty =? AND subject =?",(faculty, subject))
    a=c.fetchall()
    print(a)
    conn.commit()
    #print(a)

root = tk.Tk()
root.title("Sentiment analysis on student feedback form")

Module = Label(root, text = "Admin Module", font =("arial",17,"bold"))
Module.grid(row = 0, column = 0, columnspan = 2, padx = 5, sticky = W)

name = Label(root, text = "Faculty Name")
name.grid(row = 1, column = 0, columnspan = 1, padx = 5, sticky = W)

nameE = tk.StringVar()                         # 2
nameChosen = ttk.Combobox(root, width=47, textvariable=nameE) #3
nameChosen['values'] = ('Select a faculty','S Avinash','K Santosh rao','Sashi Bhusan Maharana','Manoj Kar','Chandan ku. Giri')     # 4
nameChosen.grid(column=1, row=1,padx=5)              # 5
nameChosen.current(0)   


subject = Label(root, text = "Subject Name")
subject.grid(row = 2, column = 0, columnspan = 1, padx = 5, sticky = W)

subjectE = tk.StringVar()                         # 2
subjectChosen = ttk.Combobox(root, width=47, textvariable=subjectE) #3
subjectChosen['values'] = ('Select a subject','Software Engineering','Database Management system','OOP using Java','CCNA','Programming in C')# 4
subjectChosen.grid(column=1, row=2,padx=5)              # 5
subjectChosen.current(0)   

check = Button(root, text = "Submit", command = check)
check.grid(row=3, column=1, pady=10)




root.mainloop()


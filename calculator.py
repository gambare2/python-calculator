import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Calculator Application")
window.geometry("400x500")
window.config(bg="#202020")
display = tk.Entry(window,font=("Arial Black",20),background="#202020",foreground="White",borderwidth = 5,justify="right")
display.grid(row=0,column=0,columnspan=4,padx=10,pady=10,sticky="nsew")
def button_click(value):
    current_text = display.get()
    display.delete(0,tk.END)
    display.insert(0,current_text+str(value))
def button_clear():
    display.delete(0,tk.END)
def button_equal():
    try:
        result= eval(display.get())
        display.delete(0,tk.END)
        display.insert(0,result)
    except Exception as e:
        display.delete(0,tk.END)
        display.insert(0,"Error")
def handle_key(event):
    key = event.char
    if key in "0123456789+-*/.":
        button_click(key)
    elif key == '\r':
        button_equal()
    elif key == '\x08':
        button_clear()
buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3),
]
for (text,row,col) in buttons:
    if text == "=":
        button = tk.Button(window,text=text,font=("Arial",20),foreground="White",background="#323232",command=button_equal)
    else:
        button = tk.Button(window,text=text,font=("Arial",20),foreground="White",background="#323232",command=lambda t=text: button_click(t))
    button.grid(row=row,column=col,padx=5,pady=5,sticky="nsew")
clear_button = tk.Button(window,text="C",font=("Arial",20),foreground="White",background="#323232",command=button_clear)
clear_button.grid(row=5,column=0,columnspan=4,padx=5,pady=5,sticky="nsew")
for i in range(6):
    window.grid_rowconfigure(i,weight=1)
for i in range(4):
    window.grid_columnconfigure(i,weight=1)
window.bind("<Key>",handle_key)
window.mainloop()
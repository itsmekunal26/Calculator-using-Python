import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Create a function to handle button click
def click(val): 
    e = entry.get()  # getting the value 
    ans = " " 
 
    try: 
        # To clear the last inserted text 
        if val == "C": 
            e = e[0:len(e) - 1]  # deleting the last entered value 
            entry.delete(0, "end") 
            entry.insert(0, e) 
            return 
 
        elif val == "=": 
            ans = eval(e) 
 
        else: 
            entry.insert("end", val) 
            return 
 
        entry.delete(0, "end") 
        entry.insert(0, ans) 
 
    except SyntaxError: 
        pass 

# Create the main window
ent = tk.Tk()

# Create an entry widget for the calculator display
entry = tk.Entry(ent, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

b7=tk.Button(ent,text="    C   ",width=4,height=1).place(x=30,y=50)
b8=tk.Button(ent,text="    -   ").place(x=90,y=50)
b9=tk.Button(ent,text="    *   ").place(x=150,y=50)

b4=tk.Button(ent,text="    7   ",command=lambda:button_click(7)).place(x=30,y=90)
b5=tk.Button(ent,text="    8   ",command=lambda:button_click(8)).place(x=90,y=90)
b6=tk.Button(ent,text="    9   ",command=lambda:button_click(9)).place(x=150,y=90) 


b1=tk.Button(ent,text="    4   ",command=lambda:button_click(4)).place(x=30,y=130)
b2=tk.Button(ent,text="    5   ",command=lambda:button_click(5)).place(x=90,y=130)
b3=tk.Button(ent,text="    6   ",command=lambda:button_click(6)).place(x=150,y=130)

be=tk.Button(ent,text="    1   ",command=lambda:button_click(1)).place(x=30,y=170)
bf=tk.Button(ent,text="    2   ",command=lambda:button_click(2)).place(x=90,y=170)
bg=tk.Button(ent,text="    3   ",command=lambda:button_click(3)).place(x=150,y=170)

b0=tk.Button(ent,text="        0      ",command=lambda:button_click(0),width=12).place(x=30,y=210)
bd=tk.Button(ent,text="    .    ").place(x=150,y=210)

ba=tk.Button(ent,text="    /    ",width=5,height=1).place(x=200,y=50)
bb=tk.Button(ent,text="    +    ",height=4,width=5).place(x=200,y=90)
bc=tk.Button(ent,text="    =    ",height=4,width=5).place(x=200,y=170)
ent.config(bg="black")
ent.geometry("250x250")
ent.title("Normal Calculator")

ent.mainloop()

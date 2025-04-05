# Import Module  
from tkinter import * 

# Create Object  
root = Tk()  
root.title("Contact Book")  

# Set geometry  
root.geometry('400x500')  

# Information List  
datas = []  

# Add Information  
def add():  
    global datas  
    if Name.get() and Number.get() and address.get(1.0, "end-1c").strip():  
        datas.append([Name.get(), Number.get(), address.get(1.0, "end-1c")])  
        update_book()  
        reset()  

# View Information  
def view():  
    if select.curselection():  
        index = int(select.curselection()[0])  
        Name.set(datas[index][0])  
        Number.set(datas[index][1])  
        address.delete(1.0, "end")  
        address.insert(1.0, datas[index][2])  

# Delete Information  
def delete():  
    if select.curselection():  
        del datas[int(select.curselection()[0])]  
        update_book()  
        reset()  

# Reset Fields  
def reset():  
    Name.set('')  
    Number.set('')  
    address.delete(1.0, "end")  

# Update ListBox  
def update_book():  
    select.delete(0, END)  
    for n, p, a in datas:  
        select.insert(END, n)  

# Create StringVars  
Name = StringVar()  
Number = StringVar()  

# Frames  
frame = Frame(root)  
frame.pack(pady=10)  

frame1 = Frame(root)  
frame1.pack()  

frame2 = Frame(root)  
frame2.pack(pady=10)  

# Name Field  
Label(frame, text="Name", font='arial 12 bold').pack(side=LEFT, padx=5)  
Entry(frame, textvariable=Name, width=30).pack()  

# Phone Field  
Label(frame1, text="Phone No.", font='arial 12 bold').pack(side=LEFT, padx=5)  
Entry(frame1, textvariable=Number, width=30).pack()  

# Address Field  
Label(frame2, text="Address", font='arial 12 bold').pack(side=LEFT, padx=5)  
address = Text(frame2, width=30, height=5)  
address.pack()  

# Buttons  
Button(root, text="Add", font="arial 12 bold", command=add).place(x=50, y=270)  
Button(root, text="View", font="arial 12 bold", command=view).place(x=150, y=270)  
Button(root, text="Delete", font="arial 12 bold", command=delete).place(x=250, y=270)  
Button(root, text="Reset", font="arial 12 bold", command=reset).place(x=150, y=310)  

# Scrollbar & Listbox  
scroll_bar = Scrollbar(root, orient=VERTICAL)  
select = Listbox(root, yscrollcommand=scroll_bar.set, height=10)  
scroll_bar.config(command=select.yview)  

select.pack(pady=10)  
scroll_bar.pack(side=RIGHT, fill=Y)  

# Run Application  
root.mainloop()

# Importing required packages
from tkinter import *
import tkinter.messagebox

# Creating the initial window
window = Tk()
window.title("To-Do List App")

# Frame widget to hold the listbox and the scrollbar
frame_task = Frame(window)
frame_task.pack()

# To hold items in a listbox
listbox_task = Listbox(frame_task, bg="white", fg="black", height=15, width=50, font=("Helvetica", 12))
listbox_task.pack(side=LEFT)

# Scrollbar for the listbox
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Function to add a task
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(END, task)
        entry_task.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")

# Function to delete a task
def delete_task():
    selected = listbox_task.curselection()
    if len(selected) > 0:
        listbox_task.delete(selected[0])
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="No task selected")

# Function to mark a task as completed
def mark_completed():
    selected = listbox_task.curselection()
    if len(selected) > 0:
        task = listbox_task.get(selected[0])
        completed_task = task + " ✔"
        listbox_task.delete(selected[0])
        listbox_task.insert(listbox_task.size(), completed_task)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="No task selected")

# Entry widget to take input
entry_task = Entry(window, width=40, borderwidth=3)
entry_task.pack(pady=10)

# Button widgets
add_button = Button(window, text="Add Task", width=10, command=add_task)
add_button.pack(pady=3)

delete_button = Button(window, text="Delete Task", width=10, command=delete_task)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark Completed", width=15, command=mark_completed)
mark_button.pack(pady=3)

# Running the mainloop
window.mainloop()
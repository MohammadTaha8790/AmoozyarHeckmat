import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("هشدار", "لطفاً یک وظیفه وارد کنید!")

app = tk.Tk()
app.title("مدیریت وظایف")
app.geometry("400x500")

entry = tk.Entry(app, width=40)
entry.pack(pady=10)

add_btn = tk.Button(app, text="افزودن وظیفه", command=add_task)
add_btn.pack()

listbox = tk.Listbox(app, width=40, height=15)
listbox.pack(pady=10)

app.mainloop()
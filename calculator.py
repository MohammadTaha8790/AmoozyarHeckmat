import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == "جمع":
            result = num1 + num2
        elif operation == "تفریق":
            result = num1 - num2
        elif operation == "ضرب":
            result = num1 * num2
        elif operation == "تقسیم":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("خطا", "تقسیم بر صفر ممکن نیست!")
                return
        else:
            messagebox.showerror("خطا", "عملیات نامعتبر!")
            return
        
        messagebox.showinfo("نتیجه", f"نتیجه: {result}")
    except ValueError:
        messagebox.showerror("خطا", "لطفاً عدد معتبر وارد کنید!")

# ساخت پنجره اصلی
window = tk.Tk()
window.title("ماشین حساب زیبا")

# ویجت‌ها
tk.Label(window, text="عدد اول:").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="عدد دوم:").pack()
entry2 = tk.Entry(window)
entry2.pack()

tk.Label(window, text="عملیات:").pack()
operation_var = tk.StringVar(value="جمع")
operations = ["جمع", "تفریق", "ضرب", "تقسیم"]
tk.OptionMenu(window, operation_var, *operations).pack()

tk.Button(window, text="محاسبه", command=calculate).pack()

# اجرای پنجره
window.mainloop()
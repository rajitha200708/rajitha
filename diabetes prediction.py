import tkinter as tk
from tkinter import messagebox

def check_diabetes():
    try:
        if int(age.get()) > 45 and float(bmi.get()) > 25 and float(glucose.get()) > 140 or family_history.get()=="yes":
            messagebox.showinfo("Result", "You might be at risk of diabetes.")
        else:
            messagebox.showinfo("Result", "You are likely not at risk of diabetes.")
    except:
        messagebox.showerror("Error", "Invalid input.")

root = tk.Tk()
tk.Label(root, text="Age:").pack(); age = tk.Entry(root); age.pack()
tk.Label(root, text="BMI:").pack(); bmi = tk.Entry(root); bmi.pack()
tk.Label(root, text="Glucose:").pack(); glucose = tk.Entry(root); glucose.pack()
tk.Label(root, text="Family History:").pack()
family_history=tk.StringVar(value="no")
tk.Radiobutton(root,text="yes",
variable=family_history, value="yes").pack()
tk.Radiobutton(root, text="no",
variable=family_history, value="no").pack()
tk.Button(root, text="Check", command=check_diabetes).pack()
root.mainloop()

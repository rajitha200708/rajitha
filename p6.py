import tkinter as tk
from tkinter import ttk, messagebox
import datetime

def add_item():
    t = int(qty.get()) * float(price.get())
    tree.insert("", "end", values=(name.get(), qty.get(), price.get(), t))
    total.set(total.get() + t)
    name.delete(0, tk.END), qty.delete(0, tk.END), price.delete(0, tk.END)

def generate_bill():
    messagebox.showinfo("Bill", f"Store: D MART\nCustomer: {cust.get()}\nTime: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}\nTotal: ${total.get():.2f}")

root = tk.Tk()
root.configure(bg='black')  # Set background color to black

tk.Label(root, text="D MART", font=("Arial", 16, "bold"), fg='white', bg='black').grid(row=0, column=0, columnspan=4)

cust, name, qty, price, total = tk.Entry(root), tk.Entry(root), tk.Entry(root, width=5), tk.Entry(root, width=10), tk.DoubleVar()
for i, (t, e) in enumerate([("Customer", cust), ("Product", name), ("Qty", qty), ("Price", price)]): 
    tk.Label(root, text=t, fg='white', bg='black').grid(row=i//2+1, column=i%2*2); e.grid(row=i//2+1, column=i%2*2+1)
tk.Button(root, text="Add", command=add_item, bg='gray', fg='white').grid(row=2, column=4)

tree = ttk.Treeview(root, columns=("Name", "Qty", "Price", "Total"), show="headings", height=5)
for c in ("Name", "Qty", "Price", "Total"): tree.heading(c, text=c)
tree.grid(row=3, column=0, columnspan=5)

tk.Label(root, text="Total: $", fg='white', bg='black').grid(row=4, column=2)
tk.Label(root, textvariable=total, fg='white', bg='black').grid(row=4, column=3)
tk.Button(root, text="Bill", command=generate_bill, bg='gray', fg='white').grid(row=5, column=2)

root.mainloop()

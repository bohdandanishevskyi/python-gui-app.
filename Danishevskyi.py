import tkinter as tk
from tkinter import ttk, messagebox
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def generate_numbers():
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError
    except Exception:
        messagebox.showerror("Chyba", "N musí byť celé kladné číslo")
        return

    try:
        a = float(entry_a.get())
    except Exception:
        messagebox.showerror("Chyba", "A musí byť číslo (float)")
        return

    nums = [random.random() for _ in range(n)]

    s = sum(nums)
    prod = 1.0
    for v in nums:
        prod *= v

    adjusted = [v + a for v in nums]

    label_count.config(text=str(n))
    label_sum.config(text=f"{s:.6g}")
    label_prod.config(text=f"{prod:.6g}")

    ax.clear()
    ax.plot(range(1, n + 1), adjusted, marker="o")
    ax.set_title("Upravené hodnoty (po pridaní A)")
    ax.set_xlabel("Index")
    ax.set_ylabel("Hodnota")
    ax.grid(True)
    canvas.draw()


root = tk.Tk()
root.title("Generátor náhodných čísel")
root.resizable(False, False)

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

ttk.Label(frame, text="N (počet):").grid(row=0, column=0)
entry_n = ttk.Entry(frame, width=10)
entry_n.insert(0, "10")
entry_n.grid(row=0, column=1)

ttk.Label(frame, text="A (prirátať):").grid(row=0, column=2)
entry_a = ttk.Entry(frame, width=10)
entry_a.insert(0, "0.5")
entry_a.grid(row=0, column=3)

ttk.Button(frame, text="Nové čísla", command=generate_numbers).grid(row=0, column=4, padx=10)

lf = ttk.Frame(root, padding=10)
lf.grid(row=1, column=0)

ttk.Label(lf, text="Počet (N):").grid(row=0, column=0)
label_count = ttk.Label(lf, text="0")
label_count.grid(row=0, column=1, padx=10)

ttk.Label(lf, text="Súčet:").grid(row=0, column=2)
label_sum = ttk.Label(lf, text="0")
label_sum.grid(row=0, column=3, padx=10)

ttk.Label(lf, text="Súčin:").grid(row=0, column=4)
label_prod = ttk.Label(lf, text="0")
label_prod.grid(row=0, column=5)

fig = Figure(figsize=(6, 3))
ax = fig.add_subplot(111)
ax.set_title("Upravené hodnoty (po pridaní A)")
ax.set_xlabel("Index")
ax.set_ylabel("Hodnota")

canvas = FigureCanvasTkAgg(fig, master=root)
fig.tight_layout()
canvas.get_tk_widget().grid(row=2, column=0, padx=10, pady=10)

root.mainloop()

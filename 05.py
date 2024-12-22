import tkinter as tk
from tkinter import ttk, messagebox
import random

def generate_random_number():
    try:
        min_value = min_entry.get()
        max_value = max_entry.get()

        if not min_value or not max_value:
            raise ValueError("Поля не должны быть пустыми")

        min_value = int(min_value)
        max_value = int(max_value)

        if min_value > max_value:
            raise ValueError("Минимальное значение должно быть меньше или равно максимальному")

        random_number = random.randint(min_value, max_value)
        result_label.config(text=f"Случайное число: {random_number}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

root = tk.Tk()
root.title("Генератор случайных чисел")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

min_label = ttk.Label(frame, text="Минимальное значение:")
min_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
min_entry = ttk.Entry(frame, width=15)
min_entry.grid(row=0, column=1, padx=5, pady=5)

max_label = ttk.Label(frame, text="Максимальное значение:")
max_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
max_entry = ttk.Entry(frame, width=15)
max_entry.grid(row=1, column=1, padx=5, pady=5)

generate_button = ttk.Button(frame, text="Сгенерировать", command=generate_random_number)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=1, column=0, pady=10)

root.mainloop()

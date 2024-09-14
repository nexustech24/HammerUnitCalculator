import tkinter as tk
from tkinter import ttk

HAMMER_TO_INCHES = 0.75
INCHES_TO_HAMMER = 1 / HAMMER_TO_INCHES
HAMMER_TO_MM = 19.05
MM_TO_HAMMER = 1 / HAMMER_TO_MM

def convert_to_hammer_inch():
    try:
        real_units = float(entry_real_units.get())
        hammer_units = real_units * INCHES_TO_HAMMER
        label_result.config(text=f"{real_units} inches = {hammer_units:.2f} Hammer Units")
    except ValueError:
        label_result.config(text="Invalid input!")

def convert_to_hammer_mm():
    try:
        real_units = float(entry_real_units.get())
        hammer_units = real_units * MM_TO_HAMMER
        label_result.config(text=f"{real_units} mm = {hammer_units:.2f} Hammer Units")
    except ValueError:
        label_result.config(text="Invalid input!")

def convert_to_real_inch():
    try:
        hammer_units = float(entry_hammer_units.get())
        real_units = hammer_units * HAMMER_TO_INCHES
        label_result.config(text=f"{hammer_units} Hammer Units = {real_units:.2f} inches")
    except ValueError:
        label_result.config(text="Invalid input!")

def convert_to_real_mm():
    try:
        hammer_units = float(entry_hammer_units.get())
        real_units = hammer_units * HAMMER_TO_MM
        label_result.config(text=f"{hammer_units} Hammer Units = {real_units:.2f} mm")
    except ValueError:
        label_result.config(text="Invalid input!")

window = tk.Tk()
window.title("Hammer Units Converter")

label_real_units = ttk.Label(window, text="Enter real-world units (inches/mm):")
label_real_units.grid(row=0, column=0, padx=10, pady=10)

entry_real_units = ttk.Entry(window)
entry_real_units.grid(row=0, column=1, padx=10, pady=10)

btn_to_hammer_inch = ttk.Button(window, text="Convert to Hammer Units (Inches)", command=convert_to_hammer_inch)
btn_to_hammer_inch.grid(row=0, column=2, padx=10, pady=10)

btn_to_hammer_mm = ttk.Button(window, text="Convert to Hammer Units (mm)", command=convert_to_hammer_mm)
btn_to_hammer_mm.grid(row=0, column=3, padx=10, pady=10)

label_hammer_units = ttk.Label(window, text="Enter Hammer Units:")
label_hammer_units.grid(row=1, column=0, padx=10, pady=10)

entry_hammer_units = ttk.Entry(window)
entry_hammer_units.grid(row=1, column=1, padx=10, pady=10)

btn_to_real_inch = ttk.Button(window, text="Convert to Real Units (Inches)", command=convert_to_real_inch)
btn_to_real_inch.grid(row=1, column=2, padx=10, pady=10)

btn_to_real_mm = ttk.Button(window, text="Convert to Real Units (mm)", command=convert_to_real_mm)
btn_to_real_mm.grid(row=1, column=3, padx=10, pady=10)

label_result = ttk.Label(window, text="Result will be shown here")
label_result.grid(row=2, column=0, columnspan=4, padx=10, pady=20)

window.mainloop()

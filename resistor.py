import tkinter as tk
from tkinter import ttk

# Color Code Dictionaries
digit_colors = {
    'Black': 0, 'Brown': 1, 'Red': 2, 'Orange': 3,
    'Yellow': 4, 'Green': 5, 'Blue': 6, 'Violet': 7,
    'Grey': 8, 'White': 9
}

multiplier_colors = {
    'Black': 1, 'Brown': 10, 'Red': 100, 'Orange': 1_000,
    'Yellow': 10_000, 'Green': 100_000, 'Blue': 1_000_000,
    'Gold': 0.1, 'Silver': 0.01
}

tolerance_colors = {
    'Brown': '±1%', 'Red': '±2%', 'Gold': '±5%', 'Silver': '±10%', 'None': '±20%'
}

# Color Lists
digit_list = list(digit_colors.keys())
multiplier_list = list(multiplier_colors.keys())
tolerance_list = list(tolerance_colors.keys())

def calculate_resistance():
    band1 = band1_var.get()
    band2 = band2_var.get()
    band3 = band3_var.get()
    band4 = band4_var.get()

    if band1 and band2 and band3 and band4:
        first_digit = digit_colors[band1]
        second_digit = digit_colors[band2]
        multiplier = multiplier_colors[band3]
        tolerance = tolerance_colors[band4]

        resistance_value = (first_digit * 10 + second_digit) * multiplier

        # Format resistance nicely
        if resistance_value >= 1_000_000:
            display_value = f"{resistance_value / 1_000_000:.2f} MΩ"
        elif resistance_value >= 1_000:
            display_value = f"{resistance_value / 1_000:.2f} kΩ"
        else:
            display_value = f"{resistance_value:.2f} Ω"

        result_label.config(text=f"Resistance: {display_value} {tolerance}")
    else:
        result_label.config(text="Please select all bands.")

# GUI Setup
root = tk.Tk()
root.title("Resistor Color Code Calculator")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="4-Band Resistor Color Code", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

# Dropdowns
band1_var = tk.StringVar()
band2_var = tk.StringVar()
band3_var = tk.StringVar()
band4_var = tk.StringVar()

ttk.Label(frame, text="Band 1").grid(row=0, column=0, padx=5, pady=5)
ttk.OptionMenu(frame, band1_var, '', *digit_list).grid(row=1, column=0)

ttk.Label(frame, text="Band 2").grid(row=0, column=1, padx=5, pady=5)
ttk.OptionMenu(frame, band2_var, '', *digit_list).grid(row=1, column=1)

ttk.Label(frame, text="Multiplier").grid(row=0, column=2, padx=5, pady=5)
ttk.OptionMenu(frame, band3_var, '', *multiplier_list).grid(row=1, column=2)

ttk.Label(frame, text="Tolerance").grid(row=0, column=3, padx=5, pady=5)
ttk.OptionMenu(frame, band4_var, '', *tolerance_list).grid(row=1, column=3)

# Calculate Button
tk.Button(root, text="Calculate", command=calculate_resistance, bg="lightblue").pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Import backend functions
from backend import calculate_bmi, health_risk


# Create main window
root = tk.Tk()
root.title("BMI & Health Risk Calculator")
root.geometry("400x500")
root.config(bg="#d0f0ff")


# Title
title = tk.Label(
    root,
    text="BMI & Health Risk Calculator",
    font=("Arial", 16, "bold"),
    bg="#d0f0ff"
)
title.pack(pady=10)


# Name
tk.Label(root, text="Name:", bg="#d0f0ff").pack()

name_entry = tk.Entry(root)
name_entry.pack()


# Age
tk.Label(root, text="Age:", bg="#d0f0ff").pack()

age_entry = tk.Entry(root)
age_entry.pack()


# Height
tk.Label(root, text="Height (cm):", bg="#d0f0ff").pack()

height_entry = tk.Entry(root)
height_entry.pack()


# Weight
tk.Label(root, text="Weight (kg):", bg="#d0f0ff").pack()

weight_entry = tk.Entry(root)
weight_entry.pack()


# Gender
tk.Label(root, text="Gender:", bg="#d0f0ff").pack()

gender_var = tk.StringVar(value="Male")

tk.Radiobutton(
    root,
    text="Male",
    variable=gender_var,
    value="Male",
    bg="#d0f0ff"
).pack()

tk.Radiobutton(
    root,
    text="Female",
    variable=gender_var,
    value="Female",
    bg="#d0f0ff"
).pack()


# Result Labels
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#d0f0ff"
)
result_label.pack(pady=10)


risk_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#d0f0ff"
)
risk_label.pack(pady=5)


# Calculate Function
def calculate():

    try:
        name = name_entry.get()
        age = int(age_entry.get())
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        gender = gender_var.get()

        # Calculate BMI
        bmi = calculate_bmi(height, weight)

        category, risk = health_risk(bmi)

        # Display Results
        result_label.config(
            text=f"{name}, Your BMI is: {bmi}"
        )

        risk_label.config(
            text=f"Category: {category}\nHealth Risk: {risk}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values."
        )


# Calculate Button
tk.Button(
    root,
    text="Calculate BMI",
    command=calculate,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white"
).pack(pady=15)


# Exit Button
tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    font=("Arial", 12),
    bg="red",
    fg="white"
).pack()


# Run GUI
root.mainloop()
# backend.py

def calculate_bmi(height, weight):
    """
    Calculate BMI using height (cm) and weight (kg)
    """
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def health_risk(bmi):
    """
    Determine health risk based on BMI
    """

    if bmi < 18.5:
        return "Underweight", "Malnutrition Risk"

    elif 18.5 <= bmi < 25:
        return "Normal Weight", "Low Risk"

    elif 25 <= bmi < 30:
        return "Overweight", "Enhanced Risk"

    elif 30 <= bmi < 35:
        return "Moderately Obese", "Medium Risk"

    elif 35 <= bmi < 40:
        return "Severely Obese", "High Risk"

    else:
        return "Very Severely Obese", "Very High Risk"

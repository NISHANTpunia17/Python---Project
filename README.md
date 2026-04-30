# Python---Project
BMI & Health Risk Calculator 🧮

📌 Project Overview

The BMI & Health Risk Calculator is a Python-based desktop application that calculates a user's Body Mass Index (BMI) and determines their health risk category based on BMI values.

The project uses:

- Python for logic and calculations
- Tkinter for graphical user interface (GUI)
- A backend module for BMI calculations and health risk evaluation

---

🎯 Features

- User-friendly graphical interface
- Input fields for:
  - Name
  - Age
  - Height (cm)
  - Weight (kg)
  - Gender
- Calculates BMI instantly
- Displays:
  - BMI value
  - BMI category
  - Health risk level
- Error handling for invalid inputs
- Exit button to close application

---

🧠 BMI Formula Used

BMI is calculated using the formula:

BMI = Weight (kg) / Height (m²)

Where:

- Height is converted from cm to meters
- BMI result is rounded to 2 decimal places

---

📂 Project Structure

BMI-Calculator/
│
├── backend.py      # Contains BMI calculation logic
├── main.py         # GUI application using Tkinter
├── README.md       # Project documentation

---

⚙️ Requirements

Make sure Python is installed on your system.

Required Library:

tkinter

Tkinter comes pre-installed with most Python versions.

To check Python version:

python --version

---

▶️ How to Run the Project

1. Download or clone the repository

git clone https://github.com/your-username/bmi-calculator.git

2. Navigate to project folder

cd bmi-calculator

3. Run the program

python main.py

---

🧮 BMI Categories & Health Risk

BMI Range| Category| Health Risk
< 18.5| Underweight| Malnutrition Risk
18.5 – 24.9| Normal Weight| Low Risk
25 – 29.9| Overweight| Enhanced Risk
30 – 34.9| Moderately Obese| Medium Risk
35 – 39.9| Severely Obese| High Risk
≥ 40| Very Severely Obese| Very High Risk

---

🧩 Backend Module Functions

"calculate_bmi(height, weight)"

Calculates BMI using height and weight.

Parameters:

- height → float (cm)
- weight → float (kg)

Returns:

- BMI value (rounded to 2 decimal places)

---

"health_risk(bmi)"

Determines BMI category and health risk.

Parameter:

- bmi → float

Returns:

- BMI category
- Health risk level

---

🖥️ GUI Components

The graphical interface includes:

- Labels
- Entry fields
- Radio buttons
- Buttons
- Result display section

Built using Tkinter.

---

❗ Error Handling

If invalid inputs are entered (like letters instead of numbers), the program shows:

Invalid Input
Please enter valid numeric values.

---

📌 Example Output

Name: Nishant
Age: 20
Height: 170 cm
Weight: 65 kg

Output:
Nishant, Your BMI is: 22.49
Category: Normal Weight
Health Risk: Low Risk

---

🚀 Future Improvements

Possible enhancements:

- Save BMI history
- Add charts or graphs
- Add unit conversion (feet/inches)
- Export results to file
- Add login system

---
---

import tkinter as tk
from tkinter import messagebox
import requests

def calculate_bmi():
    weight = weight_entry.get()
    height = height_entry.get()

    try:
        weight = float(weight)
        height = float(height) / 100  

        url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/metric"
        headers = {
            "X-RapidAPI-Key": "86af8e5970msh6f9b43afedd10d1p13756djsn0e3a758ea4fe", 
            "X-RapidAPI-Host": "body-mass-index-bmi-calculator.p.rapidapi.com"
        }
        querystring = {"weight": weight, "height": height}

        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            bmi_data = response.json()
            bmi_value = bmi_data["bmi"]
            bmi_result.config(text=f"Your BMI is: {bmi_value:.2f}")
            if bmi_value < 18.5:
                category = "Under Weight"
            elif 18.5 <= bmi_value < 25:
                category = "Normal weight"
            elif 25 <= bmi_value < 30:
                category = "Overweight"
            else:
               category = "Obese"

            bmi_category.config(text=f"Category: {category}")

            categories = ["Under Weight", "Normal weight", "Overweight", "Obese"]
            sizes = [bmi_data[c] for c in categories]
            explode = (0.1, 0, 0, 0)

            plt.figure(figsize=(6, 6))
            plt.pie(sizes, explode=explode, labels=categories, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            plt.title('BMI Categories')
            plt.show()
        else:
            messagebox.showerror("Error", "Failed to calculate BMI. Please try again.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for weight and height.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Failed to connect to the BMI calculator API.")

root = tk.Tk()
root.title("BMI Calculator")

entry_style = {"width": 10, "font": ("Arial", 12)}
button_style = {"width": 15, "font": ("Arial", 12)}
result_style = {"font": ("Arial", 14, "bold")}

weight_label = tk.Label(root, text="Weight (kg):", **result_style)
weight_label.grid(row=0, column=0, padx=10, pady=5)

weight_entry = tk.Entry(root, **entry_style)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="Height (cm):", **result_style)
height_label.grid(row=1, column=0, padx=10, pady=5)

height_entry = tk.Entry(root, **entry_style)
height_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, **button_style)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

bmi_result = tk.Label(root, text="", **result_style)
bmi_result.grid(row=3, columnspan=2, padx=10, pady=5)

bmi_category = tk.Label(root, text="")
bmi_category.grid(row=4, columnspan=2, padx=10, pady=5)

root.mainloop()

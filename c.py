import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculate():
    operation = operation_var.get()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if operation == "add":
        result_var.set(add(num1, num2))
    elif operation == "subtract":
        result_var.set(subtract(num1, num2))
    elif operation == "multiply":
        result_var.set(multiply(num1, num2))
    elif operation == "divide":
        result_var.set(divide(num1, num2))
    else:
        result_var.set("Invalid operation")

# Create the main window
root = tk.Tk()
root.title("Stylish Calculator")

# Create a frame for styling
frame = tk.Frame(root, bg="#e1e1e1", padx=20, pady=20)
frame.pack(padx=20, pady=20)

# Entry widgets for user input
entry_num1 = tk.Entry(frame, font=("Helvetica", 14), bd=0, relief="flat")
entry_num1.pack(fill=tk.X, pady=10)

entry_num2 = tk.Entry(frame, font=("Helvetica", 14), bd=0, relief="flat")
entry_num2.pack(fill=tk.X, pady=10)

# Dropdown menu for selecting operation
operation_var = tk.StringVar(root)
operation_choices = ["add", "subtract", "multiply", "divide"]
operation_var.set(operation_choices[0])

operation_label = tk.Label(frame, text="Select Operation:", font=("Helvetica", 14), bg="#e1e1e1")
operation_label.pack(anchor=tk.W)

operation_menu = tk.OptionMenu(frame, operation_var, *operation_choices)
operation_menu.config(font=("Helvetica", 14), bd=0, relief="flat")
operation_menu.pack(fill=tk.X, pady=10)

# Button to perform calculation
calculate_button = tk.Button(frame, text="Calculate", font=("Helvetica", 14), command=calculate, bd=0, relief="flat", bg="#3498db", fg="white")
calculate_button.pack()

# Label to display the result
result_var = tk.StringVar(root)
result_label = tk.Label(frame, textvariable=result_var, font=("Helvetica", 18, "bold"), bg="#e1e1e1")
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()

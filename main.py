#!/usr/bin/env python3
import tkinter as tk
from itertools import product


def generate_truth_table(logical_expression, variables):
    headers = variables + ['Result']
    rows = list(product([False, True], repeat=len(variables)))

    truth_table = []
    for row in rows:
        result = evaluate_expression(logical_expression, variables, row)
        truth_table.append(row + (result,))

    return headers, truth_table


def evaluate_expression(logical_expression, variables, row):
    variables_dict = dict(zip(variables, row))
    print(variables_dict)
    return eval(logical_expression, variables_dict)


def update_table():
    logical_expression = logical_expression_entry.get()
    variables = variables_entry.get().replace(" ", "").split(',')

    header, table = generate_truth_table(logical_expression, variables)

    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, '\t'.join(header) + '\n')
    for row in table:
        result_text.insert(tk.END, '\t'.join(map(str, row)) + '\n')
    result_text.config(state=tk.DISABLED)


# GUI setup
root = tk.Tk()
root.title("Truth Table Generator")

# Entry for logical expression input
logical_expression_label = tk.Label(root, text="Enter logical expression:")
logical_expression_label.pack()
logical_expression_entry = tk.Entry(root)
logical_expression_entry.pack()

# Entry for variable input
variables_label = tk.Label(root, text="Enter variables (comma-separated):")
variables_label.pack()
variables_entry = tk.Entry(root)
variables_entry.pack()

# Button to generate truth table
generate_button = tk.Button(root, text="Generate Truth Table", command=update_table)
generate_button.pack()

# Text widget to display the truth table
result_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
result_text.pack()

root.mainloop()

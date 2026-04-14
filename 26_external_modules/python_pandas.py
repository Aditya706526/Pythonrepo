import pandas as pd
import numpy as np
import openpyxl

file1 = r"C:\Users\asharm99\Downloads\employees.csv"
employees = pd.read_csv(file1)
print(employees)
print(employees.shape)
print(employees.columns)
print(employees.head(3))
print("----------------------------------------")

file2 = r"C:\Users\asharm99\Downloads\sales.csv"
sales = pd.read_csv(file2)
print(sales)
print(sales.shape)
print(sales.columns)
print(sales.head(3))
print("----------------------------------------")

file3 = r"C:\Users\asharm99\Downloads\practice_data.xlsx"
practice_data = pd.read_excel(file3)
print(practice_data)
print(practice_data.shape)
print(practice_data.columns)
print(practice_data.head(3))


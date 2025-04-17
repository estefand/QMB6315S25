# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name: Estefan Duran
#
# Date: April 13, 2025
#
##################################################
#
# Sample Script for Assignment 2:
# Manipulating Data
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

import os
import pandas as pd
import openpyxl
import airplane_data

# Import a module for estimating regression models.
import statsmodels.formula.api as sm # Another way to estimate linear regression
# This is a "light duty" modeling package designed to mimic the interface in R.


print(os.getcwd())        # Get current working directory
print(os.listdir())       # List files in current directory
# os.chdir("path/to/folder")  # Change working directory



##################################################
# Set up Workspace
##################################################


# Find out the current directory.
os.getcwd()

'C:\\Users\\estef\\OneDrive\\Desktop\\2025 Spring Semester\\Python\\assignment_02'


# Load the Excel file into a variable
airplane_data = pd.read_excel("airplane_data", sheet_name="airplane_sales_specs")
print(airplane_data)

# Relative path (if file is inside 'assignment 02' folder)
df = pd.read_excel("assignment 02/airplane data.xlsx")

# Or absolute path (example for Windows)
df = pd.read_excel("C:/Users/YourName/Documents/assignment 02/airplane data.xlsx")


print(os.getcwd())


# Get the path where you saved this script.
# This only works when you run the entire script (with the green "Play" button or F5 key).
print(os.path.dirname(os.path.realpath(__file__)))
# It might be comverted to lower case, but it gives you an idea of the text of the path. 
# You could copy it directly or type it yourself, using your spelling conventions. 

# Change to a new directory.

# You could set it directly from the location of this file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Check that the change was successful.
os.getcwd()


# I got lower case output, even though my folders have some upper case letters.
# But anyway, it works.


##################################################
# Part a) Read Spreadsheet and Sales Data
##################################################


print("=== Airplane Sales ===")

print(airplane_data.describe())


#--------------------------------------------------
# Fit a regression model.
#--------------------------------------------------

X1 = sm.add_constant(airplane_data["age"])
y1 = airplane_data["price"]
reg_model_sales = sm.OLS(y1, X1).fit()

print("\n=== Regression Output (price ~ age) ===")
print(reg_model_sales.summary())


##################################################
# Part b) Read Specification Data
##################################################

airplane_specs = pd.read_excel("airplane data.xlsx", sheet_name="airplane specs")

#--------------------------------------------------
# Join the two datasets together.
#--------------------------------------------------

airplane_sales_specs = pd.concat([airplane_data, airplane_specs], axis=1)


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

print("\n=== Summary of Sales + Specs ===")
print(airplane_specs.describe())

# d) Regression: price ~ age + pass + wtop + fixgear + tdrag
X2 = airplane_sales_specs[["age", "pass", "wtop", "fixgear", "tdrag"]]
X2 = sm.add_constant(X2)
y2 = airplane_sales_specs["price"]
reg_model_sales_specs = sm.OLS(y2, X2).fit()

print("\n=== Regression Output (price ~ age + pass + wtop + fixgear + tdrag) ===")
print(reg_model_sales_specs.summary())


##################################################
# Part c) Read Performance Data
##################################################

print("\n=== Summary of Full Dataset ===")
print(airplane_data.describe())

#--------------------------------------------------
# Join the third dataset to the first two.
#--------------------------------------------------

X3 = airplane_data[["age", "pass", "wtop", "fixgear", "tdrag", "horse", "fuel", "ceiling", "cruise"]]
X3 = sm.add_constant(X3)
y3 = airplane_data["price"]
reg_model_full = sm.OLS(y3, X3).fit()


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

print("\n=== Regression Output (Full Model) ===")
print(reg_model_full.summary())

##################################################
# End
##################################################

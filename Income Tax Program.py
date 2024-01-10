import pandas as pd

def welcome():
    print("Hello, this is income and tax calculation program")

def input_data():
    fname = input("Please enter your first name: ")
    lname = input("Please enter your lname: ")
    global full_name
    full_name = fname + " " + lname
    print ("Full Name:", full_name)
    global working_hours
    working_hours = float(input("Please enter the number of working hours: "))
    print ("Number of hours working: ", working_hours)
    global hourly_rate
    hourly_rate = float(input("Please enter the hourly rate: "))
    print ("Hourly rate: ", hourly_rate)
    global income_tax_deduction_rate
    income_tax_deduction_rate = 20
    print("Income tax deduction rate: ", income_tax_deduction_rate, "%")
    global superannuation_deduction_rate
    superannuation_deduction_rate = 10
    print("Superannuation deduction rate: ", superannuation_deduction_rate, "%")
    

def assign_input_data():
    fname_list.append(full_name)
    working_hours_list.append(working_hours)
    hourly_rate_list.append(hourly_rate)

def calculation():
    global income
    income = working_hours * hourly_rate
    global income_tax_deduction
    income_tax_deduction = income * income_tax_deduction_rate/100
    global superannuation_deduction 
    superannuation_deduction = income * superannuation_deduction_rate/100


def assign_calculation_data():
    income_list.append(income)
    income_tax_deduction_list.append(income_tax_deduction)
    superannuation_deduction_list.append(superannuation_deduction)
    

def output_data():
    employee_input = pd.DataFrame()
    employee_input = employee_input.assign(
        Employee_Name = fname_list,
        Hours_Worked = working_hours_list,
        Hourly_Rate = hourly_rate_list,
    )
    output_calculation = pd.DataFrame()
    output_calculation = output_calculation.assign(
        Employee_Name = fname_list,
        Income = income_list,
        Income_Tax_Deduction = income_tax_deduction_list,
        Superannuation_Deduction = superannuation_deduction_list
    )
    print(employee_input)
    print(output_calculation)
    answer = None
    
def end_program():
    output_data()
    print("End program. Thank you!") 

def run_program():
    input_data()
    assign_input_data()
    calculation()
    assign_calculation_data()
    output_data()
    ask_continue()

def ask_continue():
    answer = None
    while answer not in ("Y", "N", "Yes", "No"):
        answer = input("Would you to like to co (Y/N) \n")
        if answer == "Y" or answer == "y":
            answer = None
            return run_program()
        if answer == "N" or answer == "n":
            return end_program()
        else:
            print("Wrong syntax. Please try again!")


fname_list = []
hourly_rate_list = []
working_hours_list = []
income_list = []
income_tax_deduction_list = []
superannuation_deduction_list = []

welcome()
ask_continue()

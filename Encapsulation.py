class Empolyee:
    def __init__(self):
        self.emp_name=input(("Enter a Employee name:"))
        self.emp_id=input(("Enter a Employee id:"))
        self.emp_salary=input(("Enter a salary:"))
    def employee_display(self):
        print(f"The employee name is {self.emp_name} \nThe Employee id is:{self.emp_id}\n"
              f"Employee Salary is {self.emp_salary}")
        # print(self.details)

    # def Employee_Store_Details(self):
    #     with open("data.txt",'a') as f:
    #         data=f.write(self.details)
emp=Empolyee()
# emp.employee_display()
# print(emp(self.details))
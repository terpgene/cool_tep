# class Employee:
#     name = "Ben"
#     designation = "Sales Executive"
#     salesMadeThisWeek = 6

#     def hasAchievedTarget(self):
#         if self.salesMadeThisWeek >= 5:
#             print("Target has been achieved")
#         else:
#             print("Not achieved")


# employeeOne = Employee()
# print(employeeOne.name)
# employeeOne.hasAchievedTarget()


# class Employee2:
#     numberofWorkingHours = 40


# Employee2.numberofWorkingHours = 45
# employeeOne = Employee2()

# print(employeeOne.numberofWorkingHours)
# employeeOne.name = "Gene"
# print(employeeOne.name)

# employeeOne.numberofWorkingHours = 35
# print(employeeOne.numberofWorkingHours)





class Employee:
    def employeeDetails(self):
        self.name = "Matthew"
        print("Name = " + self.name)
        age = 30
        print('Age = ',age)
    
    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name: ",self.name)
        print("Age: ",age)

employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()
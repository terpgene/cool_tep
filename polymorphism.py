class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40
    
    def displayWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45
    
employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end = ' ')
employee.displayWorkingHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of trainee: ", end = ' ')
trainee.displayWorkingHours()
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetails(self):
        print(f"Employee Name is {self.name} and his age is {self.age}")


E1 = Employee("Abhishek", "21")
E1.printDetails()
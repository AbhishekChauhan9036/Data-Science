# Object-Oriented Programming (OOP) Basics

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.make} {self.model}, Year: {self.year}")

    def age(self, current_year):
        return current_year - self.year


car1 = Car("Toyota", "Corolla", 2015)
car2 = Car("Honda", "Civic", 2018)


car1.display_info()              # Output: Car: Toyota Corolla, Year: 2015
print("Age:", car1.age(2025))    # Output: Age: 10

car2.display_info()              # Output: Car: Honda Civic, Year: 2018
print("Age:", car2.age(2025))    # Output: Age: 7

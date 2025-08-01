class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)  
print ('Car 1 Information:')
print(car1.display_info())
print ('Car 2 Information:')
print(car2.display_info())
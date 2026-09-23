class Module2:
    def __init__(self):
        self.name = "Module 2"
    
    def greet(self):
        return f"Hello from {self.name}!"

    def cube(self, number):
        return number * number * number

    def devide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x // y
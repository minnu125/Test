from django.shortcuts import render

class Rational(ListView):
    
    def add(self, x, y):
        print("Addition: {}".format(x + y)) 

    def divide(self, x, y):
        print("Division: {}".format(x / y))

    def multiply(self, x, y):
        print("Multiplication: {}".format(x * y)) 

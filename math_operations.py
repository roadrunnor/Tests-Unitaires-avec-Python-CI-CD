# python
# math_operations.py
def addition(a, b):
 return a + b
def soustraction(a, b):
 return a - b
def multiplication(a, b):
 return a * b
def division(a, b):
 if b == 0:
 		raise ValueError("Division par zéro n'est pas autorisée")
 return a / b
def param(n1, n2):
    return n1 ** n2
num1, num2 = map(int, input("Son va darajaga Kiriting: . . .").split())
numbers = param(num1, num2)
print(numbers)
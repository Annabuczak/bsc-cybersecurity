class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
     if b ==0:
       return "Error: Cannot divide by zero"
     return a / b

def main():
    print("\nCalculator")
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Go to main menu")
    if __name__ == "__main__":
        main()
        print("\nSelect an operation:")
        choice = input("Enter your choice: ")
        calc = Calculator()
        if choice == "1":
         a = float(input("Enter first amount: "))
         b = float(input("Enter second amount: "))
        result = calc.add(a, b)
        print(result)
    elif choice == "2":
     a = float(input("Enter first amount:"))
    b = float(input("Enter second amount: "))
    result = calc.subtract(a,b)
    print(result)
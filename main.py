from calculator import calc

def repl():
    print("Simple Calculator (type 'quit' to exit)")
    while True:
        try:
            user_input = input("Enter operation (e.g. 2 + 3): ")
            if user_input.lower() == 'quit':
                break

            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Format: number operator number (e.g. 4 * 5)")
                continue

            a, operator, b = parts
            a = float(a)
            b = float(b)

            if operator == '+':
                result = calc.add(a, b)
            elif operator == '-':
                result = calc.subtract(a, b)
            elif operator == '*':
                result = calc.multiply(a, b)
            elif operator == '/':
                result = calc.divide(a, b)
            else:
                print("Unsupported operator. Use +, -, *, /")
                continue

            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()

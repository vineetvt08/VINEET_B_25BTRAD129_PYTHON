def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def main():
    print("=== Fibonacci Series Using Recursion ===")
    try:
        terms = int(input("Enter the number of terms: "))
        if terms <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            print(f"Fibonacci series up to {terms} terms:")
            series = [fibonacci_recursive(i) for i in range(terms)]
            print(", ".join(map(str, series)))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_factorial(n):
    if n < 0:
        return "Undefined (factorial does not exist for negative numbers)"
    return math.factorial(n)

def main():
    print("=== Prime Number and Factorial Program ===")
    try:
        number = int(input("Enter an integer: "))
        
        # Check Prime Status
        if is_prime(number):
            print(f"Prime Status : {number} is a PRIME number.")
        else:
            print(f"Prime Status : {number} is NOT a prime number.")
            
        # Calculate Factorial
        fact = get_factorial(number)
        print(f"Factorial : {number}! = {fact}")
        
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()

import random

while True:
    try:
        number_of_dice = int(input("Enter number of dice to roll: "))
        rolls = int(input("Enter number of times to roll: "))
        
        if number_of_dice <= 0 or rolls <= 0:
            print("Please enter positive numbers.")
            continue
            
        frequency = {}
        for roll_number in range(1, rolls + 1):
            results = [random.randint(1, 6) for _ in range(number_of_dice)]
            total = sum(results)
            print(f"Roll {roll_number}: {results} (Total = {total})")
            frequency[total] = frequency.get(total, 0) + 1
            
        print("\nFrequency of totals:")
        for total in sorted(frequency):
            print(f"{total}: {frequency[total]} time(s)")
        break
        
    except ValueError:
        print("Please enter valid whole numbers.")

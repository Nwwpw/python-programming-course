"""
#Question 2: Enhanced(ทำให้ดีขึ้น) Guessing Game with Hints
Develop an enhanced guessing game with intelligent hint system:
Core Features:

Random number between 1-100
Unlimited attempts

Progressive hint system:

    After 3 wrong guesses: Show if number is odd/even
    After 5 wrong guesses: Show if divisible by 3 or 5 (หารด้วย 3หรือ5 ลงตัว)
    After 7 wrong guesses: Narrow(ทำให้แคบลง) the range to 25-number window (เอาเป็นช่วงของตัวเลขที่สุ่มได้25ตัว)
    After 10 wrong guesses: Show first digit ()
    
Example 
    === Enhanced GUESSING GAME ===
    Guess my number between 1 and 100!
    You have unlimited attempts.

    Attempt 1 - Enter your guess: 10
    Too low! Try again.

    Attempt 2 - Enter your guess: 15
    Too high! Try again.

    Attempt 3 - Enter your guess: 12
    Too low! Try again.
    HINT: The number is even
    
    ...
    
    Attempt 5 - Enter your guess: 20
    Too high! Try again.
    HINT: The number is divisible by 5
    
    ...
    
    Congratulations! You won in 10 attempts!

"""

import random

def get_parity_hint(number):
    if number % 2 == 0:
        return "HINT: The number is even" 
    else:
        return "HINT: The number is odd"

def get_divisibility_hint(number):
    if number % 3 == 0:
        return "HINT: The number is divisible by 3"
    elif number % 5 == 0:
        return "HINT: The number is divisible by 5"
    else:
        return "HINT: The number is NOT divisible by 3 or 5"

def get_range_hint(number, current_min=1, current_max=100):
    # Return narrowed range around the number
    low = max(current_min, number-12)   #กันไม่ให้ต่ำกว่า1
    high = min(current_max, number+12)  #กันไม่ให้ต่ำกว่า100
    print(f"HINT: The narrowed range around the number is {low}-{high}")

def get_thefirst_digit_hint(number):
    # Return the first digit of the number
    first_digit = result//10    #ถ้ามันเป็น87 จะเอา87//10 = 8
    print(f"HINT: The first digit of the number is {first_digit}")
    """
    อีกแบบตามไอเดียเพื่อน
    result = str(number)
    print(f"HINT: The first digit of the number is {result[0]}")
    """

print("=== Enhanced GUESSING GAME ===")
print("Guess my number between 1 and 100!")
print("You have unlimited attempts.")

random_number = random.randint(1, 100)
attemp = 1

while True:

    guess_number = int(input(f"Attempt {attemp} - Enter your guess:"))

    if random_number == guess_number:
        print(f"Congratulations! You won in {attemp} attemps!")
        break
    elif random_number < guess_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

    if attemp == 3:
        get_parity_hint(guess_number)
    elif attemp == 5:
        get_divisibility_hint(guess_number)
    elif attemp == 7:
        get_range_hint(random_number)
    elif attemp == 10:
        get_thefirst_digit_hint(random_number)
    
    attemp += 1
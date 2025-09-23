import random

def test_random():
    # สร้างตัวแปร random_number ตัวแปรคือการสุ่มเลขระหว่าง 1-10
    random_number = random.randint(1, 10)
    print("== Guess Number between (1-10) ==")
    guess_number = input("What is your guess number: ")
    guess_number = int(guess_number)

    if random_number == guess_number:
        print("Congratulations!")
    
    elif random_number < guess_number:
        print("Too high")

    elif random_number > guess_number:
        print("Too low")

    #print(random_number)
    
test_random()
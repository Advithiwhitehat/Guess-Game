import random 
n = random.randint(1,9)
chances = 5
while chances > 0: 
    guess = input("Guess the number: ")
    if guess == n:
        print("Congratulation!!!!!!!!!!!!!")
        break
    elif guess != n:
        print("Guess Again")
    chances = chances -1
    if chances == 0:
        print("You lose")

<<<<<<< HEAD
import random 

print("Hi, Welcom to to the Number Guessing Game. Enjoy the game while improving you skills!")

play_again = "yes"
while play_again == "yes":
    
    while True:
        try:
            lower_bound = int(input("Insert the Lower Bound: "))
            upper_bound = int(input("Insert the Upper Bound: "))
            
            if lower_bound >= upper_bound:
                print("Lower bound must be less than upper bound!")
                continue
            
            if upper_bound - lower_bound < 2:
                print("Error: Bounds are too close! There must be at least one number between them.")
                print("(e.g., 1 to 3 allows secret number 2)")
                continue
            
            break
        except ValueError:
            print("Please insert a valid number")
    
    chances = 3
    print(f"You got {chances} chances to guess the number between {lower_bound} & {upper_bound}. Good Luck!")
    
    secret_number = random.randint(lower_bound + 1, upper_bound - 1)
    guess_count = 0
    
    while guess_count < chances:
        while True:
            try:
                user_try = int(input("Try your guess here: "))
                if not lower_bound <= user_try <= upper_bound:
                    print(f"Out of range! Please guess between {lower_bound} and {upper_bound}.")
                    continue
                
                if lower_bound == user_try or user_try == upper_bound:
                    print(f"The upper bounday {upper_bound} and the lower boundary {lower_bound} are excluded, please try again")
                    continue
                
                break
            except ValueError:
                print("Please insert a valid number")
                
        guess_count += 1
        attempts_left = chances - guess_count
        
        if user_try == secret_number:
            print(f"Congratulation, you get it in {guess_count} try.")
            break
        elif guess_count >= chances:
            print(f"Game Over. the number was {secret_number}")
        elif user_try > secret_number:
            print(f"You got {attempts_left} chances left, make it a bit lower")
        elif user_try < secret_number:
            print(f"You got {attempts_left} chances left, make it a bit higher")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
print("Better luck next time")
=======

>>>>>>> 641b259137337f4c958f621a153c73713e142af1

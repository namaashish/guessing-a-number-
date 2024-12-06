import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("too high")
        return turns-1
        
    elif user_guess < actual_answer :
        print("too low")
        return turns-1
    else:
        print(f"you got it ! The answer was {actual_answer}")


def set_difficulty():
    level = input("choose a Difficulty. Type 'easy' OR 'hard' : ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print('invlaid')



def game():
    print("welcome to the Number Guessing game !")
    print("I am thinkng of a number between 1 and 100.")
    computer_choice = random.randint(1, 100)

    turns = set_difficulty()
   


    Guess = 0 
    while turns > 0 :
        print(f'you have {turns} attempts remaining to guess the number ')
        Guess = int(input('Make a guess :'))
        turns = check_answer(Guess, computer_choice, turns)
        if turns == 0 :
            print('you have run out of guesses')
            return 
        elif Guess!= computer_choice :
            print("Run the commaand again")
            

game()




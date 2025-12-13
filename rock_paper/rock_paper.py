import random

user_wins = 0 
computer_wins = 0
options =  ['rock', 'scissors', 'paper']

while True:
    user_input = input("Type Rock/Paper/Scrissors or Q to quit: ").lower().strip()
    if user_input == "q":
        #quit() # completely stops the loop or can use break keyword! 
        # quit completely stops the program (whole python file)
        break # it stops the loop or break the loop only not whole program 
        # also breaks the only innermost loop
    
    if user_input not in ['rock', 'scrissors', 'paper']:
        continue # it will make loop running from asking if input is wrong !
        # skips one step 
    random_number = random.randint(0,2)
    # rock: 0, paper:1, scrissors: 2 
    computer_choice = options[random_number]
    # now have to build game logic or rule !
    print(f"computer choice is {computer_choice}")

    # okay so if we are using if only then can use continue to save 
    # further exectuion of codes if results is found 
    # optimization thing 

    # or else we can use elif's ! -- if one statement is correct further 
    # conditions will not be checked !

    if user_input == 'rock' and computer_choice == 'scissors':
        print("You Won!")
        user_wins += 1

    elif user_input == 'paper' and computer_choice == 'rock':
        print("You Won!")        
        user_wins += 1

    elif user_input == 'scissors' and computer_choice == 'paper':
        print("You Won!")
        user_wins += 1

    elif user_input == computer_choice:
        print("Draw!")
        continue 

    else: 
        print("Computer won!")
        computer_wins += 1

print(f"user won: {user_wins} times and computer won: {computer_wins} times!\n")
print("goodbye")
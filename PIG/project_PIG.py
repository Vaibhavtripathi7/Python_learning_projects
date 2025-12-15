import random

NO_OF_PLAYERS = int(input("Please enter no of players: "))
scores = [0]*NO_OF_PLAYERS
Condition = True
ROUND_NO = 1 

def player_every_roll_score(no_of_times, player):
    for score in range(0, no_of_times):
        number = random.randint(1,6)
        if number == 1:
            scores[player] = 0
            break
        else:
            scores[player] += number
            if scores[player] > 50:
                print(f"Player number won!:{ player + 1} with score {scores[player]}")
                player = NO_OF_PLAYERS + 1
                global Condition
                Condition = False
                return 0             


while Condition:
    print(f"ROUND-NO {ROUND_NO}") 
    player = 0
    while player < NO_OF_PLAYERS:
        print(f"Choose for Player{player + 1}")
        no_of_times = int(input("Please enter no of times: "))
        player_every_roll_score(no_of_times, player)

        player = player + 1 
    ROUND_NO += 1





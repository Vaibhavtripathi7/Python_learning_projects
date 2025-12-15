import random

NO_OF_PLAYERS = int(input("Please enter no of players: "))
scores = []
for i in range(0, NO_OF_PLAYERS):
    scores.append(0)

player = 0
ROUND_NO = 1 

Condition = True
while Condition:
    print(f"ROUND-NO {ROUND_NO}") 
    player = 0
    while player < NO_OF_PLAYERS:
        print(f"Choose for Player{player + 1}")
        no_of_times = int(input("Please enter no of times: "))
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
                    Condition = False
                    break             

        player = player + 1 

        # if player == NO_OF_PLAYERS:
            # player = 0
    ROUND_NO += 1





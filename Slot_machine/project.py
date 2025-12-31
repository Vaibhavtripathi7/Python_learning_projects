import random

# User data
TOTAL_AMOUNT = None 
BET_AMOUNT = int(input("Enter the Value: "))
CHOOSE_SYMBOL = None 

# Machine part : 
def SlotMachine(user_symobol):
    symbol_1 = "Banana"
    symbol_2 = "Apple"
    symbol_3 = "Grapes"
    s1 = random.randint(1,3)
    s2 = random.randint(1,3) 
    s3 = random.randint(1,3)

    if (s1 == s2 and s2 == s3):
        result = "won"
    else:
        result = "loose"
    return Result




# Game Part : Playing again or cashout

def Reward(Result):
    BET_AMOUNT_Reward = x*BET_AMOUNT
    TOTAL_AMOUNT += BET_AMOUNT_Reward
    return TOTAL_AMOUNT

def lastchoice(UserInput):
    X = "Again"
    Y = "CashOut"

    if (Again):
        # comment -- calling machine function again !: 
        pass
    elif("Cahsou"):
        # comment-- Withdraw amount!: 
    # end if
        pass


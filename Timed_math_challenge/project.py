import random 

operators = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problems():

    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(operators)
    eqn = str(left) + operator + str(right)
    print(f"The Question is:  {eqn}")
    input_answer = int(input("Enter your answer! "))
    answer = eval(eqn)

    if (input_answer == answer):
        print("your answer is correct!")
    else:
        print(f"Wrong answer!, Correct answer is : {answer}")

generate_problems()



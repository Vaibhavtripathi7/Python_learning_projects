import random 

operators = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problems():

    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(operators)
    eqn = str(left) + operator + str(right)
    # print(f"The Question is:  {eqn}")
    # input_answer = int(input("Enter your answer! "))
    answer = eval(eqn)

    return eqn, answer
    # if (input_answer == answer):
        # print("your answer is correct!")
    # else:
        # print(f"Wrong answer!, Correct answer is : {answer}")

# generate_problems()

for i in range(TOTAL_PROBLEMS):
    eqn, ans = generate_problems()
    print(f"The question is: {eqn}")
    guess = int(input("Enter the answer!"))
    if guess == ans:
        break
    else:
        print(f"AHH !! wrong answer, correct answer was! {ans}")
        continue

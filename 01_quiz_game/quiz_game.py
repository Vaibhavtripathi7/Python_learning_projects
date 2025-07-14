print("Welcome to my computer quiz")

playing = input("say yes or no") # by default it takes string -- and also takes all things until enter button used -- even space (not possible in C i think so !! usually)
print(f"\n{playing}")

score = 0

if playing.lower() != "yes":
    quit()

print("okay! lets play..")

answer = input("what does cpu stand for: ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect !")

print("you got " + str(score) + " questions correct!")
print(f"you got {score} questions correct!")
print("you got " + str((score/4)*100) + "%")

pwd = input("What is the master password? :")


def Add():
    name = input("Please enter Account Number: ")
    pwd = input("Please enter Password: ")

    with open("password.txt", 'a') as f:
        f.write(name + " | " + pwd + '\n')

def View():
    try:
        with open('password.txt', 'r') as f:
            for line in f: # or for line in f.readlines():
            #print(f"{line.rstrip()}") # to remove \n effect or line 
                data = line.rstrip()
                user, passw = data.split("|") # gives a list or object
                print(f"User:{user} and Password : {passw}")
    except:
        print("NO password saved! till now")
    # TRY BLOCK KEEPS WORKING EVEN AFTER A ERROR OCCURRED
    # IT JUST, REDIRECT ERROR TO EXCEPT BLOCK AND KEEPS ON RUNNING 

while True:
    mode = input("Please enter:  add or view :")

    if (mode.lower() == 'q'):
        break

    elif (mode.lower() == 'add'):
        Add()

    elif (mode.lower() == 'view'):
        View()
    
    else:
        print("Invalid mode")
        continue

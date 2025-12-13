pwd = input("What is the master password? :")


def Add():
    name = input("Please enter Account Number: ")
    pwd = input("Please enter Password: ")

    with open("password.txt", 'a') as f:
        f.write(name + " " + pwd + '\n')

def View():
    with open('password.txt', 'r') as f:
        for i in f: # or for line in f.readlines():
            print(f"{i.rstrip()}")

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

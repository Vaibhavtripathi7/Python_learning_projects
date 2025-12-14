from cryptography.fernet import Fernet 

"""
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""

def load_key():
    file = open("key.key", "r")
    key = file.read()
    return key # it should be in bytes now ! -- so now error! 

# generate_key() # only once! 

master_pwd = input("What is the master password? :")
# print(type(master_pwd.encode()))

key = (load_key())
# final key -- created using master password! 
# print(type(key))
def Add():
    name = input("Please enter Account Number: ")
    pwd = input("Please enter Password: ")

    with open("password.txt", 'a') as f:
        f.write(name + "|" + (Fernet(key).encrypt(pwd.encode())).decode() + '\n')

def View():
    try:
        with open('password.txt', 'r') as f:
            for line in f: # or for line in f.readlines():
            #print(f"{line.rstrip()}") # to remove \n effect or line 
                data = line.rstrip()
                user, passw = data.split("|") # gives a list or object
                f= Fernet(key)
                # print(f"User:{user} and Password : {Fernet(key).decrypt(passw)}")
                print(f"Username : {user} and Password: {(f.decrypt(passw.encode())).decode()}")
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

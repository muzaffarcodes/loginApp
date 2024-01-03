#LOGIN APP
import time
db_user = 'mountstorm'
db_passwd = 20060617

try_times = 3
while(True):
    if(try_times > 0):
        input_user = input("Username or e-mail: ")
        input_passwd = int(input("Password: "))
        
        if(db_user != input_user and db_passwd == input_passwd):
            print("Username is incorrect. Try again!")
            try_times -= 1
        elif(db_user == input_user and db_passwd != input_passwd):
            print("Password is incorrect. Try again!")
            try_times -= 1
        elif(db_user != input_user and db_passwd != input_passwd):
            print("Username and Password are incorrect. Try again!")
            try_times -= 1
        else:
            print("Welcome, {}!".format(db_user))
            break
    else:
        print("Try again in 5 seconds!")
        for i in range(5,0,-1):
            time.sleep(1)
            print(f"{i} - second")
        try_times = 3

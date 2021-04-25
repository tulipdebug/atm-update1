import random

database = {}

def init():

    print("Welcome to Bank Global")

    haveacccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

    if(haveaccount == 1):
        
        login()             
    elif(haveaccount == 2):
            
        register()
    else:
        print("You have selected invalid option")
        init()

def login():

    print("LOG IN")

    accountNumberfromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountnumber, userdetails in database.items():
               if(accountNumber == accountnumberfromuser):
                   if(userDetails[3] == password):
                       bankOperation(userDetails)

    print('invalid account or password')
    login()
        
def register():

      print("REGISTRATION")

      email = input("What is your email address? \n")
      first_name = input("What is your first name?\n")
      last_name = input("What is your last name? \n")
      password = input("create a password for yourself \n")

accountnumber = generateAccountnumber()

database[accountNumber] = [ first_name, last_name, email, password ]

print("Your account has been created")
print("== ==== ===== ===== ===")
print("your account number is: %d" % accountNumber)
print("make sure you keep it safe")
print("== ==== ===== ===== ===")
    
login()
      
def bankoperation(user):
    print("Welcome %s %s" %( user[0], user[1]))
    selectedoption = int(input("What would you like to do? (1)deposit (2) withdrawal (3)logout (4)exit \n")

  if(selectedoption == 1):                     
                         
     depositOperation()
  elif(selectedoption == 2):
            
        withdrawaloperation()
  elif(selectedoption == 3):
            
        logout()
  elif(selectedoption == 4):
            
            exit()
  else:
            print("invalid option selected")
            bankoperation(user)
            
 def withdrawalOperation():
        print("withdrawal")


def depositOperation():
        print("deposit operation")
        


def generateAccountNumber():

    return random.randrange(1111111111, 99999999999)

def logout()

    
                            

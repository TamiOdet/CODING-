from random import randint


def generatePassword():
    password = []
    for i in range(5):
            p = randint(1,9)
            if p not in password:
                    password.append(p)
            else:
                q = randint(1,9)
                if q != p :
                    password.append(q)
                else:
                    while(q==p):
                        q = randint(1,9)
                    password.append(q)
    print(password)
    return password


def Userguess():
    print("ive set my password, enter 5 digits in the range [1-9](eg.9 3 2 4 7) DO NOT GUESS DUPLICATES")
    
    userGuess = []
    while len(userGuess)!=5:
        passW = int(input(">"))
        userGuess.append(passW)
    return userGuess


def reportResult(password,guess):
    
    digits =0
    location = 0
            
    for i in range(5):
        if guess[i] in password:
            digits += 1
        if guess[i] == password[i]:
            location += 1
    
    print(password)            
    print("you got " + str(digits) + " out of 5 digits correct")
    print("you got " + str(location) + " out of 5 locations correct")
    
    if digits == 5 and location == 5:
        return True
    else:
        return False


    
def main():
    
    reportResult(generatePassword(),Userguess())
main()


letter = input("enter a letter: ")
vowel = "a" or "e" or "i" or "o" or "u"

while(letter != "q"):

        if letter == vowel: 
                print (letter, "is a vowel")
                letter = input("enter a letter: ")


        elif letter == "y":
                print("y is sometimes a vowel")
                letter = input("enter a letter: ")


        else:
                print (letter,"is not a vowel")
                letter = input("enter a letter: ")




print("hello what's your name")
my_name=input("enter your name:  ")
guess_string=""
print("Hello " + my_name+ " time to play hangman")
my_words="Turkey"
lives=10
while lives>0:
    character=0
    for char in my_words:
        if char in guess_string:
             print(char)
            
        else:
             print("-")
             character+=1
        
    if character==0:
        print("You wont!!")
        break

    guess= input("Guess a letter: ")
    guess_string+=guess
    if guess not in my_words:
        lives-=1
        print("Wrong guess!")
        print(f"You have {lives} left")
        if lives==0:
            print("You died")

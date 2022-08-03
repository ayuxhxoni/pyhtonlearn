t=18
guess=1
print("lets play a guess game")
while(guess<=9):
    g=int(input("\n"))
    if(g>t):
        print("this number is greater!!")
        continue
    if(g<t):
        print("this number is smaller!!")
        continue
    if(g==t):
        print("YOU GUESS THE RIGHT ANSWER!!")
        break
print(9-guess, "no. of guesses left")
if(guess>9):
    print("sorry game over")    
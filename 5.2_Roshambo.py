'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
print("Welcome to Roshambo! Choose Rock (1), Paper (2), or Scissors (3), or 4 to quit! Try and beat the bot!")
import random
w = 0
l = 0
p = 0
c = 1
q = 0
f_score = open ('highscore.txt')
old_score = float(f_score.readlines()[0])
print("The high score right now is",(old_score),"%")
while q != 4:
    b = random.randrange(3)
    a = 0
    while a == 0:
        c = str(input("Rock (1), Paper (2), or Scissors (3) or Quit(4)? "))
        if c.replace(" ","") == "1":
            print("You choose Rock!")
            if b == 0:
                print("The bot choose Rock!")
                print("You tied!")
            if b == 1:
                print("The bot choose Paper!")
                print("You lost!")
                l+=1
            if b == 2:
                print("The bot choose Scissors!")
                print("You won!")
                w+=1
            a+=1
            p+=1
        elif c.replace(" ","") == "2":
            print("You choose Paper!")
            if b == 0:
                print("The bot choose Rock!")
                print("You won!")
                w += 1
            if b == 1:
                print("The bot choose Paper!")
                print("You tied!")
            if b == 2:
                print("The bot choose Scissors!")
                print("You lost!")
                l += 1
            a+=1
            p+=1
        elif c.replace(" ","") == "3":
            print("You choose Scissors!")
            if b == 0:
                print("The bot choose Rock!")
                print("You lost!")
                l += 1
            if b == 1:
                print("The bot choose Paper!")
                print("You won!")
                w += 1
            if b == 2:
                print("The bot choose Scissors!")
                print("You tied!")
            a+=1
            p+=1
        elif c.replace(" ","") == "4":
            q = 4
            a+=2
            print("Quiting...")
        else:
            print("Not an option!")
    a-=1
if p == 0:
    print("You didn't play any games and will not receive a score.")
    score = 0
else:
    score = (w/p)*100
    print("You won", w, "times!")
    print("You lost", l, "times!")
    print("You played", p, "times!")
    print("You won",score,"% of the time!")

f_score.close()
if score > old_score:
    f_score = open ('highscore.txt', 'w')
    f_score.write('%s' % score)
    f_score.close()
    print("You beat the high score!")
    reset = input("Would you like to reset the highscore (Enter code)? ")
    if reset == "1234":
        f_score = open('highscore.txt.','w')
        f_score.write('%s'% 0)
        f_score.close()
    else:
        print("Wrong password!")
print("Thank you for playing! If you would like to support the maker of this game, tell Mr. Hermon to let Tristan do physics!")




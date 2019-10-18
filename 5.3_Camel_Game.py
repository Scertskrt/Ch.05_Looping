'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''
import random
print("Welcome to the Minecraft game!")
print("Quickly make it back to your house before the creepers catch up and kill you!")
print("You have a stack of steak left, so you have enough make it back to your house.")
print("However, make sure you're watching your hunger bar or you will starve!")
print("Make sure you eat your steak!")
print("Your alpaca is carrying all of your supplies and steak, so make sure they don't die from exhaustion.")
print("Once your hunger is at 10, you cannot eat anymore.")
print("Running requires 4 hunger and walking requires 2 hunger.")
print("You cannot run if you are too hungry!")
l=0
done_finally=False
done = False
start = "don't start"
mining=0
special_item = False
while done_finally == False:
    while start != ("start"):
        start = input("If your ready to start, type start! ")
        if start.lower() == ("start"):
            print()
            start = ("start")
        else:
            if mining == 10:
                print("You died!")
                start = ("start")
                done = True
                l+=1
            else:
                print("You continue to mine...")
                rewards = random.randrange(100)
                if rewards == 69 and special_item == False:
                    print("You found a mineshaft!")
                    print("There is a potion you have never seen before...")
                    special_item = True
                mining += 1
    h=10
    y=0
    c=-20
    w=0
    a=5
    ran=0
    first=0
    done_finally = False
    while done == False:
        print("Your hunger is now", h)
        print("Your house is", 200 - y, "blocks away.")
        print("The creepers are", y - c, "blocks behind you.")
        print("You alpaca can travel for", a, "more days.")
        print()
        print("You continue to run from the mobs...")
        print()
        print("A. Eat your steak.")
        if h == 10:
            print("You can't eat anymore!")
        print("B. Walk.")
        print("C. Run.")
        if h < 4:
            print("(You are too hungry to run...)")
        print("D. Hide behind a tree and rest.")
        print("E. Status check.")
        print("Q. Quit.")
        if special_item == True:
            print("?. Use strange potion.")
        user = input("You decide to... ")
        if user.lower() == ("a") or user.lower() == ("eat your steak"):
            if h<10:
                print("You ate your steak.")
                h += 4
                c += random.randrange(7, 13)
            else:
                print("You are full!")
        elif user.lower() == ("b") or user.lower() == ("walk"):
            y+=random.randrange(3, 8)
            c+=random.randrange(5,11)
            h-=2
            a -= 1
        elif user.lower() == ("c") or user.lower() == ("run"):
            if h >= 4:
                y+=random.randrange(12,17)
                c+=random.randrange(5, 11)
                h-=4
                a-=1
            else:
                print("You are too hungry.")
        elif user.lower() == ("d") or user.lower() == ("hide behind a tree and rest"):
            c += random.randrange(3, 8)
            a=5
            print("Your alpaca is now rested!")
            ran = random.randrange(10)
            if ran == 5:
                print("There was a zombie behind the tree!")
                done = True
        elif user.lower() == ("e") or user.lower() == ("status check"):
            print("Your hunger is now", h)
            print("Your house is", 200 - y, "blocks away.")
            print("The creepers are", y - c, "blocks behind you.")
            print("You alpaca can travel for", a, "more days.")
        elif user.lower() == ("q") or user.lower() == ("quit"):
            first += 1
            print("You let the creepers kill you.")
            print("You lost all of your enchanted diamond gear.")
            print("You have no back up gear.")
            l+=1
            done =  True
        elif user.lower() == ("?") or user.lower() == ("use strange potion"):
            print("You drank the magic potion")
            o = random.randrange(0,2)
            if o == 0:
                print("The potion was a poison 100 potion.")
                print("You died instantly.")
                l+=1
                done = True
            else:
                print("The potion was a speed 100 potion.")
                print("You blinked and you had already ran home with your alpaca.")
                y+=200
                done = True
        else:
            print("Not an option!")
        if h>10:
            h=10
        if y >= 200:
            print("You made it back to your house!")
            print("You are safe for tonight.")
            w+=1
            done = True
        elif c >= y:
            print("The creepers caught up to you!")
            l += 1
            done = True
        elif h < 1:
            print("You starved!")
            l += 1
            done = True
        elif a < 0:
            print("Your alpaca slowed down out of exhaustion.")
            print("The creepers were able to explode you and your alpaca!")
            print("You died!")
            l+=1
            done = True
        elif ran == 5:
            print("You got killed by a zombie... weakling.")
            l+=1
            done = True
    if w == 1:
        print("You won! You are an epic minecraft gamer!")
        print("You went outside ready to go mining again...")
        d = input("Play again? ")
        if d.lower() == ("y") or d.lower() == ("yes"):
            h = 10
            y = 0
            c = -20
            w = 0
            l = 0
            a = 5
            first = 0
            mining=0
            done = False
            start=("no")
    elif l == 1:
        print("You lost. You are a noob gamer!")
        print("The creepers have won for today...")
        d = input("Play again? ")
        if d.lower() == ("y") or d.lower() == ("yes"):
            h = 10
            y = 0
            c = -20
            w = 0
            l = 0
            a = 5
            first = 0
            start=("no")
            mining=0
            special_item = False
            done = False
        else:
            done_finally = True
print("Thanks for playing!")
print("Tell Mr. Hermon to fix the attendance bot so that it gives candy to those who are earlier!")
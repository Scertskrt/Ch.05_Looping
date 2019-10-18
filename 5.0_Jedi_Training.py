  #Sign your name: Tristan

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
      x = int(input("Enter a number: "))
      total += x
      print("The total is:", total)

'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101,2):
    print(i)

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
x=10
while x != 0:
    print(x,"!")
    x-=1
print("Blast off!")

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
x = random.randrange(1,11)
print(x)


'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
p=0
n=0
z=0
t=0
for i in range(7):
    x = int(input("Pick a number!"))
    t+=x
    if x == 0:
        z+=1
    elif x-abs(x) == 0:
        p+=1
    else:
        n+=1
print("Your total is:",t)
print("You entered",p,"positive numbers!")
print("You entered",n,"negative numbers!")
print("You entered",z,"zeros!")


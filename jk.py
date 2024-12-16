print("Welcome to my computer quiz")

playing=input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()
else:
    print("okay! let's Play")
    points=0

answer=input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    points+=1
else:
    print("Incorrect")

answer=input("what does RAM stands for? ")
if answer.lower()=="random access memory":
    print("Correct!")
    points+=1
else:
    print("Incorrect")

answer=input("what does ROM stands for? ")
if answer.lower()=="read only memory":
    print("Correct!")
    points+=1
else:
    print("Incorrect")


answer=input("what does GPU stands for? ")
if answer.lower()=="graphic processing unit":
    print("Correct!")
    points+=1
else:
    print("Incorrect")

answer=input("what does  PSU stands for? ")
if answer.lower()=="power supply":
    print("Correct!")
    points+=1
else:
    print("Incorrect")

print("you get" +  str (points) + "marks")
print("you get" +str ((points/5)*100) +"%")

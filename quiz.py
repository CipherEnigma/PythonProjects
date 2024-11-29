print("Welcome to my computer quiz!")
playing=input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()
print("Okay! Lets play :)")
score = 0
answer =input("What does GPU stands for? ").lower()
if answer =="graphical processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer =input("What does CPU stands for? ").lower()
if answer =="central processing unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
answer =input("What does RAM stands for? ").lower()
if answer =="random access memory":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
answer =input("What does SSD stands for? ").lower()
if answer =="solid state drive":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

print("You got "+ str(score)+ " questions correct!")
print("You got" + str(score/ 4)* 100) +"%."







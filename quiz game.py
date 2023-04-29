print("welcome to the quiz game !!")

playing = input("Do you want to play ? ")

score = 0

if playing.lower() != "yes":
    quit()

print("okay ! let's play")

answer = input("what is cpu stands for ? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")
    
answer = input("what is GPU stands for ? ")
if answer.lower() == "graphical processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")
    
answer = input("what is HCU stands for ? ")
if answer.lower() == "hyderabad central university":
    print("correct")
    score += 1
else:
    print("incorrect")
    
answer = input("what is PSU stands for ? ")
if answer.lower() == "power supply":
    print("correct")
    score += 1
else:
    print("incorrect")
    
print("you got" + str(score) + " questions correct")
print("you got" + str((score/4) * 100) + "%")

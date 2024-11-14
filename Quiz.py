print("Welcome to Computer Quiz")

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()
else:
    print("Okay, let's play!")
    score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You have got {score * 100 / 4}% marks")

print('Thank you for playing! please come again another time!')
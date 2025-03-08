print("Welcome to Quiz Game") 

print("Do you want to play the game?")

ans = input("yes or no: ")

if ans == "yes":
    print("Great! Let's start the game")
else:
    print("Thank you for your time")
count = 0
while ans == "yes":
    print("Question 1: What is the capital of France?")
    print("a) Paris")
    print("b) London")
    print("c) Berlin")
    print("d) Madrid")
    ans1 = input("Enter your answer: ")

    if ans1 == "a":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    print("Question 2: What is the capital of Germany?")
    print("a) Paris")
    print("b) London")
    print("c) Berlin")
    print("d) Madrid")
    ans2 = input("Enter your answer: ")

    if ans2 == "c":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    print("Question 3: What is the capital of Spain?")
    print("a) Paris")
    print("b) London")
    print("c) Berlin")
    print("d) Madrid")
    ans3 = input("Enter your answer: ")

    if ans3 == "d":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    print("Question 4: What is the capital of England?")
    print("a) Paris")
    print("b) London")
    print("c) Berlin")
    print("d) Madrid")
    ans4 = input("Enter your answer: ")

    if ans4 == "b":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    print("Question 5: What is the capital of Italy?")
    print("a) Paris")
    print("b) London")
    print("c) Berlin")
    print("d) Rome")
    ans5 = input("Enter your answer: ")

    if ans5 == "d":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    print("Thank you for playing the game!")

    print("Do you want to play again?")



    if count >= 4:
        print("You got", count, "questions correct! Well done!")
    else:
        print("You got", count, "questions correct! Better luck next time!")

    ans = input("yes or no: ")

    if ans == "yes":
        print("Great! Let's start the game")
    else:
        print("Thank you for your time")

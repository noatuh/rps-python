import random

op = input("Enter (R)ock, (P)aper, (S)cissors: ")

ROCK = "R"
PAPER = "P"
SCISSORS = "S"

if op.upper() == ROCK:
    print("You chose Rock")
    op = "Rock"
elif op.upper() == PAPER:
    print("You chose Paper")
    op = "Paper"
elif op.upper() == SCISSORS:
    print("You chose Scissors")
    op = "Scissors"
else:
    print("Invalid input")
    exit()

computer_op = random.choice(["Rock", "Paper", "Scissors"])

print("Computer chose", computer_op)

if op == "Rock" and computer_op == "Rock":
    print("It's a tie!")
elif op == "Rock" and computer_op == "Paper":
    print("You lose!")
elif op == "Rock" and computer_op == "Scissors":
    print("You win!")
elif op == "Paper" and computer_op == "Rock":
    print("You win!")
elif op == "Paper" and computer_op == "Paper":
    print("It's a tie!")
elif op == "Paper" and computer_op == "Scissors":
    print("You lose!")
elif op == "Scissors" and computer_op == "Rock":
    print("You lose!")
elif op == "Scissors" and computer_op == "Paper":
    print("You win!")
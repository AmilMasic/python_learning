import random

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player score: {player_wins}, Compture score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player = input("Player 1, make your move: ").lower()
    if player = "quit" or player == "q":
        break
    rand_num = random.randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"computer plays {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock":
        if computer == "scissors":
            print("player wins")
            player_wins += 1
        if computer == "paper":
            print("computer wins")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins")
            player_wins += 1
        if computer == "scissors":
            print("computer wins")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("player wins")
            player_wins += 1
        if computer == "rock":
            print("computer wins")
            computer_wins += 1
    else:
        print("something went wrong")
if player_wins > computer_wins:
    print("Congrats, you won!")
elif player_wins == computer_wins:
    print("it's a tie")
else:
    print("The computer won")

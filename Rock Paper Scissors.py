#rock paper scissors using while loop
import random
options = ['rock','paper','scissors']
while True:
    player = input("Enter Your Choice (rock,paper,scissors) :")
    bot = random.choice(options)
    print("You Choose",player,"and","Computer Chosen",bot)

    if player==bot:
        print("It's Tie!!")
    elif player=="rock" and bot=="paper" or player=="paper" and bot=="scissors" or player=="scissors" and bot=="stone":
        print("Bot Wins!")
    elif player=="paper" and bot=="rock" or player=="scissors" and bot=="paper" or player=="stone" and bot=="scissors":
        print("Player Wins")
        break
    else:
        print("Enter Valid Choice")
        break
from random import randint
print "Welcome to the number guessing game!\nI have my number..."

for i in range(1):
    player_guess = input("What is your guess [1-10](limit 3 times)?")
    num = randint(1,10)
    times = 1
    while True:
        if times >= 3:
            print "Thanks for playing,it's over now!"
            break
        elif num == player_guess:
            print "You got it!Thanks for playing!"
            break
        elif num > player_guess:
            print "That's too low.Try again!"
            player_guess = input("What is your guess [1-10](limit 3 times)?")
            times +=1
        elif num < player_guess:
            print "That's too high.Try again!"
            player_guess = input("What is your guess [1-10](limit 3 times)?")
            times +=1

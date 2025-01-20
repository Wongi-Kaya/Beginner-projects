# Number guessing game
import random, time

keep_playing = True
highest_num = 100
lowest_num = 0
num_of_guesses = 0
score = 110
answer = random.randint(lowest_num, highest_num)
total_score = 0
games_played = 0

print((f"Guess a number between {lowest_num} and {highest_num}"
                  f" (Type Q to stop playing): "))

while keep_playing:
    guess = input("Enter your guess: ")
    # Stop playing
    if guess.lower() == "q":
        print("Cya never")
        keep_playing = False
    # Number out of range or not
    elif int(guess) < lowest_num or int(guess) > highest_num:
        print(f"YOUR NUMBER IS OUT OF RANGE! ENTER A NUMBER BETWEEN {lowest_num} AND {highest_num}")
    # Direct the player
    elif int(guess) > answer:
        print("Your guess is too high")
        num_of_guesses += 1
    elif int(guess) < answer:
        print("Your guess is too low")
        num_of_guesses += 1
    # Results
    else:
        num_of_guesses += 1
        score = score - (num_of_guesses * 10)
        print(f"YOUR ANSWER IS CORRECT! OMG IT REALLY IS {answer}")
        time.sleep(1.5)
        print(f"It took you {num_of_guesses} guesses to find this easy number")
        time.sleep(1.5)
        print(f"Your score is: {score} cookies")
        time.sleep(1)
        num_of_guesses -= num_of_guesses
        total_score += score
        score = (110 - score) + score
        answer = random.randint(lowest_num, highest_num)
        games_played += 1

        # Play again?
        if not input("Would you like to play another game? (Yes/No) ") == "yes":
            print(f"Your total score is: {total_score} out of {games_played} games")
            time.sleep(1)
            print("Cya never")
            keep_playing = False
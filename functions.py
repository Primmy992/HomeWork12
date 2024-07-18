import json
import datetime


def play_game(secret, name, level, scoreList):
    attempts = 0
    wrongguess = 0
    while True:
        guess = int(input(f"Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            print("Wrong attempts: " + str(wrongguess))
            scoreData = {
                "name": name,
                "secretNumber": secret,
                "attempts": attempts,
                "wrong_guesses": wrongguess,
                "date": str(datetime.datetime.now())
            }

            scoreList.append(scoreData)

            with open("score.json", "w") as scoreFile:
                scoreFile.write(json.dumps(scoreList))
            break
        elif guess > secret:
            if level == "easy":
                print("Your guess is not correct... try something smaller")
                wrongguess += 1
            else:
                print("Wrong!")
                wrongguess += 1
        elif guess < secret:
            if level == "easy":
                print("Your guess is not correct... try something bigger")
                wrongguess += 1
            else:
                print("Wrong!")
                wrongguess += 1

    return scoreList

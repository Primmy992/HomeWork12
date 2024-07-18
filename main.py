import random
import json
import datetime

from functions import play_game

secret = random.randint(1, 30)
attempts = 0
wrongGuess = 0

d = datetime.datetime.now()
print(d)

with open("score.json", "r") as scoreFile:
    scoreList = json.loads(scoreFile.read())

name = input("Enter your name: ")

while True:
    selection = input("Would you like to A) play a new game, B) see the bests cores, or C) quit?")
    if selection not in {'A', 'B', 'C'}:
        print("Please provide valid input! Inputs: A or B or C")
        continue

    if selection == "A":
        level = input("Choose a difficulty level by entering ""hard"" or ""easy"" ")
        scoreList = play_game(secret, name, level, scoreList)
    elif selection == "B":
        def get_attempts(dictscore):
            return dictscore["attempts"]

        top_scores = sorted(scoreList, key=get_attempts)[:3]

        print("\nTop 3 Results:")
        identifier = 1
        for score in top_scores:
            print(f"{identifier}. {score['name']} - {score['attempts']} attempts on {score['date']}")
            identifier += 1

    else:
        break

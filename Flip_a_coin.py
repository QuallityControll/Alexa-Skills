from flask import Flask
from flask_ask import Ask, statement, question
import random


app = Flask(__name__)
ask = Ask(app, '/')


@app.route('/')
def homepage():
    return "Hello"


@ask.launch
def start_skill():
    msg = "What side of the coin do you want?"
    return question(msg)


def flip_a_coin():
    if random.random() < 0.5:
        return "Heads"
    else:
        return "Tails"


@ask.intent("HeadsIntent")
def heads_intent():
    a = flip_a_coin()
    if a == "Tails":
        return statement("You lose.")
    else:
        return statement("You win")


@ask.intent("TailsIntent")
def tails_intent():
    a = flip_a_coin()
    if a == "Heads":
        return statement("You lose.")
    else:
        return statement("You win")

if __name__ == '__main__':
    app.run(debug=True)

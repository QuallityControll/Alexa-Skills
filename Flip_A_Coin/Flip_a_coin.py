from flask import Flask
from flask_ask import Ask, statement, question
import random

"""
Intent Scheme:
{
  "intents": [
    {
      "intent": "HeadsIntent"
    },
    {
      "intent": "TailsIntent"
    }
  ]
}

Sample Utterances:

HeadsIntent heads
HeadsIntent head
TailsIntent tails
TailsIntent tail

"""
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
    """
    It will return a string of "Heads" or "Tails". Based on an RNG.

    Returns:
        A string that is heads or tails based on an RNG. 
    """
    if random.random() < 0.5:
        return "Heads"
    else:
        return "Tails"


@ask.intent("HeadsIntent")
def heads_intent():
    """
    This is the function that tells if you win or lose based off
    of the heads you said. 
    """
    a = flip_a_coin()
    if a == "Tails":
        return statement("You lose.")
    else:
        return statement("You win")


@ask.intent("TailsIntent")
def tails_intent():
        """
    This is the function that tells if you win or lose based off
    of the tails you said. 
    """
    a = flip_a_coin()
    if a == "Heads":
        return statement("You lose.")
    else:
        return statement("You win")

if __name__ == '__main__':
    app.run(debug=True)

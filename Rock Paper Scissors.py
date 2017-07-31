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
    msg = "Rock, paper or scissors?"
    return question(msg)

def get_comp_answer():
    a = random.random()
    if a < 1.0/3:
        return "Rock"
    elif a < 2.0/3:
        return "Paper"
    else:
        return "Scissors"


@ask.intent("RockIntent")
def rock_intent():
    comp = get_comp_answer()
    if comp == "Rock":
        return statement(comp + ". Tie")
    elif comp == "Scissors":
        return statement(comp + ". You Win")
    else:
        return statement(comp + ". You lose")


@ask.intent("PaperIntent")
def paper_intent():
    comp = get_comp_answer()
    if comp == "Paper":
        return statement("Tie")
    elif comp == "Rock":
        return statement("You Win")
    else:
        return statement("You lose")


@ask.intent("ScissorsIntent")
def scissors_intent():
    comp = get_comp_answer()
    if comp == "Scissors":
        return statement("Tie")
    elif comp == "Paper":
        return statement("You Win")
    else:
        return statement("You lose")

if __name__ == '__main__':
    app.run(debug=True)

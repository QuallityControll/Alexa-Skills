from flask import Flask
from flask_ask import Ask, statement, question
import requests
import time
import unidecode
import json

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    return "Hello"

@ask.launch
def start_skill():
    msg = "Hi there. Have you been feeling hot lately? Do you feel like you have been stressing out over anxiety? Or having hard times with pain, fatigue, and/or feaver? All in all do you feel like you have been having a rough time over the past couple of weeks?"
    return question(msg)

@ask.intent("YesIntent")
def share_remedy():
    remedy_msg = "Then you are having symptoms of Cog Works. To fix this I recommend to take a Seven Minute Break!. Have an amazing day".format(remedy)
    return statement(remedy_msg)

@ask.intent("NoIntent")
def no_intent():
    msg = "Ok, thanks. Have a nice day."
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)

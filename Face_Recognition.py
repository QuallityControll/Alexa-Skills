import Face_Recognition as fr
from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')


@app.route('/')
def homepage():
    return "Hello"


@ask.launch
def start_skill():
    msg = "What do you want to do? Add to the database, or recognize a person?"
    fr.load()
    return question(msg)


@ask.intent("AddIntent")
def add_intent():

@ask.intent("RecognizeIntent")
def rec_intent():
    names = fr.identify(display_picture=False)
    msg = "I see "
    num_not_recognized = 0
    for name in names:
        if name == "Not recognized":
            num_not_recognized += 1
        else:
            msg += name + ", "

    if num_not_recognized != 1:
        msg += "and " + num_not_recognized + " people I don't recognize."
    else:
        msg += "and " + num_not_recognized + " person I don't recognize."
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)




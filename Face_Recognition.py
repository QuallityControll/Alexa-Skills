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
    #msg = "What do you want to do? Add to the database, or recognize a person?"
    msg = "Hi"
    return question(msg)


@ask.intent("AddIntent")
def add_intent(firstname):
    """
    This takes the name of the person and then takes a picture of the person and adds the person to the
    database.

    Params:
        firstname[str]:
            A string that is the name of the person.
    Returns:
        statement("Done."):
            It says "Done." when it is done saving it in the database.
    """
    fr.add(firstname)
    fr.list_people()
    fr.save()
    return statement("I added " + str(firstname))


@ask.intent("RecognizeIntent")
def rec_intent():
    """
    The camera will take a picture and recognize everyone in the picture. It then formats the names into a
    grammatically correct sentence.

    Returns:
        statement(msg[str]):
            Alexa will say the people in the picture with the format of the people it knows first and then
            a count of the people it doesn't recognize.

    """

    names = fr.identify(display_picture=False)
    msg = "I see "
    num_not_recognized = 0
    for name in names:
        if name == "Not recognized":
            num_not_recognized += 1
        else:
            msg += name + ", "
    if num_not_recognized != 0:
        if msg == "I see ":
            if num_not_recognized != 1:
                msg += str(num_not_recognized) + " people I don't recognize."
            else:
                msg += str(num_not_recognized) + " person I don't recognize."
        else:
            if num_not_recognized != 1:
                msg += "and " + str(num_not_recognized) + " people I don't recognize."
            else:
                msg += "and " + str(num_not_recognized) + " person I don't recognize."
    elif msg == "I see ":
        return statement("No one is there. ")
    return statement(msg)

@ask.intent("ListIntent")
def edgy_alexa():
    return statement(fr.list_people())

@ask.intent("RemoveIntent")
def remove(firstname):
    fr.remove(firstname)
    return statement("Done. " + str(firstname) + " was removed.")

if __name__ == '__main__':
    app.run(debug=True)

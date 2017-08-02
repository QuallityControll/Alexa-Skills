from flask import Flask
from flask_ask import Ask, statement, question, session
import Face Recognition as fr
from userdata import Userdata
import pickle

app = Flask(__name__)
ask = Ask(app, '/')

#import userdata with pickle
try:
    with open("userdata.pkl","rb") as f:
        userdata = pickle.load(f)
except:
    userdata = Userdata()

@app.route('/')
def homepage():
    return "Hello"

def user():
    return session.attributes[user_name]

def nick():
    #if user has nickname in dict, return that. if not, return raw name
    try:
        return = userdata.usernicknames[user()]
    except:
        return user()

def save_userdata():
    with open("userdata.pkl","wb") as f:
        pickle.dump(userdata, f)

@ask.launch
def start_skill():
    return question("Hello, {}. What would you like to do?".format(nick())
        .reprompt("I don't understand. What would you like me to do?")

#----------------------------------------------------------------------------
#                     CONFIGURATION
#----------------------------------------------------------------------------

@ask.intent("UpdateUserIntent")
def update_user():
    name_list = fr.identify()
    if len(name_list)==0:
        return statement("I see noone. Make sure you are in front of the camera."
    elif len(name_list)>1:
        return statement("I see multiple people. Make sure you are the only \
                            person facing the camera."
    name = namelist[0]
    if name == "Not Recognized"
        return statement("I don't recognize you. Try adding yourself \
                            to the face recognition database.")
    else:
        session.attributes[user_name] = name
        userdata.user_history.add(name)
        save_userdata()

    return statement("Updated user to {}".format(nick())

#slot: {newname}
@ask.intent("UserNicknameIntent")
def update_user_nickname(newname):
    userdata.usernicknames[user()] = newname
    save_userdata()

    return statement("{} is now {}'s nickname".format(nick(), user()))

@ask.intent("RemoveUserNicknameIntent")
def remove_user_nickname():
    del userdata.usernicknames[user()]
    save_userdata()

    return statement("{}'s nickname has been removed.".format(user()))

#---------------------------------------------------------------------------
#                   USER SPECIFIC TO DO / SHOPPING LIST
#---------------------------------------------------------------------------

@ask.intent("AddToListIntent")
def add_to_list(item):
    userdata.user_lists[user()].append(item)
    save_userdata()
    return statement("Added {} to {}'s list".format(item, nick()))

@ask.intent("RemoveFromListIntent")
def remove_from_list(item):
    userdata.user_lists[user()].remove(item)
    save_userdata()
    return statement("Removed {} from {}'s list".format(item, nick()))

@ask.intent("ClearListIntent")
def clear_list():
    userdata.user_lists[user()].clear()
    save_userdata()
    return statement("Cleared {}'s list".format(nick()))

@ask.intent("ListListIntent")
def list_list():
    joined_list = ", ".join(userdata.user_lists[user()])
    return statement("Here is {}'s list: {}.".format(nick(), joined_list))

@ask.intent("CheckListIntent")
def check_list(item):
    if item in userdata.user_lists[user()]:
        msg = "{} is in {}'s list.".format(item, nick())
    else:
        msg = "{} is not in {}'s list.".format(item, nick())
    return statement(msg)

#---------------------------------------------------------------------------
#                      USER IDENTITY
#---------------------------------------------------------------------------

@ask.intent("GreetMeIntent")
def greet_me():
    msg = "Hello, {}".format(nick())
    return statement(msg)

@ask.intent("SingMeHappyBirthdayIntent")
def sing_happy_birthday():
    msg = """
            Happy birthday to you,
            Happy birthday to you,
            Happy birthday dear {},
            Happy birthday to you
        """.format(nick())
    return statement(msg)

@ask.intent("ConfirmIdentityIntent")
def confirm_identity():
    msg = "The current user is {}".format(user())

#--------------------------------------------------------------------------
#                       SOCIAL MEDIA
#--------------------------------------------------------------------------

#implement later???
@ask.intent("CheckFacebookIntent"):
def check_facebook():
    pass

@ask.intent("PostToFacebookIntent"):
def post_facebook():
    pass

@ask.intent("CheckTwitterIntent"):
def check_twitter():
    pass

@ask.intent("PostToTwitterIntent")
def post_twitter():
    pass

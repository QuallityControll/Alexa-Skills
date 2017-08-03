from flask import Flask
from flask_ask import Ask, statement, question, session
import Face_Recognition as fr
from userdata import Userdata
import pickle

app = Flask(__name__)
ask = Ask(app, '/')

#import userdata with pickle

"""
{
  "intents": [
    {
      "intent": "UpdateUserIntent",
      "slots": [
      ]
    },
    {
      "intent": "UserNickNameIntent",
      "slots": [
        {
          "name": "nickname",
          "type": "AMAZON.LITERAL"
        }
      ]
    },
    {
      "intent": "RemoveUserNicknameIntent",
      "slots": [
      ]
    },
    {
      "intent": "AddToListIntent",
      "slots": [
        {
          "name": "topic",
          "type": "AMAZON.LITERAL"
        }
      ]
    },
    {
      "intent": "RemoveFromListIntent",
      "slots": [
        {
          "name": "topic",
          "type": "AMAZON.LITERAL"
        }
      ]
    },
    {
      "intent": "ClearListIntent",
      "slots": [
      ]
    },

    {
      "intent": "ListListIntent",
      "slots": [
      ]
    },
    {
      "intent": "CheckListIntent",
      "slots": [
        {
          "name": "topic",
          "type": "AMAZON.LITERAL"
        }
      ]
    },

    {
      "intent": "GreetMeIntent",
      "slots": [
      ]
    },

    {
      "intent": "SingMeHappyBirthdayIntent",
      "slots": [
      ]
    },

    {
      "intent": "ConfirmIdentityIntent",
      "slots": [
      ]
    }
  ]
}

"""

try:
    with open("userdata.pkl","rb") as f:
        userdata = pickle.load(f)
except:
    userdata = Userdata()

fr.load()
fr.list_people()

@app.route('/')
def homepage():
    return "Hello"

def user():
    try:
        if session.attributes["user_name"] is None:
            return "User"
        else:
            return session.attributes["user_name"]
    except:
        return "User"

def nick():
    #if user has nickname in dict, return that. if not, return raw name

    try:
        if userdata.usernicknames[user()] is None:
            return user()

        else:
            return userdata.usernicknames[user()]
    except:
        return user()

def save_userdata():
    with open("userdata.pkl","wb") as f:
        pickle.dump(userdata, f)

@ask.launch
def start_skill():
    return question("Hello {}. What would you like to do?".format(nick())
        .reprompt("I don't understand. What would you like me to do?"))

#----------------------------------------------------------------------------
#                     CONFIGURATION
#----------------------------------------------------------------------------

@ask.intent("UpdateUserIntent")
def update_user():
    import Face_Recognition as fr
    fr.load()
    print("loaded database")
    print(fr.list_people())
    name_list = fr.identify()
    if len(name_list)==0:
        return statement("I see noone. Make sure you are in front of the camera.")
    elif len(name_list)>1:
        msg = "I see multiple people. Make sure you are the only person facing the camera."
        return statement(msg)
    name = name_list[0]
    if name == "Not recognized":
        msg = "I don't recognize you. Try adding yourself to the face recognition database."
        return statement(msg)
    else:
        session.attributes["user_name"] = name
        userdata.user_history.add(name)#
        save_userdata()

    return statement("Updated user to {}".format(nick()))

#slot: {newname}
@ask.intent("UserNickNameIntent")
def update_user_nickname(nickname):
    print("nickname",nickname)
    userdata.usernicknames[user()] = nickname
    save_userdata()
    print("nick",nick())
    print("user",user())

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
def add_to_list(topic):
    if topic is None:
        return statement("Could not understand item to add.")
    userdata.user_lists[user()].append(topic)
    save_userdata()
    return statement("Added {} to {}'s list".format(topic, nick()))

@ask.intent("RemoveFromListIntent")
def remove_from_list(topic):
    userdata.user_lists[user()].remove(topic)
    save_userdata()
    return statement("Removed {} from {}'s list".format(topic, nick()))

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
def check_list(topic):
    if topic in userdata.user_lists[user()]:
        msg = "{} is in {}'s list.".format(topic, nick())
    else:
        msg = "{} is not in {}'s list.".format(topic, nick())
    return statement(msg)

#---------------------------------------------------------------------------
#                      USER IDENTITY
#---------------------------------------------------------------------------

@ask.intent("GreetMeIntent")
def greet_me():
    msg = "Hello {}!".format(nick())
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
    return statement(msg)

#--------------------------------------------------------------------------
#                       SOCIAL MEDIA
#--------------------------------------------------------------------------

#implement later???
@ask.intent("CheckFacebookIntent")
def check_facebook():
    pass

@ask.intent("PostToFacebookIntent")
def post_facebook():
    pass

@ask.intent("CheckTwitterIntent")
def check_twitter():
    pass

@ask.intent("PostToTwitterIntent")
def post_twitter():
    pass

if __name__ == '__main__':
    app.run(debug=True)

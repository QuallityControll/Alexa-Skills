from flask import Flask
from flask_ask import Ask, statement, question, session
import face_recognition_2 as fr
from userdata import Userdata
import pickle

app = Flask(__name__)
ask = Ask(app, '/')

"""
(INTENT SCHEMA)
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

(SAMPLE UTTERANCES)
UpdateUserIntent update user
UpdateUserIntent update me
UpdateUserIntent who am i
UserNickNameIntent make my nickname {amazing boy|nickname}
UserNickNameIntent call me {Johnny|nickname}
RemoveUserNicknameIntent remove my nickname
RemoveUserNicknameIntent stop calling me by my nickname
RemoveUserNicknameIntent call be my my normal name
AddToListIntent Add {something|topic} to my list.
RemoveFromListIntent Remove {get chicken|topic} from my list.
RemoveFromListIntent Take {find Jason|topic} off my list.
ClearListIntent Clear my list.
ClearListIntent Clear list.
ListListIntent List my list.
ListListIntent Tell me everything on my list
ListListIntent Whats on my list
ListListIntent Whats in my list
CheckListIntent See if {get eggs|topic} is on my list.
CheckListIntent Is {call Amy|topic} on my list
CheckListIntent do i have {go to doctors|topic}
GreetMeIntent Greet me
GreetMeIntent Say hi to me
GreetMeIntent whats up
GreetMeIntent hows it going
GreetMeIntent hi
GreetMeIntent hello
GreetMeIntent whats good
SingMeHappyBirthdayIntent Sing me happy birthday
SingMeHappyBirthdayIntent Its my birthday
SingMeHappyBirthdayIntent I hate the birthday song
ConfirmIdentityIntent Who am i
ConfirmIdentityIntent confirm my identity
ConfirmIdentityIntent what is my name
ConfirmIdentityIntent what is my real name

"""



#import userdata with pickle

try:
    with open("userdata.pkl","rb") as f:
        userdata = pickle.load(f)
except:
    userdata = Userdata()

#load face recognition database
fr.load()

#set up name to nickname dictionary in session variables,
#so nickname will be available during current session.
if "name_to_nickname" not in session.attributes:
    session.attributes["name_to_nickname"] = {}
    for user in userdata.user_history:
        if user in userdata.user_nicknames:
            session.attributes["name_to_nickname"][user] = userdata.user_nicknames[user]
        else:
            session.attributes["name_to_nickname"][user] = user

@app.route('/')
def homepage():
    return "Hello"

def user():
    """
    Accesses the session object and returns the name of the current user as
    a string. If the name is unavailable, returns "User" as a dummy username.
    """
    try:
        if session.attributes["user_name"] is None:
            return "User"
        else:
            return session.attributes["user_name"]
    except:
        return "User"

def nick():
    """
    Accesses the nicknames database in userdata. If a nickname exists, returns
    the user's nickname as a string. If a nickname does not exist, returns
    the name of the current user (e.g calls user()).
    """
    try:
        if userdata.usernicknames[user()] is None:
            return user()

        else:
            return userdata.usernicknames[user()]
    except:
        return user()

def save_userdata():
    """
    Saves all userdata to a file with pickle, by dumping the userdata
    object to "userdata.pkl".
    """
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
    """
    For sake of clarity, the "acting user" is the person talking to alexa, while
    the "current user" is the username stored in the session.attributes
    dictionary. This function updates the current user so that it is the same
    as the acting user. Using the camera and Face Recognition tool, the function
    attempts to recognize the acting user. The current user is then updated
    only if exactly one person is seen and if that person is recognized
    by the database.
    """
    #database must be loaded again in case new people have been added
    #during the current session
    import face_recognition_2 as fr
    fr.load()
    print("Database loaded.")

    #use face recognition tool to attempt to identify acting user
    name_list = fr.identify()

    #error handling
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
        #change current user in session object
        session.attributes["user_name"] = name

        #update nickname dictionary in session object
        session.attributes["name_to_nickname"][name] = userdata.user_nicknames[name]

        #log new user in user history
        userdata.user_history.add(name)
        save_userdata()

    #return statment logging action
    return statement("Updated user to {}".format(nick()))

#slot: {newname}
@ask.intent("UserNickNameIntent")
def update_user_nickname(nickname):
    """
    Updates the nickname of the current user to a given nickname.

    Parameters
    ----------
    nickname: [String]
        A string containing the new nickname for the current user.

    Returns
    -------
    Updates both the userdata and session attributes objects by
    adding [name]:[nickname] to their respective dictionaries.
    """

    #update nickname dictionary in userdata object and save it to file
    userdata.usernicknames[user()] = nickname
    save_userdata()

    #update session attributes name_to_nickname dictionary
    session.attributes["name_to_nickname"][name] = userdata.user_nicknames[name]

    #return statement logging action
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
    """
    The current user's list is a python List of strings that is modifiable
    by voice command. This function adds a given topic/phrase to the current
    user's list.

    Parameters
    ----------
    topic: [String]
        A string containing the phrase to add to the list.

    Returns
    -------
    Appends topic to the current user's list.
    """
    #error detection
    if topic is None:
        return statement("Could not understand item to add.")

    #append topic to user's list and save userdata
    userdata.user_lists[user()].append(topic)
    save_userdata()

    #return statement logging action
    return statement("Added {} to {}'s list".format(topic, nick()))

@ask.intent("RemoveFromListIntent")
def remove_from_list(topic):
    """
    Removes a given topic/phrase from the current user's list.

    Parameters
    ----------
    topic: [String]
        A string containing the phrase to remove from the list.

    Returns
    -------
    Removes topic from the current user's list.
    """
    #error detection
    if topic is None:
        return statement("Could not understand item to remove.")

    #remove object from user's list and save userdata
    userdata.user_lists[user()].remove(topic)
    save_userdata()

    #return statement logging action
    return statement("Removed {} from {}'s list".format(topic, nick()))

@ask.intent("ClearListIntent")
def clear_list():
    """
    Clears the current user's list entirely.
    """
    #clear user's list and save userdata
    userdata.user_lists[user()].clear()
    save_userdata()

    #return statement logging action
    return statement("Cleared {}'s list".format(nick()))

@ask.intent("ListListIntent")
def list_list():
    """
    Returns a statement listing all phrases contained in the current
    user's list.
    """

    joined_list = ", ".join(userdata.user_lists[user()])
    return statement("Here is {}'s list: {}.".format(nick(), joined_list))

@ask.intent("CheckListIntent")
def check_list(topic):
    """
    Checks if a given topic/phrase exists in the current user's list.

    Parameters
    ----------
    topic: [String]

    """

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
    """
    Greets current user.
    """
    msg = "Hello {}!".format(nick())
    return statement(msg)

@ask.intent("SingMeHappyBirthdayIntent")
def sing_happy_birthday():
    """
    Sings happy birthday to user.
    """
    msg = """
            Happy birthday to you,
            Happy birthday to you,
            Happy birthday dear {},
            Happy birthday to you
        """.format(nick())
    return statement(msg)

@ask.intent("ConfirmIdentityIntent")
def confirm_identity():
    """
    Confirms identity of user. This returns a statement containing
    the raw username, not the nickname.
    """
    msg = "The current user is {}".format(user())
    return statement(msg)


if __name__ == '__main__':
    app.run(debug=True, port=5004)

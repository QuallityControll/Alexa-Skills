from flask import Flask
from flask_ask import Ask, statement, question
import News_Buddy as nb

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    return "Hello"

@ask.launch
def start_skill():
    nb.update_via_rss_feed("http://feeds.reuters.com/reuters/scienceNews")
    nb.save()
    return question("What would you like to know?") \
        .reprompt("I didn't get that. What would you like to know?")

#slots: {topic}
@ask.intent("WhatsNewIntent")
def whats_new(topic):
    msg = nb.new_with(topic)
    return statement(msg)

@ask.intent("AssociatedWithEntityIntent")
#slots: {entity}
def associated_with_entity(entity, num_entities=3):
    entity_list = nb.most_associated_with_entity(entity, num_entities = num_entities)
    if len(entity_list) == 0:
        msg = "I can't find anything associated with {}.".format(entity)

    else:
        entities = ", ".join(entity_list)
        msg = "For things associated with {}, I found {}.".format(entity, entities)
    return statement(msg)

#slots: {entity}
@ask.intent("AssociatedWithPhraseIntent")
def associated_with_phrase(phrase, num_entities=3):
    entity_list = nb.most_associated_with_phrase(entity, num_entities = num_entities)
    if len(entity_list) == 0:
        msg = "I can't find anything associated with {}.".format(entity)

    else:
        entities = ", ".join(entity_list)
        msg = "For things associated with {}, I found {}.".format(entity, entities)
    return statement(msg)

@ask.intent("LoadDataIntent")
def load_data():
    nb.update_via_rss_feed("http://feeds.reuters.com/reuters/scienceNews")
    nb.save()
    msg = "Data loaded."
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)

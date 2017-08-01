from flask import Flask
from flask_ask import Ask, statement, question, session
import News_Buddy as nb
import Face Recognition as fr

app = Flask(__name__)
ask = Ask(app, '/')

#for topic in topic_to_url:
    #nb.update_via_rss_feed(topic_to_url[topic])
nb.save()

@app.route('/')
def homepage():
    return "Hello"

@ask.launch
def start_skill():
    return question("Hello, {}. What would you like to do?".format(session.attributes[user_name]))
        .reprompt("I don't understand. What would you like me to do?")

@ask.intent("UpdateUserIntent")
def update_user():
    name_list = fr.identify()
    if len(name_list)==0:
        return statement("I see noone.")
    elif len(name_list)>1:
        return statement("I see multiple people.")
    name = namelist[0]
    if name == "Not Recognized"
        return statement("I don't recognize you.")
    else:
        session.attributes[user_name] = name

    return statement(msg)

@ask.intent("AssociatedWithIntent")
#slots: {topic}
def associated_with_entity(topic, num_entities=3):
    tokens = nltk.word_tokenize(topic)
    tagged_tokens = nltk.pos_tag(tokens)
    named_entities = nltk.ne_chunk(tagged_tokens)

    named_entities_list = []
    for i in range(0, len(named_entities)):
        ents = named_entities.pop()
        if getattr(ents, 'label', None) != None and ents.label() == "NE":
            named_entities_list.append([ne for ne in ents])

    entity_strings = []
    for named_entity in named_entities_list:
        entity_strings.append(" ".join(named_entity))

    if len(entity_strings) > 0:
        associated_entity_list = nb.most_associated_with_entity(entity_strings[0], \
                                                    num_entities = 3)
    else:
        associated_entity_list = nb.most_associated_with_phrase(topic, \
                                                    num_entities = 3)


    if len(associated_entity_list) > 0:
        msg = "For things associated with {}, I found".format(topic) + \
                ", ".join(associated_entity_list[:-1]) + \
                ", and " + associated_entity_list[-1] + "."

    else:
        msg = "I found nothing associated with {}.".format(topic)

    return statement(msg)

#slots: {newsTopic}
@ask.intent("LoadDataIntent")
def load_data(newsTopic):
    nb.update_via_rss_feed(topic_to_url[newsTopic])

    nb.save()
    msg = "{} news loaded.".format(newsTopic)
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)

#load data upon initialization
load_data("all")

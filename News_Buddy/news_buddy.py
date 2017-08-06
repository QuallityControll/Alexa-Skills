# (INTENT SCHEME)
# {
#   "intents": [
#     {
#       "intent": "WhatsNewIntent",
#       "slots": [
#         {
#           "name": "topic",
#           "type": "AMAZON.LITERAL"
#         }
#       ]
#     },
#     {
#       "intent": "AssociatedWithIntent",
#       "slots": [
#         {
#           "name": "topic",
#           "type": "AMAZON.LITERAL"
#         }
#       ]
#     },
#     {
#       "intent": "LoadDataIntent",
#       "slots": [
#         {
#           "name": "newsTopic",
#           "type": "NEWS_TOPICS"
#         }
#       ]
#     }
#   ]
# }

# (CUSTOM SLOT)
# NAME: NEWS_TOPICS
# arts
# business
# company
# entertainment
# environment
# health
# lifestyle
# wealth
# popular
# odd
# people
# politics
# science
# sports
# technology
# top
# domestic
# global
# world

# (SAMPLE UTTERANCES)
# WhatsNewIntent whats new with {movies|topic}
# WhatsNewIntent whats up with {movies|topic}
# WhatsNewIntent whats going on with {movies|topic}
# WhatsNewIntent how are {movies|topic}
#
# AssociatedWithIntent whats associated with {Trump|topic}
# AssociatedWithIntent what are things associated associated with {Trump|topic}
# AssociatedWithIntent what things are associated associated with {Trump|topic}
# AssociatedWithIntent whats related to {Trump|topic}
# AssociatedWithIntent what are things related to {Trump|topic}
# AssociatedWithIntent what things are related to {Trump|topic}
#
# LoadDataIntent load {newsTopic} news
# LoadDataIntent import {newsTopic} news
# LoadDataIntent load news about {newsTopic}
# LoadDataIntent import news about {newsTopic}

from flask import Flask
from flask_ask import Ask, statement, question
import News_Buddy as nb
import nltk

app = Flask(__name__)
ask = Ask(app, '/')

topic_to_url = {
    "arts":"http://feeds.reuters.com/news/artsculture",
    "business":"http://feeds.reuters.com/reuters/businessNews",
    "company":"http://feeds.reuters.com/reuters/companyNews",
    "entertainment":"http://feeds.reuters.com/reuters/entertainment",
    "environment":"http://feeds.reuters.com/reuters/environment",
    "health":"http://feeds.reuters.com/reuters/healthNews",
    "lifestyle":"http://feeds.reuters.com/reuters/lifestyle",
    "wealth":"http://feeds.reuters.com/news/wealth",
    "popular":"http://feeds.reuters.com/reuters/MostRead",
    "odd":"http://feeds.reuters.com/reuters/oddlyEnoughNews",
    "people":"http://feeds.reuters.com/reuters/peopleNews",
    "politics":"http://feeds.reuters.com/Reuters/PoliticsNews",
    "science":"http://feeds.reuters.com/reuters/scienceNews",
    "sports":"http://feeds.reuters.com/reuters/sportsNews",
    "technology":"http://feeds.reuters.com/reuters/technologyNews",
    "top":"http://feeds.reuters.com/reuters/topNews",
    "domestic":"http://feeds.reuters.com/Reuters/domesticNews",
    "global":"http://feeds.reuters.com/Reuters/worldNews"
    }

for topic in topic_to_url:
    nb.update_via_rss_feed(topic_to_url[topic])
nb.save()

@app.route('/')
def homepage():
    return "Hello"

@ask.launch
def start_skill():
    return question("What would you like to know?") \
        .reprompt("I didn't get that. What would you like to know?")

#slots: {topic}
@ask.intent("WhatsNewIntent")
def whats_new(topic):
    msg = nb.new_with(topic)
    if msg == "Input phrase not found.":
        msg = "I couldn't find anything new about {}.".format(topic)
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
    if newsTopic == "all":
        for topic in topic_to_url:
            nb.update_via_rss_feed(topic_to_url[topic])
    
    nb.update_via_rss_feed(topic_to_url[newsTopic])

    nb.save()
    msg = "{} news loaded.".format(newsTopic)
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True, port=5003)

#load data upon initialization
load_data("all")

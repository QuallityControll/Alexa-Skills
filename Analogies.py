from flask import Flask
from flask_ask import Ask, statement, question
from collections import defaultdict
import numpy as np
import time
import gensim
from gensim.models.keyedvectors import KeyedVectors
from sklearn.decomposition import TruncatedSVD



"""
Intent Scheme:
{
  "intents": [
    {
      "slots": [
        {
          "name": "first",
          "type": "AMAZON.LITERAL"
        },
        {
          "name": "second",
          "type": "AMAZON.LITERAL"
        },
        {
          "name": "third",
          "type": "AMAZON.LITERAL"
        }
      ],
      "intent": "AnalogyIntent"
    }
  ]
}

Sample Utterances:

AnalogyIntent {king|first} is to {queen|second} as {man|third} is to

"""

path = "glove.6B.50d.txt.w2v" # Make sure you have this file in the directory
glove = KeyedVectors.load_word2vec_format(path, binary=False)

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    return "Hello"


@ask.launch
def start_skill():
    msg = "What analogy do you want to do?"
    return question(msg)

@ask.intent("AnalogyIntent")
def Analogy(first, second, third):
	n = len(glove.vocab)
	d = 50
	X_glove = np.zeros((n, d))
	for i, word in enumerate(glove.vocab.keys()):
	    X_glove[i,:] = glove[word]
	svd = TruncatedSVD(n_components=2)
	svd.fit(X_glove)
	query = glove[third] - glove[first] + glove[second]
	a = glove.similar_by_vector(query)[0][0]
	if a == third:
		a = glove.similar_by_vector(query)[1][0]
	return statement(a)

if __name__ == '__main__':
    app.run(debug=True)

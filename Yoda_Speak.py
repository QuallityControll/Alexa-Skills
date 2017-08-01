from flask import Flask
from flask_ask import Ask, statement, question
import urllib

"""
Intent Scheme:

{
  "intents": [
    {
      "slots": [
        {
          "name": "phrase",
          "type": "AMAZON.LITERAL"
        }
      ],
      "intent": "PhraseIntent"
    }
  ]
}

Sample Utterances:

PhraseIntent {I am doing things|phrase}
"""

app = Flask(__name__)
ask = Ask(app, '/')

mashapeAuthorization = "MASHAPE_KEY"

@app.route('/')
def homepage():
    return "Hello"

@ask.launch
def start_skill():
    msg = "Say a phrase."
    return question(msg)

@ask.intent("PhraseIntent")
def yoda_speak(phrase):
   	opener = urllib.request.build_opener()
   	opener.addheaders = [("X-Mashape-Authorization", mashapeAuthorization)]
   	socket = opener.open("https://yoda.p.mashape.com/yoda?sentence=" + phrase)
   	content = socket.read()
   	socket.close()
   	return statement(content)

if __name__ == '__main__':
    app.run(debug=True)
  
#ATIS

from bs4 import BeautifulSoup

import requests

from flask import Flask
from flask_ask import Ask, statement, question
import requests
import time
import unidecode
import json

app = Flask(__name__)
ask = Ask(app, '/')


def split(string):
    temp = ''
    for num in string:
        temp += num + ' '

    return temp

def convertToSpeech(ATIS):
    ATIS = ATIS[:ATIS.find("RMK") - 1]
    print(ATIS)
    ATIS = ATIS.split(' ')
    print(ATIS)
    for i in range(len(ATIS)):
        print(ATIS[i])
        if i == 0:
            ATIS[i] = (split(ATIS[i]))
        elif i == 1:
            ATIS[i] = ". " + split(ATIS[i][2:6]) + ' zulu. '
        elif i == 2:
            ATIS[i] = "winds, " + ATIS[i][:3] + " at " + ATIS[i][3:5] + " knots. "
        elif i == 3:
            ATIS[i] = "visibility, " + ATIS[i][:2] + " statute miles. "
        elif i == len(ATIS) - 2:
            ATIS[i] = "tempurature " + ATIS[i][:2] + ", dew point " + ATIS[i][3:] + "."
        elif i == len(ATIS) - 1:
            ATIS[i] = " altimeter " + split(ATIS[i][1:])
        else:
            #print(ATIS[i])
            temp = ATIS[i][:3]
            if temp == 'FEW':
                temp = 'few'
            elif temp == 'SCT':
                temp = 'scattered'
            elif temp == 'CLR':
                temp = 'clear'
            elif temp == 'OVC':
                temp = 'overcast'
            elif temp == 'BKN':
                temp = 'broken'
            #print(ATIS[i])

            if temp == 'broken' or temp == 'few' or temp == 'clear' or temp == 'scattered' or temp == 'overcast':
                if temp == 'clear':
                    ATIS[i] = temp + " ."
                else:
                    ATIS[i] = temp + ATIS[i][3:] + " ."
            else:
                ATIS[i] = ''



    temp = ""

    for item in ATIS:
        temp += item
    print(temp)
    return temp






#####
@ask.intent("GetWeather")
def getHTML(AirportName):
    #print(AirportName)
    AirportName = AirportName[::3]
    print(AirportName)
    url = "http://aviationweather.gov/metar/data?ids=" + AirportName + "&format=raw&date=0&hours=0"
    print(url)
    r = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data, "lxml")

    div = soup.find("div", {"id": "awc_main_content"})
        # soup.prettify()


    div = str(div)

    beg = div.find(AirportName.upper())
    end = div.find("<br/>",beg)
    atis = div[beg:end]
    atis_return = convertToSpeech(atis)
    return statement(atis_return)
    #return statement(AirportName)

@app.route('/')
def homepage():
    return "ATIS"

@ask.launch
def start_skill():
    msg = "Which airport should I get the ay tis from?"
    return question(msg)

if __name__ == '__main__':
    app.run(debug=True)
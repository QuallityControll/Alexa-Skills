app = Flask(__name__)
ask = Ask(app, '/')
"""
{
  "intents": [
    {
      "slots": [
        {
          "name": "length",
          "type": "NUMBER"
        }
      ],
      "intent": "RecordSong"
    }
  ]
}

RecordSong Record for {five | length} seconds
RecordSong Record for {ten | length} seconds
RecordSong Record for {twenty | length} seconds
RecordSong Record for {fourty | length} seconds
RecordSong {five | length} seconds
RecordSong {ten | length} seconds
RecordSong {twenty | length} seconds
RecordSong {fourty | length} seconds
"""

@app.route('/')
def homepage():
    return "Song FP"

@ask.launch
def start_skill():
    msg = "how long would you like me to record for?"
    return question(msg)

@ask.intent("RecordSong")
def MicCheck(length):
    """

    :param length: how long you want to record for - int
    :return: perceentage confidence of song
    """
    print(length)
    length = (int(length))

    #return statement(length)
    MicPeaks = mic_to_numpy_array(length)
    print("Mic reocrded")
    #return statement("checl")
    Stemp, f, t = spectogram(MicPeaks)
    MicPeaksTemp = peaks(Stemp)
    print("Mic peaks gotten")
    peaksMicFinal = convertData(MicPeaksTemp)
    print("Mic data converted")

    #return statement('dipppp')
    temp =  check_database(peaksMicFinal, length)

    if temp[1] < .32:#32
        return statement("I am not sure")
    else:
        return statement("I am " + str(temp[1]) + " percent confident that the song is " + str(temp[0]) + '.')
    #print(returnn)
    #if returnn == "I am not sure":
    #    msg = returnn
    #else:
    #    msg = "I am " + returnn[1] + " percent confident that the song is " + returnn[0] + '.'
    #print(msg)
    #print(type(returnn))
    #print(type(msg))
    #return statement("asdasdasdasdsdasd")
    #return statement(str(length))

if __name__ == '__main__':
    app.run(debug=True)

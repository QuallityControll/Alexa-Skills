Gets the automatic terminal information service about any specifiec airport based on its reference code.

Alexa Skill:
  Name: ATIS

  Invocation Name: automatic terminal information service
  
  Intent Schematic:
  ```{
  "intents": [
    {
      "slots": [
        {
          "name": "AirportName",
          "type": "LITERAL"
        }
      ],
      "intent": "GetWeather"
    }
  ]
}


GetWeather get the atis for {k. h. p. n.| AirportName}
GetWeather get the atis for {k. j. f. k.| AirportName}
GetWeather get the atis for {k. l. a. x.| AirportName}
GetWeather get atis for {k. l. g. a.| AirportName}
GetWeather get atis for {k. a. t. l.| AirportName}
GetWeather {k. h. p. n.| AirportName}
GetWeather {k. j. f. k.| AirportName}
GetWeather {k. a. t. l.| AirportName}
GetWeather {k. g. f. g.| AirportName}
  

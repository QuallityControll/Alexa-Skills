Face Recognition skill

This file contains the Face Recognition skill. Paste the intent scheme and sample utterances into their respective locations on the amazon developer page.


INTENT SCHEME

```
{
  "intents": [
    {
      "slots": [
        {
          "name": "firstname",
          "type": "AMAZON.US_FIRST_NAME"
        }
      ],
      "intent": "AddIntent"
    },
    {
      "intent": "RecognizeIntent"
    },
    {
      "intent": "ListIntent"
    },
    {
      "slots": [
        {
          "name": "firstname",
          "type": "AMAZON.US_FIRST_NAME"
        }
      ],
      "intent": "RemoveIntent"
    }
  ]
}
```

SAMPLE UTTERANCES

```
AddIntent add {firstname}
RecognizeIntent recognize
RecognizeIntent identify
ListIntent list
RemoveIntent remove {firstname}
```

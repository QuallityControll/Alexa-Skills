Intent Schema
```
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
```

Sample Utterances

```
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
```

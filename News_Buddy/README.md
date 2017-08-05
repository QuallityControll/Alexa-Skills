Intent Scheme
```
{
  "intents": [
    {
      "intent": "WhatsNewIntent",
      "slots": [
        {
          "name": "topic",
          "type": "AMAZON.LITERAL"
        }
      ]
    },
    {
      "intent": "AssociatedWithIntent",
      "slots": [
        {
          "name": "topic",
          "type": "AMAZON.LITERAL"
        }
      ]
    },
    {
      "intent": "LoadDataIntent",
      "slots": [
        {
          "name": "newsTopic",
          "type": "NEWS_TOPICS"
        }
      ]
    }
  ]
}
```

Custom Slot
```
NAME: NEWS_TOPICS
arts
business
company
entertainment
environment
health
lifestyle
wealth
popular
odd
people
politics
science
sports
technology
top
domestic
global
world
```

Sample Utterances
```
WhatsNewIntent whats new with {movies|topic}
WhatsNewIntent whats up with {movies|topic}
WhatsNewIntent whats going on with {movies|topic}
WhatsNewIntent how are {movies|topic}

AssociatedWithIntent whats associated with {Trump|topic}
AssociatedWithIntent what are things associated associated with {Trump|topic}
AssociatedWithIntent what things are associated associated with {Trump|topic}
AssociatedWithIntent whats related to {Trump|topic}
AssociatedWithIntent what are things related to {Trump|topic}
AssociatedWithIntent what things are related to {Trump|topic}

LoadDataIntent load {newsTopic} news
LoadDataIntent import {newsTopic} news
LoadDataIntent load news about {newsTopic}
LoadDataIntent import news about {newsTopic}
```

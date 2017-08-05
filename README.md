# Installation

Install Face_Recognition, Song_Fingerprint and News_Buddy from their respective repositories on this github page.
Each repository will have its own readme with installation instructions. Then clone this repository to a directory from which
you would like to run your alexa skills.

# Skill Setup

Register as an amazon developer on [Amazon](https://developer.amazon.com/). On the developer.amazon.com page, click "Skills" and "Add New Skill".

In this repository each skill is contained within a seperate folder which will have its own README file with the IntentSchema and Sample Utterances(these can be changed according to your tastes).

After specifying the title and invocation name (The statement which will activate the skill,preferablly the title or a shortened version of the title), copy and paste the Intent Schema and Sample Utterances to their respective boxes. If there is a custom slot in the README, create that by putting in the specified name and pasting in 
the slot list.

For the configuration, any service can be used which will forward traffic from the given url to the localhost. We reccomend
using [ngrok](https://github.com/inconshreveable/ngrok) you can follow the insturctions on the ngrok website.

Testing the alexa skill is easy under the "test" tab on the developer page. If you enter sample utterances for the respective
skill, functionality can be tested without setting up Alexa.

# Alexa

[This page](https://alexa.amazon.com/spa/index.html) gives instructions for setting up the alexa device. Once it is set up, run the python files for the skills you want and make sure service is being forward to your computer(ngrok).

Everything should be working now. Activate a skill with its invocation name and enjoy your cognitive assistant!

For help, post on the issues tab and we will be happy to help with troubleshooting.

The Quality Control Team

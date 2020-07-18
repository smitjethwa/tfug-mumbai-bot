# tfug-mumbai-bot

Telegram Bot to manage collections of Learning Material

**Functionalities:**
- /tutorials
- /courses
- /blogs
- /events

---
![Database](https://github.com/smitjethwa/tfug-mumbai-bot/blob/master/img/7.png)
![Database](https://github.com/smitjethwa/tfug-mumbai-bot/blob/master/img/8.png)


## How to use?
### 1. Create a Telegram bot using [Bot Father](https://telegram.me/BotFather)
Use the `/newbot` command to create a new bot. The BotFather will ask you for a name and username, then generate an authorization token for your new bot.
The name of your bot is displayed in contact details and elsewhere.
The Username is a short name, to be used in mentions and t.me links. Usernames are 5-32 characters long and are case insensitive, but may only include Latin characters, numbers, and underscores. Your bot's username **must** end in 'bot', e.g. '`tetris_bot`' or '`TetrisBot`'.
The token is a string along the lines of `110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw` that is required to authorize the bot and send requests to the Bot API. Keep your token secure and store it safely, it can be used by anyone to control your bot.
### 2. Fork and Clone this repository.
### 3. Get all required packages/Library using [`pip install -r requirements.txt`](requirements.txt)
### 4. Change Telegram Authorization Token [Here](https://github.com/smitjethwa/tfug-mumbai-bot/blob/master/bot.py#L10)
### 5. Edit [Command lists](https://github.com/smitjethwa/tfug-mumbai-bot/blob/master/bot.py#L141:L148) as per your requirements. 
### 6. Database
I have used Firebase Realtime Database to store the data.
![Database](https://github.com/smitjethwa/tfug-mumbai-bot/blob/master/img/1.PNG)

You can use any database, just replace the queries. If you are using Firebase Realtime database, Set up [Admin Database API](https://firebase.google.com/docs/database/admin/start?authuser=0) and Download `serviceAccountKey.json` and insert Firebase URL in the [code](https://github.com/smitjethwa/tfug-mumbai-bot/blob/master/bot.py#L18)
### Deployment
TFUG Mumbai Bot is deployed on [Heroku](http://heroku.com/)
- Create heroku project ```heroku create```
- Insert App_link in [code](https://github.com/smitjethwa/tfug-mumbai-bot/blob/master/bot.py#L154)
- Create a new Git repository ```git init```
- Add files ```git add .```
- Commit the change ```git commit -m "first commit"```
- Change “YourAppName” to the name of your heroku app```heroku git:remote -a YourAppName```
- Push everything to the server```git push heroku master```

### Tada! Done!! 


import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

TOKEN = '1361748338:AAEG53stqIhZUn5sA5WTA-qY_XyeH-5LdsU'
ADMINS = ['smitjethwa']
FIREBASE_TOKEN = "hey-smit-firebase-adminsdk-52vpd-86c5806a19.json"
PORT = int(os.environ.get('PORT', 5000))

cred = credentials.Certificate(FIREBASE_TOKEN)
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tfug-mumbai.firebaseio.com',
    'databaseAuthVariableOverride': None
})

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


BLOG_EMOJI = u'\U0001F538'
TUTORIAL_EMOJI = u'\U0001F4DA'
COURSE_EMOJI = u'\U0001F4D9'
EVENT_EMOJI = u'\U0001F3A4'


def get_blog():
    ref = db.reference('/admin/blogs/').get()
    dict_key = []
    dict_value = []
    for x in list(ref)[0:]:
        dict_key.append(x)
        dict_value.append(ref[x])
    # return dict_key,dict_value 
    complete_list = []
    for i in range(len(dict_value)):
        individual_list = []
        individual_list.append(dict_value[i]['blog_title'])
        individual_list.append(dict_value[i]['blog_url'])
        complete_list.append(individual_list)
    return complete_list

def get_tutorial():
    ref = db.reference('/admin/tutorials/').get()
    dict_key = []
    dict_value = []
    for x in list(ref)[0:]:
        dict_key.append(x)
        dict_value.append(ref[x])
    # return dict_key,dict_value 
    complete_list = []
    for i in range(len(dict_value)):
        individual_list = []
        individual_list.append(dict_value[i]['tutorial_platform'])
        individual_list.append(dict_value[i]['tutorial_title'])
        individual_list.append(dict_value[i]['tutorial_url'])
        complete_list.append(individual_list)
    return complete_list

def get_course():
    ref = db.reference('/admin/courses/').get()
    dict_key = []
    dict_value = []
    for x in list(ref)[0:]:
        dict_key.append(x)
        dict_value.append(ref[x])
    # return dict_key,dict_value 
    complete_list = []
    for i in range(len(dict_value)):
        individual_list = []
        individual_list.append(dict_value[i]['course_platform'])
        individual_list.append(dict_value[i]['course_title'])
        individual_list.append(dict_value[i]['course_url'])
        complete_list.append(individual_list)
    return complete_list

def get_event():
    ref = db.reference('/admin/events/').get()
    dict_key = []
    dict_value = []
    for x in list(ref)[0:]:
        dict_key.append(x)
        dict_value.append(ref[x])
    # return dict_key,dict_value 
    complete_list = []
    for i in range(len(dict_value)):
        individual_list = []
        individual_list.append(dict_value[i]['event_date'])
        individual_list.append(dict_value[i]['event_link'])
        individual_list.append(dict_value[i]['event_name'])
        individual_list.append(dict_value[i]['event_location'])
        complete_list.append(individual_list)
    return complete_list

def start(bot, update):
    user_first_name = update.effective_user.first_name
    """Send a message when the command /start is issued."""
    message_to_be_send = f'<b>Hi {user_first_name}</b>! \nRead TensorFlow blogs via /blogs or explore more using /help'
    update.message.reply_text(message_to_be_send,parse_mode=telegram.ParseMode.HTML)

def help(bot, update):
    """Send a message when the command /help is issued."""
    message_to_be_send = '''
    You can use the following commands!\n
    <b>Read Blogs : </b> /blogs 
    <b>Learn via Tutorials: </b> /tutorials
    <b>Community Events: </b> /events
    <b>Certification or course: </b> /courses
    <b>Online Presence: </b> /social_media
    '''
    update.message.reply_text(message_to_be_send,parse_mode=telegram.ParseMode.HTML)

def blogs(bot, update):
    """Send a message when the command /help is issued."""
    complete_list = get_blog()
    message_to_be_send = []
    for i in range(len(complete_list)):
        blog_title = complete_list[i][0]
        blog_url = complete_list[i][1]
        message_to_be_send.append(f'{BLOG_EMOJI} <b>{i+1}. {blog_title}</b> {BLOG_EMOJI}\n<b>URL: </b>{blog_url}')
    output_text = "\n\n".join(message_to_be_send) 
    update.message.reply_text(output_text,parse_mode=telegram.ParseMode.HTML)
  
def tutorials(bot, update):
    """Send a message when the command /help is issued."""
    complete_list = get_tutorial()
    message_to_be_send = []
    for i in range(len(complete_list)):
        tutorial_platform = complete_list[i][0]
        tutorial_title = complete_list[i][1]
        tutorial_url = complete_list[i][2]
        message_to_be_send.append(f'{TUTORIAL_EMOJI} <b>{i+1}. {tutorial_title}</b> {TUTORIAL_EMOJI}\n<b>Platform: </b>{tutorial_platform}\n<b>URL: </b>{tutorial_url}')
    output_text = "\n\n".join(message_to_be_send) 
    update.message.reply_text(output_text,parse_mode=telegram.ParseMode.HTML)

def events(bot, update):
    """Send a message when the command /help is issued."""
    complete_list = get_event()
    message_to_be_send = []
    for i in range(len(complete_list)):
        event_date = complete_list[i][0].split('-')
        event_link = complete_list[i][1]
        event_name = complete_list[i][2]
        event_location = complete_list[i][3]
        event_date = '-'.join(event_date[::-1])
        message_to_be_send.append(f'{EVENT_EMOJI} <b>{i+1}. {event_name}</b> {EVENT_EMOJI}\n<b>Date: </b>{event_date}\n<b>Location: </b>{event_location}\nRegister: {event_link}')
    output_text = "\n\n".join(message_to_be_send) 
    update.message.reply_text(output_text,parse_mode=telegram.ParseMode.HTML)

def courses(bot, update):
    """Send a message when the command /help is issued."""
    complete_list = get_course()
    message_to_be_send = []
    for i in range(len(complete_list)):
        course_platform = complete_list[i][0]
        course_title = complete_list[i][1]
        course_url = complete_list[i][2]
        message_to_be_send.append(f'{COURSE_EMOJI} <b>{i+1}. {course_title}</b> {COURSE_EMOJI}\n<b>Platform: </b>{course_platform}\n<b>URL: </b>{course_url}')
    output_text = "\n\n".join(message_to_be_send) 
    update.message.reply_text(output_text,parse_mode=telegram.ParseMode.HTML)

def social_media(bot, update):
    """Send a message when the command /help is issued."""
    message_to_be_send = '''
    Be a part of TFUG Mumbai.
    Telegram : <a href="https://t.me/tfugmumbai">@tfugmumbai</a>
    <a href="https://www.instagram.com/tensorflowmumbai/">Follow us on Instagram</a>
    <a href="https://twitter.com/tfugmumbai">Follow us on Twitter</a>
    <a href="https://www.meetup.com/tfugmumbai/">Join Meetup Group</a>
    <a href="https://www.youtube.com/channel/UCMlfIpRC-995awLMUzdHSIg">Subscribe our YouTube channel</a>
    '''
    update.message.reply_text(message_to_be_send,parse_mode=telegram.ParseMode.HTML)

def echo(update, context):
    update.message.reply_text("Unsupported Command! Check /help")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('blogs',blogs))
    dp.add_handler(CommandHandler('tutorials',tutorials))
    dp.add_handler(CommandHandler('events',events))
    dp.add_handler(CommandHandler('courses',courses))
    dp.add_handler(CommandHandler('social_media',social_media))
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://tfugmumbai-bot.herokuapp.com/' + TOKEN)
    updater.idle()
    
if __name__ == '__main__':
    main()
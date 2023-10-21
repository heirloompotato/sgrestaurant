from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import constants as const
import keyboardBuilder as kb
import json
import filters as f
import initiationDB as db
import os


TOKEN = '1813893791:AAHRhU7SnLpNtZ9c5FJ_N2pX6-14L2sseLo'
PORT = int(os.environ.get('PORT', 13978))

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=const.first_text.format(update.effective_chat["first_name"]))
    update.message.reply_text(const.second_text, reply_markup=kb.price_initial_markup)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=const.help_text)

def restart(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=const.restart_text)
    update.message.reply_text(const.second_text, reply_markup=kb.price_initial_markup)

def review(update, context):
    result = db.getByChatId(update.effective_chat.id)
    message = db.reviewCleanUp(result) 
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def button(update, context) -> None:
    query = update.callback_query
    query.answer() #must be answered if not will have errors
    querydata = json.loads(query["data"]) #looks like [stage, "ac", "e"]
    if querydata[0] == 0:
        query.edit_message_text(text=const.second_text, reply_markup=kb.markup_editor(querydata, kb.price_keyboard_markup, 1))
    elif querydata[0] == 1:
        query.edit_message_text(text=const.third_text, reply_markup=kb.markup_editor(querydata, kb.rating_keyboard_markup, 2))
    elif querydata[0] == 2:
        query.edit_message_text(text=const.fourth_text, reply_markup=kb.markup_editor(querydata, kb.cuisine_keyboard_markup, 3))
    elif querydata[0] == 3:
        query.edit_message_text(text=const.fifth_text, reply_markup=kb.markup_editor(querydata, kb.location_keyboard_markup, 4))
    elif querydata[0] == 4:
        end_point_df = (f.filter(querydata, db.df)).sample(frac=1).head()
        query.edit_message_text(text=const.last_text)
        for i in range(len(end_point_df)):
            restaurant = end_point_df.iloc[i]['Restaurant']
            link = end_point_df.iloc[i]['Link']
            final_message = "How about {}? \nFind out more here \n{}".format(restaurant, link) #test dats affordable, 1 , cafe, paya
            context.bot.send_message(chat_id=update.effective_chat.id, text=final_message)
        context.bot.send_message(chat_id=update.effective_chat.id, text="That's all the options.")
        db.insertData(querydata, update.effective_chat.id)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=const.error)


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    restart_handler = CommandHandler('restart', restart)
    review_handler = CommandHandler('review', review)
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    unknown_handler = MessageHandler(Filters.text | (~Filters.command), unknown)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(restart_handler)
    dispatcher.add_handler(review_handler)
    dispatcher.add_handler(unknown_handler)

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.setWebhook('https://sgfoodpicker.herokuapp.com/' + TOKEN)
    #using polling for testing
    # updater.start_polling()
    
    updater.idle()


if __name__ == "__main__":
    main()



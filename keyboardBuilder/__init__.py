import json
import constants as const
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def markup_editor(querydata, kb, stage):

    kb = kb.to_dict()

    for kbline in kb['inline_keyboard']:

        for button in kbline:

            if button["text"] == "I'm done picking":
                querydata[0] += 1
                callback = json.dumps(querydata)
                button["callback_data"] = callback
            else:
                newquerydata = querydata.copy()
                if button["callback_data"] in newquerydata[stage]:
                    newquerydata[stage] = newquerydata[stage].replace(button["callback_data"], "")
                    button["text"] += " ✔"
                else:
                    newquerydata[stage] += button["callback_data"]

                callback = json.dumps(newquerydata)
                button["callback_data"] = callback
                # print(str(newquerydata))

    return kb

def kb_builder(dict):
    keyboard = []
    for alpha, text in dict.items():
        buttonline = [InlineKeyboardButton(text, callback_data=alpha)]
        keyboard.append(buttonline)
    return keyboard

def kb_builder_2r(dict):
    keyboard = []
    limit = len(dict)
    i = 0
    alpha_list = list(dict.keys())
    text_list = list(dict.values())
    if limit % 2 != 0:
        limit -= 1
        while i < limit:
            buttonline = [InlineKeyboardButton(text_list[i], callback_data=alpha_list[i]), InlineKeyboardButton(text_list[i+1], callback_data=alpha_list[i+1])]
            keyboard.append(buttonline)
            i += 2
        keyboard.append([InlineKeyboardButton(text_list[limit], callback_data=alpha_list[limit])])
    else:
        while i < limit:
            buttonline = [InlineKeyboardButton(text_list[i], callback_data=alpha_list[i]), InlineKeyboardButton(text_list[i+1], callback_data=alpha_list[i+1])]
            keyboard.append(buttonline)
            i += 2
    return keyboard


#making the keyboard constantnts
price_keyboard_markup = InlineKeyboardMarkup(kb_builder(const.price_dict))
rating_keyboard_markup = InlineKeyboardMarkup(kb_builder_2r(const.rating_dict))
cuisine_keyboard_markup = InlineKeyboardMarkup(kb_builder_2r(const.cuisine_dict))
location_keyboard_markup = InlineKeyboardMarkup(kb_builder_2r(const.location_dict))
price_initial_markup = markup_editor(const.base_query_data, price_keyboard_markup, 1)
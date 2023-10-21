import pandas as pd
import sqlite3
import os

import constants as const


#initiate RESTAURANT database
df = pd.read_csv("../app/database/Restaurant Database - Sheet1.csv") #heroku path
# df = pd.read_csv("database/Restaurant Database - Sheet1.csv") #local path for testing

#clean up table
df.drop(axis=1, columns=["linkParser"], inplace=True) 

#intiate USER databse
# DATABASE = os.environ.get("DATABASE_URL", "user.db") #postgres table not working
DATABASE = "user.db"

#functions to for USER database
def getByChatId(chatId):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    query = ''' SELECT * FROM user WHERE chatId = {}'''.format(chatId) #table is "_user" for prod
    result = cursor.execute(query)
    row = result.fetchone()
    print(row)
    return row

def insertData(queryData, chatId): #data looks like this[4, 'a', 'bd', '', '']
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    queryData[0] = chatId
    queryData[1] = str(list(map(const.price_dict.get, queryData[1])))
    queryData[2] = str(list(map(const.rating_dict.get, queryData[2])))
    queryData[3] = str(list(map(const.cuisine_dict.get, queryData[3])))
    queryData[4] = str(list(map(const.location_dict.get, queryData[4])))
    qd_tuple = tuple(queryData)

    query = ''' REPLACE INTO user (chatId, price, rating, location, cuisine) VALUES(?,?,?,?,?) ''' #table is "_user" for prod
    cursor.execute(query, qd_tuple)
    connection.commit()

def reviewCleanUp(row):
    #do map in func above n store data as the real word itself
    message = f"Your last selections \nPrice : {row[1]} \nRating : {row[2]} \nCuisine : {row[3]} \nLocation : {row[4]}"
    return message







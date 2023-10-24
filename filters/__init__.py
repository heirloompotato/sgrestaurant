import constants as const

def filter(queryData, df):
    price = list(map(const.pDict.get, queryData[1]))
    if len(queryData[2]) > 0:
        rating_str = list(map(const.rDict.get, queryData[2]))
        rating = [int(i) for i in rating_str]
    else:
        rating = []
    cuisine = list(map(const.cDict.get, queryData[3]))
    location = list(map(const.lDict.get, queryData[4]))

    if len(price) > 0:
        df = df[df["Price"].isin(price)]
    if len(rating) > 0:
        df = df[df["Rating"].isin(rating)] #int
    if len(cuisine) > 0:
        df = df[df["Cuisine"].isin(cuisine)]
    if len(location) > 0:
        df = df[df["Location"].isin(location)]

    return df






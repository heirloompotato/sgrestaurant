# Constants for price list check

base_query_data = [0, "", "", "", ""]
price_list = ["Affordable", "Mid-range", "High-end", "I'm done picking"]
rating_list = ["1", "2", "3", "4", "5", "I'm done picking"]
location_list = ["Paya Lebar", "Tanjong Pagar", "Telok Ayer", "Esplanade", "Orchad",\
                                       "Changi", "Eunos", "Hougang", "City Hall", "Farrer Park", "Little India",\
                                       "Somerset", "Dhoby Ghaut", "Bugis", "Pasir Ris", "Ang Mo Kio",\
                                       "Yishun", "Clementi", "Dover", "Jurong", "Kallang", "I'm done picking"]
cuisine_list = ["Cafe", "Korean", "Chinese", "Indian", "Halal", "Japanese", "Vegetarian", "I'm done picking"]

#const for filters
alphabet_list = ["a", "b", "c", "d", 'e', "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
price_dict = dict(zip(alphabet_list, price_list)) #rating numbers are still string
rating_dict = dict(zip(alphabet_list, rating_list))
location_dict = dict(zip(alphabet_list, location_list))
cuisine_dict = dict(zip(alphabet_list, cuisine_list))

#const without I'm done picking
pDict = price_dict.copy()
pDict.popitem()
rDict = rating_dict.copy()
rDict.popitem()
cDict = cuisine_dict.copy()
cDict.popitem()
lDict = location_dict.copy()
lDict.popitem()

# Constants for standard text messages
first_text = "Hey {}! Unsure and hungry? You've come to the right place! Let's start picking!"
second_text = "Choose your price range:"
third_text = "Choose the rating of the restaurant:"
fourth_text = "Pick the type of cuisine you want!"
fifth_text = "Where do you want to eat?"
last_text = "Here are some options available!"
help_text = "/start to begin the food picker \n/restart to restart your food choice \n/review to see your previous choices"
restart_text = "Starting from the top again!"
error = "Sorry we don't understand this message. /start to begin your food picking."
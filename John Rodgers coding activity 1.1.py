__title__ = "Coding activity 1, OpenWeather API"
__author__ = "John Rodgers"
# Documentation used: https://openweathermap.org/current

import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "insert API"
# use your api key here
UNITS = "imperial"
# constants because these do not need to change, user is assumed to be in CONUS
favorites = {}
command = "start"
# empty declarations

def add_favorite(city, response):
    
    if city not in favorites and len(favorites) < 3:
        favorites[city] = response
        print(city + " was added to your favorites.")
    elif city in favorites:
        print("That city is already in your favorites list.")
    elif len(favorites) == 3:
        print("Your favorites list is at maximum capacity (3). Please remove a city if you wish to add another.")
# function to add a favorite city to the list


def remove_favorite(removed_city):
    if removed_city in favorites:
        favorites.pop(removed_city)
        print(removed_city + " was removed.")
    else:
        print(removed_city + " is not in your favorites list.")
# function to remove a favorite city from the list

def format_output(city, response):

    temp_max = response['main']['temp_max']
    temp_min = response['main']['temp_min']
    temp_fahrenheit = response['main']['temp']
    feels_like_fahrenheit = response['main']['feels_like']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    wind_speed = response['wind']['speed']
    # json output formatting

    print(f"For {city}:\n\n"
    f"The current conditions are: {description}\n"
    f"The current temperature is: {temp_fahrenheit}°F\n"
    f"The minimum temperature is: {temp_min}°F\n"
    f"The maximum temperature is: {temp_max}°F\n"
    f"It currently feels like {feels_like_fahrenheit}°F\n"
    f"The wind speed is: {wind_speed} MPH"
    )
#function to format output

print("This program accepts a city and outputs the current weather for that city.\n")
print("Commands:\n\nSearch: check a city's weather\nFavorites: view your favorites list\nRemove: remove an item from your favorites list\n" \
"Add: add an item to your favorites list\nEnd: close program\n")
print("Note: add a city to your favorites before searching the next city.\n")
# command list

while command != "end":

    command = input("Enter command:").strip().lower()

    match command:
        case "search": 
            city = input("Enter your city:")
            url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=" + UNITS
            # url for submitting api request

            response = requests.get(url).json()
            # send api request with appended information

            format_output(city, response)
            # output

        case "favorites":
            if len(favorites) == 0: 
                print("You do not have any cities stored in your favorites list.")
                
            else: 
                print("\nFavorite cities:\n")
                for city in favorites:
                    format_output(response)
        # check favorites 

        case "add":
            add_favorite(city, response)
        # add city to favorites

        case "remove":
            removed_city = input("which city would you like to remove?")
            remove_favorite(removed_city)
        # remove city from favorites










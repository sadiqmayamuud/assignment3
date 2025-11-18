# https://github.com/sadiqmayamuud/assignment3

import json

# This script is getting data from local data.json
# (Fallback method due to API changes)
# Students will still implement GBP and EUR retrieval using the same logic shown in showUsd().

# Local JSON file path

url = "data.json"


def fetch_prices():
    """
    This function loads Bitcoin pricing data from data.json.
    """
    with open(url, "r", encoding="utf-8") as file:
        return json.load(file)


def showUsd():
    """
    This function loads Bitcoin's current price in USD from local JSON file.
    """
    jsonResponse = fetch_prices()   # loading data
    time = jsonResponse["time"]["updated"]     # getting time from response
    code = jsonResponse["bpi"]["USD"]["code"]  # getting currency code
    rate = jsonResponse["bpi"]["USD"]["rate"]  # getting price in USD

    print(time, code, rate)


def showGbp():
    # Your code will go here, similar to showUsd()
    # Remove 'pass' once you are done editing your code.
    pass


def showEuro():
    # Your code will go here, similar to showUsd()
    # Remove 'pass' once you are done editing your code.
    def showeuro():
        data = fetch_prices()
        print("Bitcoin Price in EUR:", data["bpi"]["EUR"]["rate"])


while True:
    try:
        print("1. Show Bitcoin Price in USD.")
        print("2. Show Bitcoin Price in GBP.")
        print("3. Show Bitcoin Price in EUR.")
        userInput = int(input("Please Enter Your Choice: "))

        if userInput == 1:
            showUsd()
            break
        elif userInput == 2:
            showGbp()
            break
        elif userInput == 3:
            showEuro()
            break
        else:
            print("Something Went Wrong, Please Try Again...")
            continue

    except:
        print("Something Went Wrong, Quitting...")
        break
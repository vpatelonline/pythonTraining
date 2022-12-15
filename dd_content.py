import csv
import random

# Get rendom quote from qt,csv filw
def get_random_quote(quote_files="qt.csv"):
    try:
        with open(quote_files) as csvfile:
            quotes=[{'author':line[0], 'quote':line[1]} for  line in csv.reader(csvfile, delimiter='|')]
    
    except Exception as e:
            quotes=[{'author':'Eric','quote':"xxxxxxxxx"}]

            return random.choice(quotes)




def get_weather_forecast():
    pass

def get_twitter_trends():
    pass

def get_wikipedia_article():
    pass


if __name__=='__main__':
    print('\nTesting quote generation')

    quote = get_random_quote()
    print(f'-Random quote is "{quote["quote"]}" - {quote["author"]}')

    quote = get_random_quote(quote_files = None)
    print(f'-Default quote is "{quote["quote"]}" - {quote["author"]}')

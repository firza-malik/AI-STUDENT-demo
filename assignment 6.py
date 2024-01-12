
#QUESTION NO1:
def calculate_ticket_price(age, day, num_tickets):
    base_price = 0

    if age == "adult":
        base_price = 10
    elif age == "child":
        base_price = 5
    elif age == "senior":
        base_price = 8

    if day == "weekend":
        base_price += 2
    if num_tickets >= 5:
        discount_percentage = 0.1 
        base_price -= base_price * discount_percentage

    return base_price * num_tickets

ticket_age = "adult"
ticket_day = "weekend"
num_of_tickets = int(input("Enter a number:"))
total_price = calculate_ticket_price(ticket_age, ticket_day, num_of_tickets)

print(f"Total ticket price for {num_of_tickets} {ticket_age} tickets on {ticket_day}: ${total_price}")

#question 2:

def calculate_total_bill(items, quantities, prices, discount_rate=0, tax_rate=0, split_friends=1):
    if len(items) != len(quantities) or len(quantities) != len(prices):
        return "Error: Mismatched input lengths."

    total_cost = sum(quantities[i] * prices[i] for i in range(len(items)))

    
    total_cost -= total_cost * (discount_rate / 100)

  
    total_cost += total_cost * (tax_rate / 100)
    total_cost /= split_friends

    return total_cost

items = ["Item1", "Item2", "Item3"]
quantities = [2, 1, 3]
prices = [10.0, 5.0, 8.0]

total_bill = calculate_total_bill(items, quantities, prices, discount_rate=10, tax_rate=5, split_friends=3)
print(f"Total Bill: ${total_bill:.2f}")

#QUESTION NO 3

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from collections import Counter


nltk.download('vader_lexicon')
nltk.download('punkt')


def is_emoji(char):
    emoji_set = {'😊', '😃', '😢', '😠', '😐', '🙂', '😍', '🙁', '😂', '😎'}
    return char in emoji_set


def analyze_social_media_post(post):
    words = word_tokenize(post)
    sia = SentimentIntensityAnalyzer()

sentiment_score = sia.polarity_scores(post)['compound']
if sentiment_score >= 0.05:
        sentiment = "positive"
elif sentiment_score <= -0.05:
        sentiment = "negative"
else:
        sentiment = "neutral"


keywords = [word.lower() for word in words if word.isalnum()]
emojis = [char for char in post if is_emoji(char)]
emoji_counter = Counter(emojis)
trending_emojis = [emoji for emoji, count in emoji_counter.items() if count > 1]

return {
        'sentiment': sentiment,
        'keywords': keywords,
        'emojis': emojis,
        'trending_emojis': trending_emojis
    }


def main():
    social_media_post = input("Enter your social media post: ")
    result = analyze_social_media_post(social_media_post)


    print("\nAnalysis Result:")
    print("Sentiment:", result['sentiment'])
    print("Keywords:", ', '.join(result['keywords']))
    print("Emojis:", ', '.join(result['emojis']))
    print("Trending Emojis:", ', '.join(result['trending_emojis']))


if __name__ == "__main__":
    main()
    
#QUESTION NO 4

def estimate_travel_cost(destination, transportation_cost, accommodation_cost, activities_cost, travel_style='budget', duration=7):
    if travel_style == 'budget':
        budget_multiplier = 1.0
    elif travel_style == 'luxury':
        budget_multiplier = 1.5
    else:
        raise ValueError("Invalid travel style. Choose 'budget' or 'luxury'.")

    total_cost = (transportation_cost + accommodation_cost + activities_cost) * budget_multiplier * duration
    return f"Estimated travel cost for {destination} ({travel_style} style, {duration} days): ${total_cost:.2f}"

destination = "Paris"
transportation_cost = 500
accommodation_cost = 800
activities_cost = 300
estimated_cost = estimate_travel_cost(destination, transportation_cost, accommodation_cost, activities_cost, travel_style='budget', duration=10)
print(estimated_cost)

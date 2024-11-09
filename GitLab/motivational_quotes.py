import random

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
        "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
        "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("Here's your motivational quote for the day:")
    print(get_random_quote())
    print("Hi bro wassup")
    print("Hi bro wassup!!!!")

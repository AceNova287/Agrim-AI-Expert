from textblob import TextBlob
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "Welcome to Sentiment Spy!\n")
sentence = input(Fore.YELLOW + "Type a sentence : ")

blob = TextBlob(sentence)
polarity = blob.sentiment.polarity

print("\n Analyzing Statement...")

if polarity > 0.2 :
    print(Fore.GREEN + "Positive sentiment detected!")
elif polarity < -0.2 :
    print(Fore.RED + "Negative sentiment detected!")
else:
    print(Fore.YELLOW + "Neutral sentiment detected!")

print(Style.DIM + f"(Polarity Score: {polarity})")
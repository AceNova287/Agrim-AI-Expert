import re, random
from colorama import Fore, init

init(autoreset=True)
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
     "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

def normalize_input (text):
    return re.sub("r\s+", " ", text.strip().lower())
def recommend():
    print(Fore.CYAN + "Travel bot: Beaches, mountains or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.CYAN + f"Travel bot: How about visiting {suggestion}?")
        print(Fore.CYAN + "Travel bot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.CYAN + "Travel bot: Great! Have a wonderful trip!")
        elif answer == "no":
            print(Fore.CYAN + "Travel bot: No worries! Let's try again.")
            recommend()
        else:
            print(Fore.RED + "Travel bot: I didn't understand that. Let's start over.")
    else:
        print(Fore.RED + "Travel bot: I didn't catch that. Please choose from beaches, mountains, or cities.")

    show_help()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to? ")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days? ")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: For a trip to {location} for {days} days, pack essentials like clothes, toiletries, and any specific items based on the weather and activities planned. Safe travels!")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.CYAN + "TravelBot: I can help you with the following commands:")
    print(Fore.CYAN + "- 'recommend': Get travel destination recommendations.")
    print(Fore.CYAN + "- 'packing': Get packing tips for your trip.")
    print(Fore.CYAN + "- 'joke': Hear a travel-related joke.")
    print(Fore.CYAN + "- 'help': Show this help message.")
    print(Fore.CYAN + "Type exit or bye to end!\n")

def chat():
    print(Fore.CYAN + "Hello! I am TravelBot, your virtual travel assistant.")
    name  = input(Fore.YELLOW + "TravelBot: What's your name? \nYou: ")
    print(Fore.CYAN + f"TravelBot: Nice to meet you, {name}! How can I assist you today?")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Thank you for chatting! Have a great day!")
            break
        else:
            print(Fore.RED + "TravelBot: I'm sorry, I didn't understand that. Type 'help' to see what I can do.")

if __name__ == "__main__":
    chat()
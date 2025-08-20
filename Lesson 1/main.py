print("Hi, Welcome to ChatBot!")
name = input("What's your name? ")
print(f"Hello {name}, Nice to meet you")
print("How are you feeling today? (good/bad) : ")
mood = input().lower()
if mood == "good" or mood == "Good":
    print("That's great to hear!")
elif mood == "bad" or mood == "Bad":
    print("I'm sorry to hear that.")
else:
    print("Sometimes its hard to express your feeling.")

print(f"It was nice chatting with you {name}. Goodbye!")
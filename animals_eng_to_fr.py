translations={   
     "lion": "le lion",
    "wolf": "le loup",
    "cat": "le chat",
    "dog": "le chien",
    "snake": "le serpent",
    "bird": "l'oiseau",
    "horse": "le cheval",
    "rabbit": "le lapin",
    "spider": "l'araignée"
    }
print("WELCOME TO THE ENGLISH TO FRENCH ANIMAL TRANSLATOR!")
word=input("Enter an animal in English to translate it to French").lower()
if word in translations:
    print(f"The translation of {word} is {translations[word]}")
else:
    print(f"Sorry, {word} is not in the dictionary.")
    response=input("Would you like to view the list of available animals? (yes/no)").lower()
    if response=="yes":
        for eng,fr in translations.items():
            print(f"{eng}:{fr}")

 
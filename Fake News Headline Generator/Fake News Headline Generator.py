# FAKE NEWS HEADLINE GENERATOR

#  import random module 
import random

# Subject List 
subjects = ['Mahira Khan – Actress',
            'Babar Azam – Cricketer',
            'Atif Aslam – Singer',
            'Imran Khan – Politician & Former Cricketer',
            'Sajal Aly – Actress',
            'Fawad Khan – Actor/Singer',
            'Wasim Akram – Legendary Cricketer',
            'Mehwish Hayat – Actress/Model',
            'Hamza Ali Abbasi – Actor/Activist',
            'Hania Aamir – Actress/Social Media Star']


# Actions List
actions = ['do random dance',
           'boop your own nose',
           'laugh without reason',
           'talk to a plant',
           'run like Naruto',
           'eat chips without hands',
           'hide from your shadow',
           'wear socks on hands',
           'sleep with eyes open',
           'fight with a mosquito']


# Objects List
objects = ['a flying slipper',
           'your invisible friend',
           'a dancing tomato',
           'the angry ceiling fan',
           'a confused pigeon',
           'a crying onion',
           'a ghost in the fridge',
           'your lost sock',
           'a sleepy laptop',
           'a banana with WiFi']


# Function to generate a random fake news headline

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    object = random.choice(objects)

    headline = f"BREAKING NEWs: Do you know {subject} {action} with {object}."

    print("\n" + headline)

    option = input("\nDo you want to generate another News (yes/no):").strip().lower()
    if option == "no":
        break

print("\nThanks for using Fake News Headline Generator. Have a fun chilled day.")


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

#  Home Function
def optSelect():
    while True:
        print("1. Generate Random News \n2. Add on your data \n3 Exit")
        try:
            select = int(input("\nChoose an option: "))
        except ValueError:
            print("Wrong input! make sure you select from available options.\n")
        except Exception:
            print("invalid Input! Try Again\n")
        else:
            break
    return select

def fileSave(text):
    with open("F:\PY PROJECTS\Fake News Headline Generator\noStore Generated Headlines.txt", 'a') as saveNews:
        saveNews.write(text)
    print("Successfully Stored in Memory.")
    return None

# Getting return value from Home Func
while True:
        
    select1 = optSelect()

    # Match the options
    match select1:
        case 1:
            # Generate News
            while True:
                subject = random.choice(subjects)
                action = random.choice(actions)
                object = random.choice(objects)

                headline = f"BREAKING NEWs: Do you know {subject} {action} with {object}."

                print("\n" + headline)
                fileSave(headline)

                option = input("\nDo you want to generate another News (yes/no):").strip().lower()
                if option == "no":
                    break
                    # optSelect() 
                    # After selecting option 1 (generate news), jab tum "no" likh dete ho, woh wapis optSelect() ko call karta hai, lekin uska return value handle hi nahi kar raha — isliye woh select1 ki old value (1) use karta rehta hai.            #    

            print("\nThanks for using Fake News Generator 😎")
        case 2:
            #  Add-on list 
            print("What you want to add on to List. \n\n1. Subjects \n2. Actions \n3. Objects \n4. Exit")
            
            select2 = int(input("\nChoose an option: "))
            
            match select2:
                case 1:
                    add_on_Subject = input("Enter the Subject to add in list: ").strip()
                    subjects.append(add_on_Subject)
                    print("Subject successfully added in List!")
                case 2:
                    add_on_Action = input("Enter the Action to add in list: ").strip()
                    actions.append(add_on_Action)
                    print("Action successfully added in List!")
                case 3:
                    add_on_Object = input("Enter the Object to add in list: ").strip()
                    objects.append(add_on_Object)
                    print("Object successfully added in List!")
                case 4:
                    print("Thanks for using Fake News Generator 😎")
                    quit()
                case _:
                    print("Invalid Option! Try Again")  
        case 3:
            # Exist Program
            print("\nhanks for using Fake News Generator 😎")
            quit()
        case _:
            # Handling invalid Input
            print("Invalid Option! Try Again")
            
        
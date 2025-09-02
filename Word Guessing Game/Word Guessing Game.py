# Word Guessing Game
import random

easy_words = [
    "cat", "dog", "sun", "book", "milk",
    "tree", "ball", "car", "shoe", "fish",
    "hat", "cup", "rain", "star", "baby",
    "door", "hand", "chair", "water", "home"
]
medium_words = [
    "window", "garden", "purple", "planet", "rocket",
    "dancer", "summer", "bottle", "forest", "pencil",
    "silver", "breeze", "candle", "camera", "pillow",
    "bridge", "hunter", "yellow", "glider", "mountain"
]
hard_words = [
    "curious", "gentle", "confident", "brilliant", "challenge",
    "freedom", "pioneer", "inspire", "mystery", "imagine",
    "adventure", "distant", "journey", "believer", "explore",
    "fortune", "rescue", "whisper", "vision", "miracle"
]

print("Welcome To Word Guessing Game")
print("=============================")
print("\nChoose a difficulty level: easy, medium or hard")

level = input("Enter difficulty: ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid Choice! Defaulting to easy level.")
    secret = random.choice(easy_words)

attempts = 0

print("\n--- -- - Guess the Word - -- ---")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratualtions you guess the correct word in {attempts} attempts")
        break

    hint = ""

    for i in range(len(secret)):
        if i<len(guess) and guess[i] == secret[i]:
            hint += guess[i] # hint = hint + guess[1]
        else:
            hint += "_"
    print("Hint: ", hint)

print("Game Over")
import random
import os

# Define the list of questions and answers about Hawaii
questions = [
    {
        "question": "What is the capital of Hawaii?",
        "answer": "Honolulu"
    },
    {
        "question": "What is the name of the active volcano on the Big Island of Hawaii?",
        "answer": "Kilauea"
    },
    {
        "question": "What is the name of the famous beach on the North Shore of Oahu?",
        "answer": "Waimea Bay"
    },
    {
        "question": "What is the name of the Hawaiian dish made with raw fish?",
        "answer": "Poke"
    },
    {
        "question": "What is the name of the Hawaiian goddess of fire and volcanoes?",
        "answer": "Pele"
    },
    {
        "question": "What is the name of the Hawaiian king who united the islands?",
        "answer": "Kamehameha"
    },
    {
        "question": "What is the name of the Hawaiian flower necklace?",
        "answer": "Lei"
    },
    {
        "question": "What is the name of the Hawaiian instrument made from a gourd?",
        "answer": "Ukulele"
    },
    {
        "question": "What is the name of the Hawaiian word for hello?",
        "answer": "Aloha"
    },
    {
        "question": "What is the name of the Hawaiian word for goodbye?",
        "answer": "Aloha"
    },
    {
        "question": "What is the name of the Hawaiian word for thank you?",
        "answer": "Mahalo"
    },
    {
        "question": "What is the name of the Hawaiian word for family?",
        "answer": "Ohana"
    },
    {
        "question": "What is the name of the Hawaiian word for delicious?",
        "answer": "Ono"
    },
    {
        "question": "What is the name of the Hawaiian word for love?",
        "answer": "Aloha"
    },
    {
        "question": "What is the name of the Hawaiian word for ocean?",
        "answer": "Kai"
    },
    {
        "question": "What is the name of the Hawaiian word for mountain?",
        "answer": "Mauna"
    },
    {
        "question": "What is the name of the Hawaiian word for water?",
        "answer": "Wai"
    },
    {
        "question": "What is the name of the Hawaiian word for rainbow?",
        "answer": "Anuenue"
    },
    {
        "question": "What is the name of the Hawaiian word for turtle?",
        "answer": "Honu"
    },
    {
        "question": "What is the name of the Hawaiian word for shark?",
        "answer": "Mano"
    },
    {
        "question": "What is the name of the Hawaiian word for fish?",
        "answer": "I'a"
    },
    {
        "question": "What is the name of the Hawaiian word for flower?",
        "answer": "Pua"
    },
    {
        "question": "What is the name of the Hawaiian word for star?",
        "answer": "Hoku"
    },
    {
        "question": "What is the name of the Hawaiian word for sun?",
        "answer": "La"
    },
    {
        "question": "What is the name of the Hawaiian word for moon?",
        "answer": "Mahina"
    },
    {
        "question": "What is the name of the Hawaiian word for wind?",
        "answer": "Makani"
    },
    {
        "question": "What is the name of the Hawaiian word for rain?",
        "answer": "Ua"
    },
    {
        "question": "What is the largest town on the Big Island?",
        "answer": "Hilo"
    },
    {
        "question": "What is the name of the town on the Big Island where the Kona coffee is grown?",
        "answer": "Kona"
    },
    {
        "question": "What is the name of the town in between Kona and Hilo on the Big Island? (Arel lives here)",
        "answer": "Waimea"
    },
    {
        "question": "What is the name of the tallest mountain in the world? (It's in Hawaii)",
        "answer": "Mauna Kea"
    },
    {
        "question": "How many freeways are there on the Big Island?",
        "answer": "Zero"
    },
    {
        "question": "What year did Hawaii become a state?",
        "answer": "1959"
    },
    {
        "question": "What year did Hawaii become a US territory?",
        "answer": "1898"
    },
    {
        "question": "What year did Captain Cook discover Hawaii?",
        "answer": "1778"
    },
    {
        "question": "What year did the first Polynesians arrive in Hawaii?",
        "answer": "500"
    },
    {
        "question": "What year did the first Hawaiians arrive in Hawaii?",
        "answer": "300"
    },
    {
        "question": "Who was the last Hawaiian monarch?",
        "answer": "Queen Liliuokalani"
    },
    {
        "question": "What is the largest island in Hawaii?",
        "answer": "Big Island"
    },
    {
        "question": "What is the second largest island in Hawaii?",
        "answer": "Maui"
    },
    {
        "question": "What is the third largest island in Hawaii?",
        "answer": "Oahu"
    },
    {
        "question": "What is the smallest island in Hawaii?",
        "answer": "Kahoolawe"
    },
    {
        "question": "What is the name of the island in Hawaii where the state capital is located?",
        "answer": "Oahu"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous road to Hana is located?",
        "answer": "Maui"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous Waikiki beach is located?",
        "answer": "Oahu"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous lava flows are located?",
        "answer": "Big Island"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous leper colony is located?",
        "answer": "Molokai"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous Napali coast is located?",
        "answer": "Kauai"
    }
]

# Check if leaderboard file exists, if not create one
if not os.path.exists("leaderboard.txt"):
    with open("leaderboard.txt", "w") as f:
        f.write("Name,Score\n")

# Load the leaderboard from a file
with open("leaderboard.txt", "r") as f:
    leaderboard = [line.strip().split(",") for line in f]

# Welcome message
print("Welcome to the Hawaii Trivia Game!")
print("Type 'quit' at any time to exit the game and see the leaderboard.")

# Ask the user for their name
name = input("What is your name? ")

# Shuffle the list of questions
random.shuffle(questions)

# Initialize the score
score = 0

# Loop through the questions and ask the user each question
for question in questions:
    print(question["question"])
    answer = input("Enter your answer: ")
    if answer.lower() == question["answer"].lower():
        print("Correct!")
        score += 1
    elif answer.lower() == "quit":
        break
    else:
        print("Incorrect. The correct answer is " + question['answer'] + ".")

# Add the user's name and score to the leaderboard
if name.lower() == "clear":
    with open("leaderboard.txt", "w") as f:
        f.write("Name,Score\n")
else:
    leaderboard.append([name, str(score)])

    # Create a new list that only contains entries where the score is a number
    numeric_leaderboard = [
        entry for entry in leaderboard if entry[1].isdigit()]

    # Sort the numeric_leaderboard by score in descending order
    numeric_leaderboard.sort(key=lambda x: int(x[1]), reverse=True)

    # Display the leaderboard to the user
    print("LEADERBOARD")
    print("-----------")
    for i, (name, score) in enumerate(numeric_leaderboard):
        print("{0}. {1}: {2}".format(i+1, name, score))

    # Save the updated leaderboard to a file
    with open("leaderboard.txt", "w") as f:
        for name, score in numeric_leaderboard:
            f.write("{},{}\n".format(name, score))

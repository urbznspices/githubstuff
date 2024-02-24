from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
from random import shuffle, sample

app = Flask(__name__)
app.secret_key = 'SpencerStrider'

# Define the list of questions and answers about Hawaii
questions = [
    {
        "question": "What is the capital of Hawaii?",
        "choices": ["Honolulu", "Hilo", "Kona", "Lahaina"],
        "answer": "Honolulu"
    },

    {
        "question": "What is the name of the active volcano on the Big Island of Hawaii?",
        "choices": ["Mauna Kea", "Mauna Loa", "Kilauea", "Haleakala"],
        "answer": "Kilauea"
    },
    {
        "question": "What is the name of the famous beach on the North Shore of Oahu?",
        "choices": ["Waikiki", "Lanikai", "Waimea Bay", "Hanauma Bay"],
        "answer": "Waimea Bay"
    },
    {
        "question": "What is the name of the Hawaiian dish made with raw fish?",
        "choices": ["Poke", "Lomi Lomi Salmon", "Kalua Pig", "Laulau"],
        "answer": "Poke"
    },
    {
        "question": "What is the name of the Hawaiian goddess of fire and volcanoes?",
        "choices": ["Pele", "Hi'iaka", "Laka", "Kapo"],
        "answer": "Pele"
    },
    {
        "question": "What is the name of the Hawaiian king who united the islands?",
        "choices": ["Kalakaua", "Kamehameha", "Lunalilo", "Kamehameha II"],
        "answer": "Kamehameha"
    },
    {
        "question": "What is the name of the Hawaiian flower necklace?",
        "choices": ["Haku", "Lei", "Kukui", "Maile"],
        "answer": "Lei"
    },
    {
        "question": "What is the name of the Hawaiian instrument made from a gourd?",
        "choices": ["Steel Guitar", "Ukulele", "Slack Key Guitar", "Ipu Heke"],
        "answer": "Ukulele"
    },
    {
        "question": "What is the name of the Hawaiian word for hello?",
        "choices": ["Mahalo", "Aloha", "Ohana", "Ono"],
        "answer": "Aloha"
    },
    {
        "question": "What is the name of the Hawaiian word for goodbye?",
        "choices": ["Mahalo", "Ohana", "Aloha", "Ono"],
        "answer": "Aloha"
    },
    {
        "question": "What is the name of the Hawaiian word for thank you?",
        "choices": ["Aloha", "Ohana", "Ono", "Mahalo"],
        "answer": "Mahalo"
    },
    {
        "question": "What is the name of the Hawaiian word for family?",
        "choices": ["Mahalo", "Ohana", "Aloha", "Ono"],
        "answer": "Ohana"
    },
    {
        "question": "What is the name of the Hawaiian word for delicious?",
        "choices": ["Mahalo", "Ohana", "Aloha", "Ono"],
        "answer": "Ono"
    },
    {
        "question": "What is the name of the Hawaiian word for love?",
        "choices": ["Mahalo", "Ohana", "Aloha", "Ono"],
        "answer": "Aloha"
    },
    {
        "question": "What is the name of the Hawaiian word for ocean?",
        "choices": ["Kai", "Wai", "Anuenue", "Honu"],
        "answer": "Kai"
    },
    {
        "question": "What is the name of the Hawaiian word for mountain?",
        "choices": ["Kai", "Wai", "Anuenue", "Mauna"],
        "answer": "Mauna"
    },
    {
        "question": "What is the name of the Hawaiian word for water?",
        "choices": ["Kai", "Wai", "Anuenue", "Honu"],
        "answer": "Wai"
    },
    {
        "question": "What is the name of the Hawaiian word for rainbow?",
        "choices": ["Kai", "Wai", "Anuenue", "Honu"],
        "answer": "Anuenue"
    },
    {
        "question": "What is the name of the Hawaiian word for turtle?",
        "choices": ["Kai", "Wai", "Anuenue", "Honu"],
        "answer": "Honu"
    },
    {
        "question": "What is the name of the Hawaiian word for shark?",
        "choices": ["Pua", "I'a", "Mano", "Hoku"],
        "answer": "Mano"
    },
    {
        "question": "What is the name of the Hawaiian word for fish?",
        "choices": ["Pua", "Hoku", "Mano", "I'a"],
        "answer": "I'a"
    },
    {
        "question": "What is the name of the Hawaiian word for flower?",
        "choices": ["I'a", "Hoku", "Mano", "Pua"],
        "answer": "Pua"
    },
    {
        "question": "What is the name of the Hawaiian word for star?",
        "choices": ["I'a", "Pua", "Mano", "Hoku"],
        "answer": "Hoku"
    },
    {
        "question": "What is the name of the Hawaiian word for sun?",
        "choices": ["I'a", "Hoku", "La", "Hoku"],
        "answer": "La"
    },
    {
        "question": "What is the name of the Hawaiian word for moon?",
        "choices": ["Aloha", "Makani", "La", "Mahina"],
        "answer": "Mahina"
    },
    {
        "question": "What is the name of the Hawaiian word for wind?",
        "choices": ["Mauka", "Mahina", "Makani", "Makai"],
        "answer": "Makani"
    },
    {
        "question": "What is the name of the Hawaiian word for rain?",
        "choices": ["Mauka", "Waiwai", "Makani", "Ua"],
        "answer": "Ua"
    },
    {
        "question": "What is the largest town on the Big Island?",
        "choices": ["Kona", "Hilo", "Waimea", "Pahoa"],
        "answer": "Hilo"
    },
    {
        "question": "What is the name of the town on the Big Island where the Kona coffee is grown?",
        "choices": ["Hilo", "Waimea", "Kona", "Pahoa"],
        "answer": "Kona"
    },
    {
        "question": "What is the name of the town in between Kona and Hilo on the Big Island? (Arel lives here)",
        "choices": ["Waimea", "Pahoa", "Honokaa", "Kealakekua"],
        "answer": "Waimea"
    },
    {
        "question": "What is the name of the tallest mountain in the world? (It's in Hawaii)",
        "choices": ["Mount Everest", "Mauna Loa", "Mauna Kea", "Kilauea"],
        "answer": "Mauna Kea"
    },
    {
        "question": "How many freeways are there on the Big Island?",
        "choices": ["One", "Two", "Three", "Zero"],
        "answer": "Zero"
    },
    {
        "question": "What year did Hawaii become a state?",
        "choices": ["1959", "1898", "1778", "500"],
        "answer": "1959"
    },
    {
        "question": "What year did Hawaii become a US territory?",
        "choices": ["1959", "1898", "1778", "500"],
        "answer": "1898"
    },
    {
        "question": "What year did Captain Cook discover Hawaii?",
        "choices": ["1959", "1898", "1778", "500"],
        "answer": "1778"
    },
    {
        "question": "What year did the first Polynesians arrive in Hawaii?",
        "choices": ["1959", "1898", "1778", "500"],
        "answer": "500"
    },
    {
        "question": "What year did the first Hawaiians arrive in Hawaii?",
        "choices": ["1400", "300", "800", "500"],
        "answer": "300"
    },
    {
        "question": "Who was the last Hawaiian monarch?",
        "choices": ["King Kamehameha", "Queen Liliuokalani", "King Kalakaua", "King Kamehameha II"],
        "answer": "Queen Liliuokalani"
    },
    {
        "question": "What is the largest island in Hawaii?",
        "choices": ["Oahu", "Maui", "Kauai", "Big Island"],
        "answer": "Big Island"
    },
    {
        "question": "What is the second largest island in Hawaii?",
        "choices": ["Oahu", "Maui", "Kauai", "Big Island"],
        "answer": "Maui"
    },
    {
        "question": "What is the third largest island in Hawaii?",
        "choices": ["Oahu", "Maui", "Kauai", "Big Island"],
        "answer": "Oahu"
    },
    {
        "question": "What is the smallest island in Hawaii?",
        "choices": ["Kahoolawe", "Niihau", "Lanai", "Big Island"],
        "answer": "Kahoolawe"
    },
    {
        "question": "What is the name of the island in Hawaii where the state capital is located?",
        "choices": ["Maui", "Oahu", "Kauai", "Big Island"],
        "answer": "Oahu"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous road to Hana is located?",
        "choices": ["Maui", "Oahu", "Kauai", "Big Island"],
        "answer": "Maui"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous Waikiki beach is located?",
        "choices": ["Maui", "Kauai", "Oahu", "Big Island"],
        "answer": "Oahu"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous lava flows are located?",
        "choices": ["Maui", "Kauai", "Oahu", "Big Island"],
        "answer": "Big Island"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous leper colony is located?",
        "choices": ["Maui", "Kauai", "Oahu", "Molokai"],
        "answer": "Molokai"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous Napali coast is located?",
        "choices": ["Maui", "Kauai", "Oahu", "Big Island"],
        "answer": "Kauai"
    },
    {
        "question": "On what battleship does the Pearl Harbor memorial sit?",
        "choices": ["USS Missouri", "USS Arizona", "USS Oklahoma", "USS California"],
        "answer": "USS Arizona"
    },
    {
        "question": "What is the name of the royal palace in Honolulu?",
        "choices": ["Iolani Palace", "Queen's Palace", "King's Palace", "Prince's Palace"],
        "answer": "Iolani Palace"
    },
    {
        "question": "What is the name of the school located in Honolulu that former President Obama attended?",
        "choices": ["Kamehameha", "Iolani", "Punahou", "Mid-Pacific"],
        "answer": "Punahou"
    },
    {
        "question": "What is the name of the school located in Waimea that Arel attended?",
        "choices": ["Kamehameha", "Iolani", "Punahou", "Hawaii Preparatory Academy"],
        "answer": "Hawaii Preparatory Academy"
    },
    {
        "question": "What is the mascot of the University of Hawaii at Manoa?",
        "choices": ["Rainbow Warriors", "Vulcans", "Rainbows", "Warriors"],
        "answer": "Rainbow Warriors"
    },
    {
        "question": "What is the mascot of the University of Hawaii at Hilo?",
        "choices": ["Vikings", "Warriors", "Vulcans", "Sharks"],
        "answer": "Vulcans"
    },
    {
        "question": "How many islands are in Hawaii?",
        "choices": ["8", "6", "4", "10"],
        "answer": "8"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous pineapple is grown?",
        "choices": ["Maui", "Oahu", "Kauai", "Lanai"],
        "answer": "Oahu"
    },
    {
        "question": "How do you say 'Merry Christmas' in Hawaiian?",
        "choices": ["Hau'oli La Hanau", "Hau'oli Makahiki Hou", "Mele Kalikimaka", "Aloha Au Ia 'Oe"],
        "answer": "Mele Kalikimaka"
    },
    {
        "question": "How do you say 'Happy New Year' in Hawaiian?",
        "choices": ["Hau'oli La Hanau", "Hau'oli Makahiki Hou", "Mele Kalikimaka", "Aloha Au Ia 'Oe"],
        "answer": "Hau'oli Makahiki Hou"
    },
    {
        "question": "How do you say 'Happy Birthday' in Hawaiian?",
        "choices": ["Hau'oli Makahiki Hou", "Mele Kalikimaka", "Hau'oli La Hanau", "Aloha Au Ia 'Oe"],
        "answer": "Hau'oli La Hanau"
    },
    {
        "question": "How do you say 'I love you' in Hawaiian?",
        "choices": ["Hau'oli Makahiki Hou", "Mele Kalikimaka", "Hau'oli La Hanau", "Aloha Au Ia 'Oe"],
        "answer": "Aloha Au Ia 'Oe"
    },
    {
        "question": "How do you say 'perseverance' in Hawaiian?",
        "choices": ["Kuleana", "Ho'omau", "Laulima", "Malama"],
        "answer": "Ho'omau"
    },
    {
        "question": "Who is the famous Hawaiian surfer who popularized surfing in the 1950s?",
        "choices": ["Eddie Aikau", "Duke Kahanamoku", "Laird Hamilton", "Bethany Hamilton"],
        "answer": "Duke Kahanamoku"
    },
    {
        "question": "What is the name of the most famous Hawaiian baseball player? (According to Wikipedia)",
        "choices": ["Shane Victorino", "Kolten Wong", "Kurt Suzuki", "Brandon League"],
        "answer": "Shane Victorino"
    },
    {
        "question": "What is the name of the most famous Hawaiian football player? (According to Wikipedia)",
        "choices": ["Marcus Mariota", "Tua Tagovailoa", "Manti Te'o", "Max Unger"],
        "answer": "Marcus Mariota"
    },
    {
        "question": "What is the name of the president in office that refused to annex Hawaii?",
        "choices": ["Theodore Roosevelt", "William McKinley", "Grover Cleveland", "William Taft"],
        "answer": "Grover Cleveland"
    },
    {
        "question": "What is the name of the president in office that annexed Hawaii?",
        "choices": ["Theodore Roosevelt", "William McKinley", "Grover Cleveland", "William Taft"],
        "answer": "William McKinley"
    },
    {
        "question": "What is the name of the president in office when Hawaii became a state?",
        "choices": ["Dwight Eisenhower", "John F. Kennedy", "Lyndon B. Johnson", "Richard Nixon"],
        "answer": "Dwight Eisenhower"
    },
    {
        "question": "What is the Hawaiian word for responsibility?",
        "choices": ["Kuleana", "Ho'omau", "Laulima", "Malama"],
        "answer": "Kuleana"
    },
    {
        "question": "What is the Hawaiian game that is similar to chess?",
        "choices": ["Ulu Maika", "Hula", "Konane", "Makahiki"],
        "answer": "Konane"
    },
    {
        "question": "Which 2002 Disney animated film was set in Hawaii?",
        "choices": ["Moana", "Lilo & Stitch", "The Lion King", "Mulan"],
        "answer": "Lilo & Stitch"
    },
    {
        "question": "What is the name of the famous Hawaiian dessert made with ice and flavored syrup, and frequently topped with things such as li hing powder, mochi, and adzuki beans?",
        "choices": ["Snow Cone", "Ice Cream", "Shave Ice", "Sorbet"],
        "answer": "Shave Ice"
    },
    {
        "question": "What is the name of the famous Hawaiian dish made with spam and rice?",
        "choices": ["Poke", "Lomi Lomi Salmon", "Kalua Pig", "Spam Musubi"],
        "answer": "Spam Musubi"
    },
    {
        "question": "What is the name of the famous Hawaiian dish made with pork and cooked in an underground oven?",
        "choices": ["Poke", "Lomi Lomi Salmon", "Kalua Pig", "Laulau"],
        "answer": "Kalua Pig"
    },
    {
        "question": "What is the name of the famous Hawaiian dessert made with fried sweet bread and fruit / cream filling?",
        "choices": ["Malasada", "Ice Cream", "Shave Ice", "Sorbet"],
        "answer": "Malasada"
    },
    {
        "question": "What is the name of the traditional Hawaiian feast that is often accompanied by live music, hula dancing, and a pig cooked in the ground?",
        "choices": ["Luau", "Makahiki", "Ho'olaule'a", "Paniolo"],
        "answer": "Luau"
    },
    {
        "question": "What is the name of the famous beach on the Big Island that is known for its black sand and sea turtles?",
        "choices": ["Waikiki", "Lanikai", "Waimea Bay", "Punalu'u"],
        "answer": "Punalu'u"
    },
    {
        "question": "What is the name of the famous beach on the Big Island that is known for its green sand?",
        "choices": ["Waikiki", "Papakolea", "Waimea Bay", "Punalu'u"],
        "answer": "Papakolea"
    },
    {
        "question": "What is the name of the famous waterfall on the Big Island that is known for its 442-foot drop?",
        "choices": ["Akaka Falls", "Rainbow Falls", "Hi'ilawe Falls", "Wai'ale Falls"],
        "answer": "Akaka Falls"
    }

]


# Shuffle the list of questions
shuffle(questions)

# Leaderboard file
LEADERBOARD_FILE = "leaderboard2.txt"

# Home page


@app.route('/')
def home():
    return render_template('index.html')

# Start game route


@app.route('/start_game', methods=['GET', 'POST'])
def start_game():
    if request.method == 'POST':
        name = request.form.get('name')
        session['name'] = name
        session['score'] = 0
        session['current_question_index'] = 0

        # Shuffle the questions and store them in the session
        shuffled_questions = list(questions)
        shuffle(shuffled_questions)
        session['shuffled_questions'] = shuffled_questions

        return redirect(url_for('ask_question'))
    return render_template('start_game.html')


@app.route('/ask_question', methods=['GET', 'POST'])
def ask_question():
    # Retrieve the current question index from the session
    current_question_index = session.get('current_question_index', 0)

    # Check if the user has answered all questions
    if current_question_index >= len(questions) or current_question_index >= 20:
        # Redirect to the game over screen
        return redirect(url_for('game_over'))

    # Get the current question
    question = questions[current_question_index]
    # Shuffle the choices
    shuffled_choices = sample(question['choices'], len(question['choices']))
    # Update the question with shuffled choices
    question['choices'] = shuffled_choices

    if request.method == 'POST':
        # Retrieve the user's answer from the form
        answer = request.form.get('answer')
        # Get the correct answer for the current question
        correct_answer = question['answer']

        # Check if the answer is correct
        if answer == question['answer']:
            # Increment the user's score
            session['score'] = session.get('score', 0) + 1

            # Update the leaderboard
            name = session['name']
            with open("leaderboard2.txt", "r+") as f:
                lines = f.readlines()
                found = False
                for i, line in enumerate(lines):
                    if name in line:
                        lines[i] = f"{name},{session['score']}\n"
                        found = True
                        break
                if not found:
                    lines.append(f"{name},{session['score']}\n")

                # Write updated leaderboard back to the file
                f.seek(0)
                f.truncate()  # Clear the file content
                f.writelines(lines)

            # Increment the question index
            session['current_question_index'] = current_question_index + 1

            # Redirect to the "correct" page
            return redirect(url_for('correct_answer'))

        else:
            # Increment the question index
            session['current_question_index'] = current_question_index + 1

            # Redirect to the "incorrect" page with the correct answer for the current question
            return redirect(url_for('incorrect_answer', correct_answer=correct_answer))

    # Render the template for displaying the question
    return render_template('ask_question.html', question=question, current_question_index=current_question_index + 1, total_questions=min(len(questions), 20))


@app.route('/correct_answer')
def correct_answer():
    # Render the template for correct answer
    return render_template('correct_answer.html')


@app.route('/incorrect_answer/<correct_answer>')
def incorrect_answer(correct_answer):
    # Render the template for incorrect answer
    return render_template('incorrect_answer.html', correct_answer=correct_answer)


# View leaderboard route

@app.route('/view_leaderboard')
def view_leaderboard():
    # Load the leaderboard from the file
    leaderboard = []
    with open("leaderboard2.txt", "r") as f:
        for line in f:
            name, score = line.strip().split(",")
            leaderboard.append((name, int(score)))

    # Get the length of the leaderboard
    leaderboard_length = len(leaderboard)

    # Render the template with the leaderboard data
    return render_template('leaderboard.html', leaderboard=leaderboard, leaderboard_length=leaderboard_length)


# Add score to leaderboard route


@app.route('/game_over')
def game_over():
    # Retrieve the final score from the session
    score = session.get('score', 0)

    # Load the leaderboard from a file
    with open("leaderboard2.txt", "r") as f:
        leaderboard = [line.strip().split(",") for line in f]

    # Create a new list that only contains entries where the score is a number
    numeric_leaderboard = [
        entry for entry in leaderboard if entry[1].isdigit()]

    # Sort the numeric_leaderboard by score in descending order
    numeric_leaderboard.sort(key=lambda x: int(x[1]), reverse=True)

    # Render the game over screen with the final score and leaderboard
    return render_template('game_over.html', score=score, leaderboard=numeric_leaderboard)


if __name__ == '__main__':
    app.run(debug=True)

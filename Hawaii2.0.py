import random
import os
import json
import sys
from tkinter.tix import ComboBox
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QInputDialog
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QInputDialog, QDialog


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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Hawaii Trivia Game Version 2.0")
        self.setGeometry(100, 100, 400, 300)

        # Create menu labels
        self.menu_label = QLabel("MENU", self)
        self.menu_label.setGeometry(150, 50, 100, 30)

        # Create buttons
        self.start_button = QPushButton("Start Game", self)
        self.start_button.setGeometry(100, 100, 200, 30)

        self.leaderboard_button = QPushButton("Leaderboard", self)
        self.leaderboard_button.setGeometry(100, 150, 200, 30)

        self.quit_button = QPushButton("Quit", self)
        self.quit_button.setGeometry(100, 200, 200, 30)

        # Connect button signals to slots
        self.start_button.clicked.connect(self.start_game)
        self.leaderboard_button.clicked.connect(self.view_leaderboard)
        self.quit_button.clicked.connect(self.close)

    def start_game(self):
        start_game()

    def view_leaderboard(self):
        leaderboard_dialog = LeaderboardDialog()
        leaderboard_dialog.exec()


class LeaderboardDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Leaderboard")
        self.setGeometry(100, 100, 400, 300)

        # Create leaderboard label
        self.leaderboard_label = QLabel("LEADERBOARD", self)
        self.leaderboard_label.setGeometry(130, 50, 150, 30)

        # Create buttons
        self.view_button = QPushButton("View Leaderboard", self)
        self.view_button.setGeometry(100, 100, 200, 30)

        self.delete_button = QPushButton("Delete Entry", self)
        self.delete_button.setGeometry(100, 150, 200, 30)

        self.clear_button = QPushButton("Clear Leaderboard", self)
        self.clear_button.setGeometry(100, 200, 200, 30)

        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(100, 250, 200, 30)

        # Connect button signals to slots
        self.view_button.clicked.connect(self.view_leaderboard)
        self.delete_button.clicked.connect(self.delete_entry)
        self.clear_button.clicked.connect(self.clear_leaderboard)
        self.back_button.clicked.connect(self.close)

    def view_leaderboard(self):
        # Load the leaderboard from a file
        with open("leaderboard2.txt", "r") as f:
            leaderboard = [line.strip().split(",") for line in f]

        # Display the leaderboard
        leaderboard_text = ""
        for entry in leaderboard:
            leaderboard_text += f"Name: {entry[0]}, Score: {entry[1]}\n"

        QMessageBox.information(self, "Leaderboard", leaderboard_text)

    def delete_entry(self):
        # Get the name of the entry to delete
        name, ok = QInputDialog.getText(
            self, "Delete Entry", "Enter the name of the entry to delete:")

        if ok:
            # Load the leaderboard from a file
            with open("leaderboard2.txt", "r") as f:
                leaderboard = [line.strip().split(",") for line in f]

            # Find and remove the entry
            updated_leaderboard = [
                entry for entry in leaderboard if entry[0] != name]

            # Save the updated leaderboard to the file
            with open("leaderboard2.txt", "w") as f:
                for entry in updated_leaderboard:
                    f.write(f"{entry[0]},{entry[1]}\n")

            QMessageBox.information(
                self, "Delete Entry", "Entry deleted successfully.")

    def clear_leaderboard(self):
        # Confirm the action
        reply = QMessageBox.question(self, "Clear Leaderboard", "Are you sure you want to clear the leaderboard?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            # Clear the leaderboard file
            with open("leaderboard2.txt", "w") as f:
                f.write("")

            QMessageBox.information(
                self, "Clear Leaderboard", "Leaderboard cleared successfully.")
        leaderboard_text = ""
        for entry in leaderboard:
            leaderboard_text += f"{entry[0]} - {entry[1]}\n"

        QMessageBox.information(None, "Leaderboard", leaderboard_text)

    def delete_entry(self):
        # Ask the user for the name to delete
        name, ok = QInputDialog.getText(
            None, "Delete Entry", "Enter the name to delete:")
        if ok:
            name = name.strip()
        else:
            return

        # Load the leaderboard from a file
        with open("leaderboard2.txt", "r") as f:
            leaderboard = [line.strip().split(",") for line in f]

        # Remove the entry with the specified name
        leaderboard = [entry for entry in leaderboard if entry[0] != name]

        # Save the updated leaderboard to the file
        with open("leaderboard2.txt", "w") as f:
            for entry in leaderboard:
                f.write(f"{entry[0]},{entry[1]}\n")

        QMessageBox.information(None, "Delete Entry",
                                "Entry deleted successfully.")

    def clear_leaderboard(self):
        # Confirm with the user before clearing the leaderboard
        reply = QMessageBox.question(
            None, "Clear Leaderboard", "Are you sure you want to clear the leaderboard?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Clear the leaderboard file
            with open("leaderboard2.txt", "w") as f:
                f.write("Name,Score\n")

            QMessageBox.information(
                None, "Clear Leaderboard", "Leaderboard cleared successfully.")


def start_game():
    # Check if leaderboard file exists, if not create one
    if not os.path.exists("leaderboard2.txt"):
        with open("leaderboard2.txt", "w") as f:
            f.write("Name,Score\n")

    # Load the leaderboard from a file
    with open("leaderboard2.txt", "r") as f:
        leaderboard = [line.strip().split(",") for line in f]

    # Welcome message
    QMessageBox.information(None, "Hawaii Trivia Game",
                            "Welcome to the Hawaii Trivia Game! You will be asked twenty questions about Hawaii. Let's see how many you can get right!")

    # Ask the user for their name
    name, ok = QInputDialog.getText(
        None, "Hawaii Trivia Game", "What is your name?")
    if ok:
        name = name.strip()
    else:
        return

    # Shuffle the list of questions
    random.shuffle(questions)

    # Initialize the score
    score = 0

    # Loop through the questions and ask the user each question
    for i, question in enumerate(questions[:20]):
        choices = question["choices"]
        random.shuffle(choices)  # Shuffle the choices
        answer, ok = QInputDialog.getItem(
            None, "Hawaii Trivia Game", f"Question {i+1}/20: {question['question']}", ["Select Answer Below"] + choices + ["Quit"], editable=False)
        if ok:
            answer = answer.strip()
        else:
            return

        if answer.lower() == "quit":
            QMessageBox.information(
                None, "Hawaii Trivia Game", "Game ended. Your final score is: " + str(score))
            break

        if answer.lower() == question["answer"].lower():
            QMessageBox.information(None, "Hawaii Trivia Game", "Correct!")
            score += 1
        else:
            QMessageBox.information(
                None, "Hawaii Trivia Game", "Incorrect. The correct answer is " + question['answer'] + ".")

    # Add the user's name and score to the leaderboard
    if name.lower() == "clear":
        with open("leaderboard2.txt", "w") as f:
            f.write("Name,Score\n")
    else:
        # Check if the user's name is already in the leaderboard
        name_exists = False
        for i, entry in enumerate(leaderboard):
            if entry[0] == name:
                leaderboard[i][1] = str(score)
                name_exists = True
                break

        # If the user's name is not in the leaderboard, add it
        if not name_exists:
            leaderboard.append([name, str(score)])

        # Create a new list that only contains entries where the score is a number
        numeric_leaderboard = [
            entry for entry in leaderboard if entry[1].isdigit()]

        # Sort the numeric_leaderboard by score in descending order
        numeric_leaderboard.sort(key=lambda x: int(x[1]), reverse=True)

        # Display the leaderboard to the user
        leaderboard_text = "LEADERBOARD\n-----------\n"
        for i, (name, score) in enumerate(numeric_leaderboard):
            leaderboard_text += "{0}. {1}: {2}\n".format(
                i+1, name, score)

        QMessageBox.information(
            None, "Hawaii Trivia Game", leaderboard_text)

        # Save the updated leaderboard to a file
        with open("leaderboard2.txt", "w") as f:
            for name, score in numeric_leaderboard:
                f.write("{},{}\n".format(name, score))


def view_leaderboard():
    # Load the leaderboard from a file
    with open("leaderboard2.txt", "r") as f:
        leaderboard = [line.strip().split(",") for line in f]

    # Create a new list that only contains entries where the score is a number
    numeric_leaderboard = [
        entry for entry in leaderboard if entry[1].isdigit()]

    # Sort the numeric_leaderboard by score in descending order
    numeric_leaderboard.sort(key=lambda x: int(x[1]), reverse=True)

    # Display the leaderboard to the user
    leaderboard_text = "LEADERBOARD\n-----------\n"
    for i, (name, score) in enumerate(numeric_leaderboard):
        leaderboard_text += "{0}. {1}: {2}\n".format(i+1, name, score)

    QMessageBox.information(None, "Leaderboard", leaderboard_text)


def delete_entry():
    # Load the leaderboard from a file
    with open("leaderboard2.txt", "r") as f:
        leaderboard = [line.strip().split(",") for line in f]

    # Ask the user for the name of the entry to delete
    name, ok = QInputDialog.getText(
        None, "Delete Entry", "Enter the name of the entry to delete:")
    if ok:
        name = name.strip()
    else:
        return

    # Remove the entry from the leaderboard
    for i, entry in enumerate(leaderboard):
        if entry[0] == name:
            del leaderboard[i]
            break

    # Save the updated leaderboard to a file
    with open("leaderboard2.txt", "w") as f:
        for name, score in leaderboard:
            f.write("{},{}\n".format(name, score))

    QMessageBox.information(None, "Delete Entry", "Entry deleted.")


def clear_leaderboard():
    # Clear the leaderboard file
    with open("leaderboard2.txt", "w") as f:
        f.write("Name,Score\n")

    QMessageBox.information(None, "Clear Leaderboard", "Leaderboard cleared.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            # Set window title and size
            self.setWindowTitle("Hawaii Trivia Game")
            self.setGeometry(100, 100, 400, 300)

            # Create menu labels
            self.menu_label = QLabel("MENU", self)
            self.menu_label.setGeometry(150, 50, 100, 30)

            # Create buttons
            self.start_button = QPushButton("Start Game", self)
            self.start_button.setGeometry(100, 100, 200, 30)

            self.leaderboard_button = QPushButton("Leaderboard", self)
            self.leaderboard_button.setGeometry(100, 150, 200, 30)

            self.quit_button = QPushButton("Quit", self)
            self.quit_button.setGeometry(100, 200, 200, 30)

            # Connect button signals to slots
            self.start_button.clicked.connect(self.start_game)
            self.leaderboard_button.clicked.connect(self.view_leaderboard)
            self.quit_button.clicked.connect(self.close)

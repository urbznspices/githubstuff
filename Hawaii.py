import random
import os
import json
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QInputDialog
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QInputDialog, QDialog

# Define the list of questions and answers about Hawaii
questions = [
    {
        "question": "What is the capital of Hawaii?",
        "choices": ["A. Honolulu", "B. Hilo", "C. Kona", "Lahaina"],
        "answer": "A. Honolulu"
    },

    {
        "question": "What is the name of the active volcano on the Big Island of Hawaii?",
        "choices": ["A. Mauna Kea", "B. Mauna Loa", "C. Kilauea", "D. Haleakala"],
        "answer": "C. Kilauea"
    },
    {
        "question": "What is the name of the famous beach on the North Shore of Oahu?",
        "choices": ["A. Waikiki", "B. Lanikai", "C. Waimea Bay", "D. Hanauma Bay"],
        "answer": "C. Waimea Bay"
    },
    {
        "question": "What is the name of the Hawaiian dish made with raw fish?",
        "choices": ["A. Poke", "B. Lomi Lomi Salmon", "C. Kalua Pig", "D. Laulau"],
        "answer": "A. Poke"
    },
    {
        "question": "What is the name of the Hawaiian goddess of fire and volcanoes?",
        "choices": ["A. Pele", "B. Hi'iaka", "C. Laka", "D. Kapo"],
        "answer": "A. Pele"
    },
    {
        "question": "What is the name of the Hawaiian king who united the islands?",
        "choices": ["A. Kalakaua", "B. Kamehameha", "C. Lunalilo", "D. Kamehameha II"],
        "answer": "B. Kamehameha"
    },
    {
        "question": "What is the name of the Hawaiian flower necklace?",
        "choices": ["A. Haku", "B. Lei", "C. Kukui", "D. Maile"],
        "answer": "B. Lei"
    },
    {
        "question": "What is the name of the Hawaiian instrument made from a gourd?",
        "choices": ["A. Steel Guitar", "B. Ukulele", "C. Slack Key Guitar", "D. Ipu Heke"],
        "answer": "B. Ukulele"
    },
    {
        "question": "What is the name of the Hawaiian word for hello?",
        "choices": ["A. Mahalo", "B. Aloha", "C. Ohana", "D. Ono"],
        "answer": "B. Aloha"
    },
    {
        "question": "What is the name of the Hawaiian word for goodbye?",
        "choices": ["A. Mahalo", "B. Ohana", "C. Aloha", "D. Ono"],
        "answer": "C. Aloha"
    },
    {
        "question": "What is the name of the Hawaiian word for thank you?",
        "choices": ["A. Aloha", "B. Ohana", "C. Ono", "D. Mahalo"],
        "answer": "D. Mahalo"
    },
    {
        "question": "What is the name of the Hawaiian word for family?",
        "choices": ["A. Mahalo", "B. Ohana", "C. Aloha", "D. Ono"],
        "answer": "B. Ohana"
    },
    {
        "question": "What is the name of the Hawaiian word for delicious?",
        "choices": ["A. Mahalo", "B. Ohana", "C. Aloha", "D. Ono"],
        "answer": "D. Ono"
    },
    {
        "question": "What is the name of the Hawaiian word for love?",
        "choices": ["A. Mahalo", "B. Ohana", "C. Aloha", "D. Ono"],
        "answer": "C. Aloha"
    },
    {
        "question": "What is the name of the Hawaiian word for ocean?",
        "choices": ["A. Kai", "B. Wai", "C. Anuenue", "D. Honu"],
        "answer": "A. Kai"
    },
    {
        "question": "What is the name of the Hawaiian word for mountain?",
        "choices": ["A. Kai", "B. Wai", "C. Anuenue", "D. Mauna"],
        "answer": "D. Mauna"
    },
    {
        "question": "What is the name of the Hawaiian word for water?",
        "choices": ["A. Kai", "B. Wai", "C. Anuenue", "D. Honu"],
        "answer": "B. Wai"
    },
    {
        "question": "What is the name of the Hawaiian word for rainbow?",
        "choices": ["A. Kai", "B. Wai", "C. Anuenue", "D. Honu"],
        "answer": "C. Anuenue"
    },
    {
        "question": "What is the name of the Hawaiian word for turtle?",
        "choices": ["A. Kai", "B. Wai", "C. Anuenue", "D. Honu"],
        "answer": "D. Honu"
    },
    {
        "question": "What is the name of the Hawaiian word for shark?",
        "choices": ["A. Pua", "B. I'a", "C. Mano", "D. Hoku"],
        "answer": "C. Mano"
    },
    {
        "question": "What is the name of the Hawaiian word for fish?",
        "choices": ["A. Pua", "B. Hoku", "C. Mano", "D. I'a"],
        "answer": "D. I'a"
    },
    {
        "question": "What is the name of the Hawaiian word for flower?",
        "choices": ["A. I'a", "B. Hoku", "C. Mano", "D. Pua"],
        "answer": "D. Pua"
    },
    {
        "question": "What is the name of the Hawaiian word for star?",
        "choices": ["A. I'a", "B. Pua", "C. Mano", "D. Hoku"],
        "answer": "D. Hoku"
    },
    {
        "question": "What is the name of the Hawaiian word for sun?",
        "choices": ["A. I'a", "B. Hoku", "C. La", "D. Hoku"],
        "answer": "C. La"
    },
    {
        "question": "What is the name of the Hawaiian word for moon?",
        "choices": ["A. Aloha", "B. Makani", "C. La", "D. Mahina"],
        "answer": "D. Mahina"
    },
    {
        "question": "What is the name of the Hawaiian word for wind?",
        "choices": ["A. Mauka", "B. Mahina", "C. Makani", "D. Makai"],
        "answer": "D. Makani"
    },
    {
        "question": "What is the name of the Hawaiian word for rain?",
        "choices": ["A. Mauka", "B. Waiwai", "C. Makani", "D. Ua"],
        "answer": "D. Ua"
    },
    {
        "question": "What is the largest town on the Big Island?",
        "choices": ["A. Kona", "B. Hilo", "C. Waimea", "D. Pahoa"],
        "answer": "B. Hilo"
    },
    {
        "question": "What is the name of the town on the Big Island where the Kona coffee is grown?",
        "choices": ["A. Hilo", "B. Waimea", "C. Kona", "D. Pahoa"],
        "answer": "C. Kona"
    },
    {
        "question": "What is the name of the town in between Kona and Hilo on the Big Island? (Arel lives here)",
        "choices": ["A. Waimea", "B. Pahoa", "C. Honokaa", "D. Kealakekua"],
        "answer": "A. Waimea"
    },
    {
        "question": "What is the name of the tallest mountain in the world? (It's in Hawaii)",
        "choices": ["A. Mount Everest", "B. Mauna Loa", "C. Mauna Kea", "D. Kilauea"],
        "answer": "C. Mauna Kea"
    },
    {
        "question": "How many freeways are there on the Big Island?",
        "choices": ["A. One", "B. Two", "C. Three", "D. Zero"],
        "answer": "D. Zero"
    },
    {
        "question": "What year did Hawaii become a state?",
        "choices": ["A. 1959", "B. 1898", "C. 1778", "D. 500"],
        "answer": "A. 1959"
    },
    {
        "question": "What year did Hawaii become a US territory?",
        "choices": ["A. 1959", "B. 1898", "C. 1778", "D. 500"],
        "answer": "B. 1898"
    },
    {
        "question": "What year did Captain Cook discover Hawaii?",
        "choices": ["A. 1959", "B. 1898", "C. 1778", "D. 500"],
        "answer": "C. 1778"
    },
    {
        "question": "What year did the first Polynesians arrive in Hawaii?",
        "choices": ["A. 1959", "B. 1898", "C. 1778", "D. 500"],
        "answer": "D. 500"
    },
    {
        "question": "What year did the first Hawaiians arrive in Hawaii?",
        "choices": ["A. 1400", "B. 300", "C. 800", "D. 500"],
        "answer": "B. 300"
    },
    {
        "question": "Who was the last Hawaiian monarch?",
        "choices": ["A. King Kamehameha", "B. Queen Liliuokalani", "C. King Kalakaua", "D. King Kamehameha II"],
        "answer": "B. Queen Liliuokalani"
    },
    {
        "question": "What is the largest island in Hawaii?",
        "choices": ["A. Oahu", "B. Maui", "C. Kauai", "D. Big Island"],
        "answer": "D. Big Island"
    },
    {
        "question": "What is the second largest island in Hawaii?",
        "choices": ["A. Oahu", "B. Maui", "C. Kauai", "D. Big Island"],
        "answer": "B. Maui"
    },
    {
        "question": "What is the third largest island in Hawaii?",
        "choices": ["A. Oahu", "B. Maui", "C. Kauai", "D. Big Island"],
        "answer": "A. Oahu"
    },
    {
        "question": "What is the smallest island in Hawaii?",
        "choices": ["A. Kahoolawe", "B. Niihau", "C. Lanai", "D. Big Island"],
        "answer": "A. Kahoolawe"
    },
    {
        "question": "What is the name of the island in Hawaii where the state capital is located?",
        "choices": ["A. Maui", "B. Oahu", "C. Kauai", "D. Big Island"],
        "answer": "B. Oahu"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous road to Hana is located?",
        "choices": ["A. Maui", "B. Oahu", "C. Kauai", "D. Big Island"],
        "answer": "A. Maui"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous Waikiki beach is located?",
        "choices": ["A. Maui", "B. Kauai", "C. Oahu", "D. Big Island"],
        "answer": "C. Oahu"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous lava flows are located?",
        "choices": ["A. Maui", "B. Kauai", "C. Oahu", "D. Big Island"],
        "answer": "D. Big Island"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous leper colony is located?",
        "choices": ["A. Maui", "B. Kauai", "C. Oahu", "D. Molokai"],
        "answer": "D. Molokai"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous Napali coast is located?",
        "choices": ["A. Maui", "B. Kauai", "C. Oahu", "D. Big Island"],
        "answer": "B. Kauai"
    },
    {
        "question": "On what battleship does the Pearl Harbor memorial sit?",
        "choices": ["A. USS Missouri", "B. USS Arizona", "C. USS Oklahoma", "D. USS California"],
        "answer": "B. USS Arizona"
    },
    {
        "question": "What is the name of the royal palace in Honolulu?",
        "choices": ["A. Iolani Palace", "B. Queen's Palace", "C. King's Palace", "D. Prince's Palace"],
        "answer": "A. Iolani Palace"
    },
    {
        "question": "What is the name of the school located in Honolulu that former President Obama attended?",
        "choices": ["A. Kamehameha", "B. Iolani", "C. Punahou", "D. Mid-Pacific"],
        "answer": "C. Punahou"
    },
    {
        "question": "What is the name of the school located in Waimea that Arel attended?",
        "choices": ["A. Kamehameha", "B. Iolani", "C. Punahou", "D. Hawaii Preparatory Academy"],
        "answer": "D. Hawaii Preparatory Academy"
    },
    {
        "question": "What is the mascot of the University of Hawaii at Manoa?",
        "choices": ["A. Rainbow Warriors", "B. Vulcans", "C. Rainbows", "D. Warriors"],
        "answer": "A. Rainbow Warriors"
    },
    {
        "question": "What is the mascot of the University of Hawaii at Hilo?",
        "choices": ["A. Vikings", "B. Warriors", "C. Vulcans", "D. Sharks"],
        "answer": "C. Vulcans"
    },
    {
        "question": "How many islands are in Hawaii?",
        "choices": ["A. 8", "B. 6", "C. 4", "D. 10"],
        "answer": "A. 8"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous pineapple is grown?",
        "choices": ["A. Maui", "B. Oahu", "C. Kauai", "D. Lanai"],
        "answer": "B. Oahu"
    },
    {
        "question": "How do you say 'Merry Christmas' in Hawaiian?",
        "choices": ["A. Hau'oli La Hanau", "B. Hau'oli Makahiki Hou", "C. Mele Kalikimaka", "D. Aloha Au Ia 'Oe"],
        "answer": "C. Mele Kalikimaka"
    },
    {
        "question": "How do you say 'Happy New Year' in Hawaiian?",
        "choices": ["A. Hau'oli La Hanau", "B. Hau'oli Makahiki Hou", "C. Mele Kalikimaka", "D. Aloha Au Ia 'Oe"],
        "answer": "B. Hau'oli Makahiki Hou"
    },
    {
        "question": "How do you say 'Happy Birthday' in Hawaiian?",
        "choices": ["A. Hau'oli Makahiki Hou", "B. Mele Kalikimaka", "C. Hau'oli La Hanau", "D. Aloha Au Ia 'Oe"],
        "answer": "C. Hau'oli La Hanau"
    },
    {
        "question": "How do you say 'I love you' in Hawaiian?",
        "choices": ["A. Hau'oli Makahiki Hou", "B. Mele Kalikimaka", "C. Hau'oli La Hanau", "D. Aloha Au Ia 'Oe"],
        "answer": "D. Aloha Au Ia 'Oe"
    },
    {
        "question": "How do you say 'perseverance' in Hawaiian?",
        "choices": ["A. Kuleana", "B. Ho'omau", "C. Laulima", "D. Malama"],
        "answer": "B. Ho'omau"
    },
    {
        "question": "Who is the famous Hawaiian surfer who popularized surfing in the 1950s?",
        "choices": ["A. Eddie Aikau", "B. Duke Kahanamoku", "C. Laird Hamilton", "D. Bethany Hamilton"],
        "answer": "B. Duke Kahanamoku"
    },
    {
        "question": "What is the name of the most famous Hawaiian baseball player? (According to Wikipedia)",
        "choices": ["A. Shane Victorino", "B. Kolten Wong", "C. Kurt Suzuki", "D. Brandon League"],
        "answer": "A. Shane Victorino"
    },
    {
        "question": "What is the name of the most famous Hawaiian football player? (According to Wikipedia)",
        "choices": ["A. Marcus Mariota", "B. Tua Tagovailoa", "C. Manti Te'o", "D. Max Unger"],
        "answer": "A. Marcus Mariota"
    },
    {
        "question": "What is the name of the president in office that refused to annex Hawaii?",
        "choices": ["A. Theodore Roosevelt", "B. William McKinley", "C. Grover Cleveland", "D. William Taft"],
        "answer": "C. Grover Cleveland"
    },
    {
        "question": "What is the name of the president in office that annexed Hawaii?",
        "choices": ["A. Theodore Roosevelt", "B. William McKinley", "C. Grover Cleveland", "D. William Taft"],
        "answer": "B. William McKinley"
    },
    {
        "question": "What is the name of the president in office when Hawaii became a state?",
        "choices": ["A. Dwight Eisenhower", "B. John F. Kennedy", "C. Lyndon B. Johnson", "D. Richard Nixon"],
        "answer": "A. Dwight Eisenhower"
    }
]


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
        with open("leaderboard.txt", "r") as f:
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
            with open("leaderboard.txt", "r") as f:
                leaderboard = [line.strip().split(",") for line in f]

            # Find and remove the entry
            updated_leaderboard = [
                entry for entry in leaderboard if entry[0] != name]

            # Save the updated leaderboard to the file
            with open("leaderboard.txt", "w") as f:
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
            with open("leaderboard.txt", "w") as f:
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
        with open("leaderboard.txt", "r") as f:
            leaderboard = [line.strip().split(",") for line in f]

        # Remove the entry with the specified name
        leaderboard = [entry for entry in leaderboard if entry[0] != name]

        # Save the updated leaderboard to the file
        with open("leaderboard.txt", "w") as f:
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
            with open("leaderboard.txt", "w") as f:
                f.write("Name,Score\n")

            QMessageBox.information(
                None, "Clear Leaderboard", "Leaderboard cleared successfully.")


def start_game():
    # Check if leaderboard file exists, if not create one
    if not os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "w") as f:
            f.write("Name,Score\n")

    # Load the leaderboard from a file
    with open("leaderboard.txt", "r") as f:
        leaderboard = [line.strip().split(",") for line in f]

    # Welcome message
    QMessageBox.information(None, "Hawaii Trivia Game",
                            "Welcome to the Hawaii Trivia Game!")

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
    for question in questions:
        answer, ok = QInputDialog.getItem(
            None, "Hawaii Trivia Game", question["question"], question["choices"] + ["Quit"], editable=False)
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
        with open("leaderboard.txt", "w") as f:
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
        with open("leaderboard.txt", "w") as f:
            for name, score in numeric_leaderboard:
                f.write("{},{}\n".format(name, score))


def view_leaderboard():
    # Load the leaderboard from a file
    with open("leaderboard.txt", "r") as f:
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
    with open("leaderboard.txt", "r") as f:
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
    with open("leaderboard.txt", "w") as f:
        for name, score in leaderboard:
            f.write("{},{}\n".format(name, score))

    QMessageBox.information(None, "Delete Entry", "Entry deleted.")


def clear_leaderboard():
    # Clear the leaderboard file
    with open("leaderboard.txt", "w") as f:
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

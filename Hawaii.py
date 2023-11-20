import random
import os
import json
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QInputDialog

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
    },
    {
        "question": "On what battleship does the Pearl Harbor memorial sit?",
        "answer": "USS Arizona"
    },
    {
        "question": "What is the name of the royal palace in Honolulu?",
        "answer": "Iolani Palace"
    },
    {
        "question": "What is the name of the school located in Honolulu that President Obama attended?",
        "answer": "Punahou"
    },
    {
        "question": "What is the name of the school located in Waimea that Arel attended?",
        "answer": "Hawaii Preparatory Academy"
    },
    {
        "question": "What is the mascot of the University of Hawaii at Manoa?",
        "answer": "Rainbow Warriors"
    },
    {
        "question": "What is the mascot of the University of Hawaii at Hilo?",
        "answer": "Vulcans"
    },
    {
        "question": "How many islands are in Hawaii?",
        "answer": "8"
    },
    {
        "question": "What is the name of the island in Hawaii where the famous pineapple is grown?",
        "answer": "Oahu"
    },
    {
        "question": "How do you say 'Merry Christmas' in Hawaiian?",
        "answer": "Mele Kalikimaka"
    },
    {
        "question": "How do you say 'Happy New Year' in Hawaiian?",
        "answer": "Hau'oli Makahiki Hou"
    },
    {
        "question": "How do you say 'Happy Birthday' in Hawaiian?",
        "answer": "Hau'oli La Hanau"
    },
    {
        "question": "How do you say 'I love you' in Hawaiian?",
        "answer": "Aloha Au Ia 'Oe"
    },
    {
        "question": "How do you say 'perseverance' in Hawaiian?",
        "answer": "Ho'omau"
    },
    {
        "question": "Who is the famous Hawaiian surfer who popularized surfing in the 1950s?",
        "answer": "Duke Kahanamoku"
    },
    {
        "question": "What is the name of the most famous Hawaiian baseball player?",
        "answer": "Shane Victorino"
    },
    {
        "question": "What is the name of the most famous Hawaiian football player?",
        "answer": "Marcus Mariota"
    },
    {
        "question": "What is the name of the president in office that refused to annex Hawaii?",
        "answer": "Grover Cleveland"
    },
    {
        "question": "What is the name of the president in office that annexed Hawaii?",
        "answer": "William McKinley"
    },
    {
        "question": "What is the name of the president in office when Hawaii became a state?",
        "answer": "Dwight Eisenhower", "answer": "Dwight D. Eisenhower"
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
        leaderboard_window = LeaderboardWindow()
        leaderboard_window.show()


class LeaderboardWindow(QMainWindow):
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
        answer, ok = QInputDialog.getText(
            None, "Hawaii Trivia Game", question["question"])
        if ok:
            answer = answer.strip()
        else:
            return

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
            leaderboard_text += "{0}. {1}: {2}\n".format(i+1, name, score)

        QMessageBox.information(None, "Hawaii Trivia Game", leaderboard_text)

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

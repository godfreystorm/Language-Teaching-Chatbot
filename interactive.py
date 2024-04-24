from numbers_teaching import french_numbers_chat
from greetings_teaching import greetings_lesson_teaching
from nouns_teaching import nouns_lesson_teaching
from subject_pronouns_teaching import pronouns_lesson_teaching
from phrases_teaching import common_phrases_lesson_teaching


def lesson_introduction():
    print("Welcome to the Interactive French Lessons!")
    print("Select what you would like to learn.")

def display_lesson_options():
    print("\nLesson Options:")
    print("1. Greetings")
    print("2. Numbers")
    print("3. Nouns")
    print("4. Subject pronouns")
    print("5. Common Phrases")
    print("6. Return to Main Menu")

def greetings_lesson():
    greetings_lesson_teaching()

def numbers_lesson():
    french_numbers_chat()

def nouns_lesson():
    nouns_lesson_teaching()

def verb_conjugates_lesson():
    pronouns_lesson_teaching()

def common_phrases_lesson():
    common_phrases_lesson_teaching()

def interactive_lessons_selected():
    lesson_introduction()
    while True:
        display_lesson_options()
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            greetings_lesson()
        elif choice == '2':
            numbers_lesson()
        elif choice == '3':
            nouns_lesson()
        elif choice == '4':
            verb_conjugates_lesson()
        elif choice == '5':
            common_phrases_lesson()
        elif choice == '6':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    interactive_lessons_selected()

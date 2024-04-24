import sys
from translate import french_tutor_chat
from interactive import interactive_lessons_selected
from big_quiz import run_french_quiz
from feedback import save_feedback

def introduction():
    print("\nWelcome to the French Learning Chatbot!")
    print("\nI'm here to help you learn French. Please choose from the following learning options:")

def display_menu():
    print("\nLearning Options:")
    print("1. Direct Translations")
    print("2. Interactive Lessons")
    print("3. Quizzes and Progress Level Assement")
    print("4. Feedback for Creators")
    print("5. Quit")

def direct_translations():
    print('')
    french_tutor_chat()

def interactive_lessons():
    print("")
    interactive_lessons_selected()

def quizzes():
    print("")
    run_french_quiz()

def feedback():
    print("")
    save_feedback()

def goodbye_message():
    print("\nBot: Au revoir! Feel free to come back anytime to continue learning.")

def main():
    introduction()
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            direct_translations()
        elif choice == '2':
            interactive_lessons()
        elif choice == '3':
            quizzes()
        elif choice == '4':
            feedback()
        elif choice == '5':
            goodbye_message()
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

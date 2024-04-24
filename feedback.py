def save_feedback():
    """Prompt user for feedback and save it to a file."""
    try:
        # Prompting the user to enter their feedback
        user_feedback = input("Please enter your feedback and press enter: ")

        path_to_save = "../feedback.txt"
        # Opening the feedback.txt file in append mode to add new feedback entries
        with open(path_to_save, "a") as file:
            file.write(user_feedback + "\n")  # Adding a newline for each new entry
        
        print("Thank you for your feedback!")  # Confirming that the feedback has been recorded

    except Exception as e:
        print(f"An error occurred: {e}")  # Handling potential errors gracefully

if __name__ == "__main__":
    save_feedback()

from openai import OpenAI
import os
import platform
import random
from data import nouns_to_learn  # Adjust according to your data structure

api_key = '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'
client = OpenAI(api_key=api_key)

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def transition_phrase():
    """Generates a dynamic transition phrase."""
    transitions = [
        "Okay, now let's talk about",
        "Moving on to",
        "Next up, we have",
        "Let's move on to",
        "Now, let's explore"
    ]
    return random.choice(transitions)

def get_instructional_content(noun):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user", 
                "content": f"Explain the French noun '{noun}' and provide a memorable way to remember and understand it."
            }],
            temperature=0.7,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        content = response.choices[0].message.content.strip()
        return f"Bot: {content}"
    except Exception as e:
        return f"Error generating content: {e}"

def get_quiz_question(english_description):
    # Adjusted to ask for the French equivalent of the English description
    return f"\nBot: What is the French noun for '{english_description}'?"

def evaluate_response(user_response, correct_answer):
    if user_response.lower().strip() == correct_answer.lower():
        return "Bot: Correct!", True
    else:
        return f"Bot: That's not quite right. The correct answer is '{correct_answer}'.", False

def nouns_lesson_teaching():
    print("\nBot: Hi! Welcome to the French nouns learning section.\n")

    nouns_list = list(nouns_to_learn.items())
    batch_size = 5
    batch_index = 0  # Initialize batch index

    while batch_index * batch_size < len(nouns_list):  # Ensure loop runs as long as there are batches
        start_index = batch_index * batch_size
        batch = nouns_list[start_index:start_index + batch_size]

        for j, (french_noun, english_description) in enumerate(batch):
            intro_line = "Let's begin with" if j == 0 else transition_phrase()
            print(f"\n{intro_line} '{french_noun}'.\n")
            print(get_instructional_content(french_noun))
            input("\nPress Enter once you're ready to move on...\n")

        print("\nBot: Alright! It's quiz time 🌟 You'll need to translate the following English nouns into French. Hit Enter when you're ready.")
        input()
        clear_screen()

        correct_answers = 0
        for _, (french_noun, english_description) in enumerate(batch):
            question = get_quiz_question(english_description)
            print(question)
            user_response = input("Your answer: ").strip()
            feedback, correct = evaluate_response(user_response, french_noun)
            print(feedback)
            if correct:
                correct_answers += 1

        if correct_answers >= 3:
            print(f"\nBot: Woohoo! You nailed it with {correct_answers} out of {len(batch)} correct! 🚀")
        else:
            print(f"\nBot: Oh no, you got {correct_answers} out of {len(batch)}. Not quite there, but don't worry! 💪")

        user_choice = input("\nWould you like to [c]ontinue with the next batch, [r]epeat this one, or take a [b]reak and return to the menu? (c/r/b): ").lower().strip()

        if user_choice == 'b':
            print("\nBot: Taking a break? No worries, come back anytime you're ready to continue!")
            break
        elif user_choice == 'r':
            print("\nBot: Let's tackle this batch again for better mastery!")
            continue  # Forces a repeat of the current batch
        elif user_choice == 'c' and correct_answers < 3:
            print("\nBot: Remember, you need at least 3 out of 5 correct to move to the next batch. Let's try this batch again.")
            continue  # Forces a repeat of the current batch
        elif user_choice == 'c' and correct_answers >= 3:
            batch_index += 1  # Only increment to the next batch if passed


    print("\nBot: You did it! 🎉 Congratulations on mastering the nouns section. Let's head back to the Main Menu...")

if __name__ == "__main__":
    nouns_lesson_teaching()

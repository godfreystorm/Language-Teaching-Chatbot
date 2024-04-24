from openai import OpenAI
import os
import platform
from data import pronouns_to_learn  # Ensure this matches your data structure

api_key = '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'
client = OpenAI(api_key=api_key)

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def get_instructional_content(pronoun):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user", 
                "content": f"Explain the French pronoun '{pronoun}' and provide a memorable way to remember it."
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
    return f"\nBot: What is the French pronoun for '{english_description}'?"

def evaluate_response(user_response, correct_answer):
    if user_response.lower().strip() == correct_answer.lower():
        return "Bot: Correct!", True
    else:
        return f"Bot: That's not quite right. The correct answer is '{correct_answer}'.", False

def pronouns_lesson_teaching():
    print("\nBot: Hi! Welcome to the French pronouns learning section.\n")

    pronouns_list = list(pronouns_to_learn.items())
    # Adjust the batches for 9 pronouns divided into two groups
    batch_sizes = [5, 4]  # First batch of 5, second batch of 4
    for batch_size in batch_sizes:
        batch = pronouns_list[:batch_size]
        pronouns_list = pronouns_list[batch_size:]

        for french_pronoun, english_description in batch:
            print("\n" + get_instructional_content(french_pronoun))
            input("Press Enter once you're ready to move on...\n")

        print("\nBot: Alright! It's quiz time 🌟 Try to translate the English pronouns into French. Hit Enter when you're ready.")
        input()
        clear_screen()

        correct_answers = 0
        for french_pronoun, english_description in batch:
            question = get_quiz_question(english_description)
            print(question)
            user_response = input("Your answer: ").strip()
            feedback, correct = evaluate_response(user_response, french_pronoun)
            print(feedback)
            if correct:
                correct_answers += 1

        success_rate = correct_answers / len(batch)
        if success_rate >= 0.7:
            print(f"\nBot: Excellent! You got {correct_answers} out of {len(batch)} right!")
            if pronouns_list:
                print("Moving on to the next set...")
            else:
                print("\nBot: You've mastered pronouns! Congratulations! 🎉")
                break
        else:
            print(f"\nBot: You scored {correct_answers} out of {len(batch)}, that is {(correct_answers/len(batch)*100)}%. You need at least 70% to move on.")
            choice = input("Would you like to try again or take a break? (try again/break): ").lower()
            if choice == "try again":
                pronouns_list = batch + pronouns_list  # Prepend the current batch for a retry
                continue
            elif choice == "break":
                print("\nBot: Taking a break? That's okay, come back anytime to continue learning!")
                break
            else:
                print("\n Invalind input. Please choose right input choice from options next time.")
                break

if __name__ == "__main__":
    clear_screen()
    pronouns_lesson_teaching()

import os
import platform
import random
from openai import OpenAI
from data import numbers_to_learn, greetings_to_learn, nouns_to_learn, pronouns_to_learn, common_phrases_to_learn

api_key = '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'
client = OpenAI(api_key=api_key)

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def get_quiz_question(term, is_english_to_french):
    """Generate a quiz question for translation based on the direction of translation."""
    if is_english_to_french:
        question_formats = [
            f"How do you say '{term}' in French?",
            f"What's the French word for '{term}'?",
            f"Translate '{term}' into French."
        ]
    else:
        question_formats = [
            f"How do you say '{term}' in English?",
            f"What's the English word for '{term}'?",
            f"Translate '{term}' into English."
        ]
    question = random.choice(question_formats)
    return question

def evaluate_and_feedback(question, user_response, correct_answer):
    """Generate feedback based on the user's response compared to the correct answer."""
    correct = user_response.strip().lower() == correct_answer.lower()  # Case-insensitive comparison
    if correct:
        feedback = f"Correct! '{user_response}' is indeed the right answer for '{question}'. Well done!"
        return feedback, True
    else:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "This is a French language mastery quiz. Provide feedback and correct the answers where necessary. Do not use the word 'correct' if the answer was wrong."
                    },
                    {
                        "role": "user",
                        "content": f"Question: {question}\nUser's answer: {user_response}"
                    }
                ],
                temperature=0.7,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            feedback = response.choices[0].message.content.strip()
            return feedback, False
        except Exception as e:
            return f"Error: {str(e)}", False

def run_french_quiz():
    quiz_data = random.sample(list(numbers_to_learn.items()) + list(greetings_to_learn.items()) +
                              list(nouns_to_learn.items()) + list(pronouns_to_learn.items()) +
                              list(common_phrases_to_learn.items()), 10)

    correct_answers = 0
    print("Welcome to the French Language Mastery Quiz! Let's get started.\n")

    for term, translation in quiz_data:
        is_english_to_french = term.isdigit()  # This assumes number data keys are strings of digits
        question = get_quiz_question(term, is_english_to_french)
        print(f"\nBot: {question}")
        user_response = input("Your answer: ").strip()
        feedback, correct = evaluate_and_feedback(question, user_response, translation)
        print(f"Bot: {feedback}")
        if correct:
            correct_answers += 1

    proficiency_levels = {0: "Complete Beginner", 1: "Early Beginner", 2: "Early Beginner",
                          3: "Mid-Beginner", 4: "Mid-Beginner", 5: "Mid-Beginner",
                          6: "Advanced Beginner", 7: "Advanced Beginner", 8: "Advanced Beginner",
                          9: "Excellent", 10: "Perfect"}

    print(f"\nBot: You answered {correct_answers} out of 10 correctly. Based on your performance, I would rate your proficiency within the beginner level of French as {proficiency_levels[correct_answers]}.")

if __name__ == "__main__":
    run_french_quiz()

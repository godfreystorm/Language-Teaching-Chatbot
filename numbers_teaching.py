from openai import OpenAI
import os
import platform
import random
from data import numbers_to_learn  # Your dictionary from 1-50

api_key = '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'
client = OpenAI(api_key=api_key)

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def get_instructional_content(number):
    try:
        response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": f"Explain how to remember the French number for '{number}' in a memorable way."}],
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

def get_quiz_question(number):
    question_formats = [
        f"How do you say '{number}' in French?",
        f"What's the French word for '{number}'?",
        f"Translate '{number}' into French."
    ]
    question = random.choice(question_formats)
    return f"\nBot: {question}"

def evaluate_response(user_response, correct_answer):
    if user_response.lower().strip() == correct_answer:
        return "Bot: Correct!", True
    else:
        return f"Bot: That's not quite right. The correct answer is '{correct_answer}'.", False

def french_numbers_chat():
    print("\nBot: Hi! Welcome to the French numbers learning section.\n")
    
    batches = [list(map(str, range(x, x+5))) for x in range(1, 51, 5)]
    
    batch_index = 0
    while batch_index < len(batches):
        batch = batches[batch_index]
        print(f"\nBot: This round, we're diving into numbers {batch[0]} to {batch[-1]}. Exciting, isn't it?\n")
        
        for number in batch:
            print(get_instructional_content(number))
            input("\nPress Enter once you've grasped the concept and are ready to move on...\n")
        
        print("\nBot: Alright! It's quiz time 🌟 You'll need to get at least 3 out of 5 correct to advance. Hit Enter when you're ready.")
        input()
        clear_screen()
        
        correct_answers = 0
        for number in batch:
            print(get_quiz_question(number))
            user_response = input("Your answer: ").strip()
            feedback, correct = evaluate_response(user_response, numbers_to_learn[number])
            print(feedback)
            if correct:
                correct_answers += 1
        
        if correct_answers >= 3:
            print(f"\nBot: Woohoo! You nailed it with {correct_answers} out of 5 correct! 🚀")
        else:
            print(f"\nBot: Oh no, you got {correct_answers} out of 5. Not quite there, but don't worry! 💪")
        
        # Providing the user with the option to continue, repeat, or take a break
        user_choice = input("\nWould you like to [c]ontinue with the next batch, [r]epeat this one, or take a [b]reak and return to the menu? (c/r/b): ").lower().strip()
        
        if user_choice == 'c':
            if correct_answers >= 3:
                print("\nBot: Great, moving on to the next batch!")
                batch_index += 1
            else:
                print("\nBot: Remember, you need at least 3 out of 5 correct to move to the next batch. Let's try this batch again.")
        elif user_choice == 'r':
            print("\nBot: No problem, let's tackle this batch again!")
        elif user_choice == 'b':
            print("\nBot: Taking a break? No worries, come back anytime you're ready to learn more!")
            break

    print("\nBot: You did it! 🎉 Congratulations on mastering the numbers section. Let's head back to the Main Menu...")


if __name__ == "__main__":
    french_numbers_chat()

from openai import OpenAI
from openai import OpenAI


# Directly include your API key here for the prototype
# Replace 'your_api_key_here' with your actual OpenAI API key
api_key = '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'

client = OpenAI(api_key=api_key)

def french_tutor_chat():
    messages = [
        {"role": "system", "content": "You are a French tutor bot. You're friendly, encouraging, and adjust the lesson's difficulty based on the user's self-assessed level."},
        {"role": "user", "content": "Hi! I'm excited to learn French."},
        {"role": "system", "content": "Bonjour! That's great to hear. What's your current level of French? (Beginner, Intermediate, Advanced)"},
        {"role": "user", "content": "I'm a beginner."},
        {"role": "system", "content": "Perfect, let's start with something simple. 'Bonjour' means 'Hello' in French. 'Comment ça va?' means 'How are you?'. Can you try to use them in a sentence?"},
        {"role": "user", "content": "Bonjour, comment ça va?"},
        {"role": "system", "content": "Excellent! You're already speaking French. Now, let's see if you can translate this sentence from English to French: 'I am fine, thank you.'"},
    ]

    print("Bot: Hi! I'm your French tutor. I'll be teaching you French. Let's start. You can ask me to translate words or phrases from English to French, or ask about French grammar.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bot: Au revoir! Feel free to come back anytime to continue learning.")
            break

        # Add user input to messages
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=messages)

        bot_reply = response.choices[0].message.content
        print("Bot:", bot_reply)

        # Add bot reply to messages for context in subsequent interactions
        messages.append({"role": "system", "content": bot_reply})

if __name__ == "__main__":
    french_tutor_chat()
from openai import OpenAI


# Directly include your API key here for the prototype
# Replace 'your_api_key_here' with your actual OpenAI API key
api_key = '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'

client = OpenAI(api_key=api_key)

def french_tutor_chat():
    messages = [
    {"role": "system", "content": "You are now acting as a direct French translator."},
    {"role": "user", "content": "Translate messages ending with 'in French' into French. If a message does not end with 'in French', respond as you normally would."},
    ]
    
    print("Bot: Hi! I'm your French tutor. I see you've chosen the direct translation section. Please end your translation questions with 'in french' so i can better tell when you just want to talk or want a translation!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Returning to Main Menu...")
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
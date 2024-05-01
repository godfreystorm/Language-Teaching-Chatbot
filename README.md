
# Language Learning Chatbot (LLC)

## Overview
The Language Learning Chatbot (LLC) is an educational tool designed to facilitate learning French through interactive lessons, quizzes, and direct translation functionalities. Developed using Python and leveraging OpenAI's API, LLC offers a user-friendly and engaging platform for users at various stages of their language learning journey.

## Team Members
- Godfrey Osagiede
- Abena Poku
- Mcarthur Diby
- Koffie Yao
- Brian Brooks

## Features
LLC consists of several key features:
- **Direct Translations:** Users can request translations for phrases or sentences, enhancing vocabulary and practical language usage.
- **Interactive Lessons:** Structured lessons on numbers, greetings, nouns, pronouns, and common phrases allow users to learn and practice French in a systematic manner.
- **Quizzes and Assessments:** Modeled after popular language learning apps like Duolingo, the quizzes test the user's knowledge and track progress.
- **Feedback System:** Users can submit feedback directly through the chatbot, contributing to continuous improvement of the application.

## Modules
Each module of LLC focuses on specific aspects of the learning experience:
- **Numbers Teaching:** (`numbers_teaching.py`) Interactive teaching of French numbers with quizzes to test comprehension.
- **Greetings Teaching:** (`greetings_teaching.py`) Lessons on common French greetings and their appropriate usage.
- **Nouns Teaching:** (`nouns_teaching.py`) Focus on French nouns, with mnemonic aids to facilitate memorization.
- **Subject Pronouns Teaching:** (`subject_pronouns_teaching.py`) Detailed explanations of French pronouns and their uses.
- **Phrases Teaching:** (`phrases_teaching.py`) Instruction on key French phrases that are essential for basic conversations.
- **Interactive Module:** (`interactive.py`) Central hub for navigating between different lessons.
- **Chatbot Module:** (`chatbot.py`) Simulates a conversational environment for applying learned content in real-time interactions.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/godfreystorm/Language-Teaching-Chatbot.git
   ```
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To start the chatbot, run:
```
python main.py
```
Follow the on-screen prompts to select a learning module or take quizzes.

## API Key
For individual use and personal development, a new API key must be obtained from OpenAI. All uses of the current API key in the source code must be replaced with the new key. This is necessary because uploading my current API key to GitHub would render it unusable due to security restrictions; however, this does not compromise the project's functionality in any way. The project will continue to operate effectively once a new API key is configured, ensuring users can fully utilize all features without interruption.

## Planned Improvements
- Expansion to include more languages.
- Integration with a web interface for broader accessibility.
- Support for multiple users to handle different learning paths.
- Advanced lessons and voice recognition for a more immersive learning experience.

## Feedback
Your feedback is valuable to us! Please submit any feedback through the chatbot interface or directly into the `feedback.txt` file.

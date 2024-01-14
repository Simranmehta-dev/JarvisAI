# JarvisAI
Jarvis AI
The Jarvis AI script is a Python program designed to function as a voice-controlled assistant. It leverages various external libraries and APIs to perform tasks such as opening websites, playing music, providing the current time, and generating responses using OpenAI's GPT-3.5 Turbo language model.

Key Features:
Voice Recognition: Utilizes the SpeechRecognition library to convert spoken words into text, enabling user interaction through voice commands.

Web Browsing: Opens specified websites like YouTube, Wikipedia, and Google using the webbrowser module based on user commands.

Media Playback: Plays music and opens movies by utilizing the os module to start associated applications.

AI Integration: Incorporates OpenAI's GPT-3.5 Turbo for natural language understanding and generation, allowing the assistant to respond to user queries using advanced language models.

File Logging: Creates individual text files in the 'Openai' directory, logging each interaction with the AI along with corresponding OpenAI responses.

Usage:
Execute the script.
Initiate interactions with the assistant by speaking predefined commands or questions.
The assistant responds audibly and logs interactions in separate text files in the 'Openai' directory.
Dependencies:
speech_recognition
openai
win32com.client
datetime
webbrowser
Note: Ensure proper API keys are configured for OpenAI usage.

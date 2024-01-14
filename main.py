import webbrowser
import datetime
import speech_recognition as sr
import os
import win32com.client
import random
import openai

speaker = win32com.client.Dispatch("SAPI.SpVoice")
def ai(prompt):
    openai.api_key = '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'
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        #prompt=prompt,
        messages=messages,
    temperature = 1,
    max_tokens = 256,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    # text += response["choices"][0]["text"]
    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")
    #
    # # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    # with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
    #     f.write(text)
    text += response["choices"][0]["message"]["content"]

    if not os.path.exists("Openai"):
        os.mkdir("Openai")


    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"Openai/{timestamp}.txt"


    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

while 1:

    print("enter the word")
    # s=input()
    s="hello iam jarvis ai"
    speaker.Speak(s)
    text=takeCommand()

    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"], ]

    # if "Open youtube".lower() in text.lower():
    #     speaker.Speak("opening youtube sir")
    #     webbrowser.open("https://youtube.com")
    for site in sites:
        if f"Open {site[0]}".lower() in text.lower():
            speaker.Speak(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])

    if "open music".lower() in text.lower():
        musicPath = "C:\\Users\\ASUS\\Downloads\\Raam Aayenge(PagalWorld.com.pe).mp3"
        os.startfile(musicPath)

    elif "the time".lower() in text.lower():
        musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
        hour = datetime.datetime.now().strftime("%H")
        min = datetime.datetime.now().strftime("%M")
        speaker.Speak(f"Sir time is {hour} bajke {min} minutes")

    elif "open movie".lower() in text.lower():
        path="C:\\Users\\ASUS\\Downloads\\Telegram Desktop\\When The Promised Flower Blooms [1080p] [Dual] @AN1M_HUB.mkv"
        os.startfile(path)

    # elif "Using artificial intelligence".lower() in query.lower():
    #     ai(prompt=query)

    elif "using ai".lower() in text.lower():
        print("function called called")
        ai(prompt=text)

    speaker.speak(text)




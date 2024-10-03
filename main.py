# from datetime import datetime
# from time import strftime
#
# import speech_recognition as sr
# import os
# import webbrowser
# import datetime
# import openai
#
# from openai import Audio
#
# from wikipedia import languages
#
#
# def say(text):
#     os.system(f"say {text}")
#
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.pause_threshold = 0.6
#         audio = r.listen(source)
#         try:
#             print("Recognizing")
#             query = r.recognize_google(audio, language="en-in")
#             print(f"User said : {query}")
#             return query
#         except Exception as e:
#             return "Some Error occurred. sorry from jarvis"
#
# if __name__ =='__main__':
#     print('pycharm')
#     say("hello i am jarvis A.I")
#     while True:
#         print("Listening...")
#         query = takeCommand()
#         # todo: Add more sites
#         sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
#                  ["google", "https://www.google.com"], ]
#         for site in sites:
#             if f"Open {site[0]}".lower() in query.lower():
#                 say(f"okay i am Opening {site[0]} sir...")
#                 webbrowser.open(site[1])
#         # todo: Add a feature to play a specific song
#         if "play music" in query:
#             musicPath = "/Users/purva/Downloads/downfall-3-208028.mp3"
#             say(f" i am opening  enjoy your music ")
#             # os.startfile(musicPath)
#             # import subprocess ,sys
#             # opener = "open" if sys.platform == "darwin" else "xdg-open"
#             # subprocess.call([opener,musicPath])
#             os.system(f"open {musicPath}")
#         if "the time" in query:
#             musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
#             hour = datetime.datetime.now().strftime("%H")
#             min = datetime.datetime.now().strftime("%M")
#             say(f"Sir time is {hour}   {min} P.M")
#         elif "open facetime".lower() in query.lower():
#             os.system(f"open /System/Applications/FaceTime.app")
#         elif "open calculator".lower() in query.lower():
#             os.system(f"open /System/Applications/Calculator.app")
#         elif "open Dictionary".lower() in query.lower():
#             os.system(f"open /System/Applications/Dictionary.app")
#
#         # say(query)


# import speech_recognition as sr
# import os
# import webbrowser
# import datetime
#
#
# # Function to make Jarvis speak
# def say(text):
#     os.system(f"say {text}")
#
#
# #  recognize voice commands to capture audio input from user ..recognize it and covert into text
# def takeCommand():
#     r = sr.Recognizer()  #Create an instance of the Recognizer class
#     with sr.Microphone() as source:
#         r.pause_threshold = 0.6
#         audio = r.listen(source)
#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language="en-in")
#             print(f"User said: {query}")
#             return query
#         except Exception as e:
#             print(f"Error: {e}")
#             return "Some error occurred. Sorry from Jarvis."
#
# playlist = {
#     "shape of you": "/Users/purva/Documents/Gallery/music/ed_sheeran_shape_of_you_lyrics_mp3_42542.mp3",
#     "photograph": "/Users/purva/Documents/Gallery/music/ed_sheeran_photograph_lyrics_mp3_42449.mp3",
#     "let me down slowly": "/Users/purva/Documents/Gallery/music/alec_benjamin_let_me_down_slowly_lyrics_mp3_42666.mp3"
# }
#
# # Function to play a specific songs
# def play_music(song_name):
#     if song_name in playlist:
#         music_path = playlist[song_name]
#         os.system(f"open {music_path}")  # Opens and plays the song using the default music player
#         say(f"Playing {song_name}. Enjoy your music!")
#     else:
#         say(f"Sorry, I could not find {song_name} in your playlist.")
#
#
#
# if __name__ == '__main__':
#     say("Hello! I am Jarvis. How can I assist you today?")
#
#     while True:
#         print("Listening...")
#         query = takeCommand().lower()  # Normalize input for easier matching
#
#         # Respond to thank you
#         if "thank you" in query:
#             say("You're welcome! I'm here to help you!")
#             continue  # Skip to the next iteration
#
#         # Command to open websites
#         sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
#                  ["google", "https://www.google.com"]]
#         for site in sites:
#             if f"open {site[0]}".lower() in query:
#                 say(f"Okay, I am opening {site[0]} sir...")
#                 webbrowser.open(site[1])
#                 break  # Exit the loop after opening a site
#
#         # Play specific songs by name
#         if "play music" in query:
#             say("Which song would you like to play?")
#             song_query = takeCommand().lower()  # Listen for the song name
#             play_music(song_query)  # Play the requested song
#             continue  # Skip to the next iteration
#
#         # Tell the time
#         if "the time" in query:
#             hour = datetime.datetime.now().strftime("%H")
#             minute = datetime.datetime.now().strftime("%M")
#             say(f"Sir, the time is {hour} {minute}. P.M")
#
#         # Open specific  apps
#         if "open facetime" in query:
#             os.system("open /System/Applications/FaceTime.app")
#         elif "open calculator" in query:
#             os.system("open /System/Applications/Calculator.app")
#         elif "open dictionary" in query:
#             os.system("open /System/Applications/Dictionary.app")
# # say(query)
import speech_recognition as sr
import os
import webbrowser
import datetime
import pyjokes


# Function to make Jarvis speak
def say(text):
    os.system(f"say {text}")


#  recognize voice commands to capture audio input from user ..recognize it and covert into text
def takeCommand():
    r = sr.Recognizer()  # Create an instance of the Recognizer class
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "Some error occurred. Sorry from Jarvis."


playlist = {
    "shape of you": "/Users/purva/Documents/Gallery/music/ed_sheeran_shape_of_you_lyrics_mp3_42542.mp3",
    "photograph": "/Users/purva/Documents/Gallery/music/ed_sheeran_photograph_lyrics_mp3_42449.mp3",
    "let me down slowly": "/Users/purva/Documents/Gallery/music/alec_benjamin_let_me_down_slowly_lyrics_mp3_42666.mp3"
}



# Function to play specific songs
def play_music(song_name):
    if song_name in playlist:
        music_path = playlist[song_name]
        os.system(f"open {music_path}")  # Opens and plays the song using the default music player
        say(f"Playing {song_name}. Enjoy your music!")
    else:
        say(f"Sorry, I could not find {song_name} in your playlist.")


if __name__ == '__main__':
    say("Hello! I am Jarvis. How can I assist you today?")

    while True:
        print("Listening...")
        query = takeCommand().lower()  # Normalize input for easier matching

        # Exit the program
        if "exit" in query or "stop" in query:
            say("Goodbye! Have a great day!")
            break  # Break out of the loop and exit

        # Respond to thank you
        if "thank you" in query:
            say("You're welcome! I'm here to help you!")
            continue  # Skip to the next iteration

        # Command to open websites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query:
                say(f"Okay, I am opening {site[0]} sir...")
                webbrowser.open(site[1])
                break  # Exit the loop after opening a site

        # Play specific songs by name
        if "play music" in query:
            say("Which song would you like to play?")
            song_query = takeCommand().lower()  # Listen for the song name
            if song_query:
                play_music(song_query)  # Play the requested song
            else:
                say("Sorry, I couldn't understand the song name.")
            continue  # Skip to the next iteration

        # Tell the time with AM/PM
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%I")  # 12-hour format
            minute = datetime.datetime.now().strftime("%M")
            period = datetime.datetime.now().strftime("%p")  # AM/PM
            say(f"Sir, the time is {hour} {minute} {period}")

        # Open specific apps
        if "open facetime" in query:
            os.system("open /System/Applications/FaceTime.app")
        elif "open calculator" in query:
            os.system("open /System/Applications/Calculator.app")
        elif "open dictionary" in query:
            os.system("open /System/Applications/Dictionary.app")
        elif "offline" in query:
            quit()
        elif "joke" in query:
            speak(pyjokes.get_joke())

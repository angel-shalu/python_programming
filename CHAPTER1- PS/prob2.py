"""
2.. Use REPL and print the table of 5 using it
It is done in the terminal
"""

# 3...Installation on pytts3 and perform the action
# ..... this module is use to covert the code in oral form

import pyttsx3  # type: ignore 
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

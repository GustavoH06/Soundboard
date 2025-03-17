import tkinter as Tk
from tkinter import *
from PIL import Image, ImageTk
import winsound
import random
import keyboard
import threading

# Sound library organized into situations
soundLibrary = {
    
    "greeting": [
        "Sounds/Greeting/DontFeedTheAnimals.wav",
        "Sounds/Greeting/GermanHi.wav",
        "Sounds/Greeting/Greetings.wav",
        "Sounds/Greeting/Hello.wav",
        "Sounds/Greeting/HelloShield.wav",
        "Sounds/Greeting/HelloWelcome.wav",
        "Sounds/Greeting/HelloYoungLady.wav",
        "Sounds/Greeting/HiSpanish.wav",
        "Sounds/Greeting/Hi.wav"

    ],
    "gratitude": [
        "Sounds/Gratitude/AreYouDoctor.wav",
        "Sounds/Gratitude/GreatService.wav",
        "Sounds/Gratitude/HiThankYou.wav",
        "Sounds/Gratitude/IdLikeAnotherOne.wav",
        "Sounds/Gratitude/IExpected.wav",
        "Sounds/Gratitude/IHadAGreatTime.wav",
        "Sounds/Gratitude/ItArrived.wav",
        "Sounds/Gratitude/NiceComany.wav",
        "Sounds/Gratitude/PleasantSensation.wav",
        "Sounds/Gratitude/ReallyEnjoyedThat.wav",
        "Sounds/Gratitude/Satisfaction.wav",
        "Sounds/Gratitude/ThanksInAdvance.wav",
        "Sounds/Gratitude/ThankYou.wav",
        "Sounds/Gratitude/ThankYouVeryMuch.wav" 
    ],
}

#Window config
Window = Tk()
Window.geometry("800x600")
Window.title("Jackeson")
Window.maxsize(1000,700)
Window.resizable(False, False)
Window.configure(bg="#2A2929")

SoundboardButton = ImageTk.PhotoImage(file="Assets/Button.png")

#Window design
def Create_Window():
    photo = Image.open("chicken.png").resize((300, 100))
    Iconphoto = ImageTk.PhotoImage(photo, Image.LANCZOS)
    Window.iconphoto(True, Iconphoto)
    Window.config(background = "light blue")

def playSound(soundGroup):
    if soundGroup in soundLibrary:
        randomSound = random.choice(soundLibrary[soundGroup])
        winsound.PlaySound(randomSound, winsound.SND_ASYNC + winsound.SND_FILENAME)

#Generates a button based on the sound group
def generateButton(text, soundGroup, bind, row, col):
    button = Button(
        Window,
        text=text,
        image=SoundboardButton,
        compound="center",
        height=150,
        width=200,
        background="#000000",
        relief="solid",
        activebackground="#000000",
        command=lambda: playSound(soundGroup)
    )
    button.grid(row=row, column=col, padx=20, pady=20)

    keyboard.add_hotkey(bind.lower(), lambda: playSound(soundGroup))

# Manually create buttons with center alignment
generateButton("Greeting", "greeting", "g", row=1, col=0)
generateButton("Gratitude", "gratitude", "h", row=1, col=1)  # This will be in the center
generateButton("Test", "greeting", "j", row=1, col=2)

# Center the buttons using column configuration

Window.grid_columnconfigure(0, weight=1, uniform="equal")
Window.grid_columnconfigure(1, weight=1, uniform="equal")  # Center column
Window.grid_columnconfigure(2, weight=1, uniform="equal")

def runBackground():
    keyboard.wait()

hotkey_thread = threading.Thread(target=runBackground, daemon=True)
hotkey_thread.start()

Create_Window()


Window.mainloop()
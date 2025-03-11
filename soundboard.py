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

#Window design
def Create_Window():
    photo = Image.open("chicken.png").resize((300, 100))
    Iconphoto = ImageTk.PhotoImage(photo, Image.LANCZOS)
    Window.iconphoto(True, Iconphoto)
    Window.config(background = "light blue")

    SoundboardButton = ImageTk.PhotoImage(file="Neuromancer.jpg")

    #Different buttons (to be optimized)
    greetingsButton = Button(Window, text="Greeting", image=SoundboardButton, compound="center", height=150, width=200, background="#000000", relief="solid", activebackground="#000000", command=playRandomGratitude)
    greetingsButton.grid(row=1, column=1, padx=20, pady=20, sticky="we")
    gratitudeButton = Button(Window, text="Gratitude", image=SoundboardButton, compound="center", height=150, width=200, background="#000000", relief="solid", activebackground="#000000", command=playRandomGreeting)
    gratitudeButton.grid(row=1, column=2, padx=20, pady=20, sticky="we")

    #Bind key
    Window.bind('<g>', lambda event: playRandomGreeting())
    Window.bind('<h>', lambda event: playRandomGratitude())
    # Keep reference to the image to avoid garbage collection
    greetingsButton.image = SoundboardButton

# Function that plays a random greeting sound
def playRandomGreeting():
    # Randomly choose a sound from the "greetings" list
    randomGreeting = random.choice(soundLibrary["greeting"])
    winsound.PlaySound(randomGreeting, winsound.SND_ASYNC + winsound.SND_FILENAME)
def playRandomGratitude():
    # Randomly choose a sound from the "greetings" list
    randomGratitude = random.choice(soundLibrary["gratitude"])
    winsound.PlaySound(randomGratitude, winsound.SND_ASYNC + winsound.SND_FILENAME)

def handleHotkeys():
    # Listen for the 'g' key globally
    keyboard.add_hotkey('g', playRandomGreeting)
    keyboard.add_hotkey('h', playRandomGratitude)

    # Keep the program running to listen for key events
    keyboard.wait()

hotkey_thread = threading.Thread(target=handleHotkeys, daemon=True)
hotkey_thread.start()

Create_Window()

# Create the window loop
Window.mainloop()
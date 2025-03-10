import tkinter as Tk
from tkinter import *
from PIL import Image, ImageTk
import winsound
import random
import keyboard
import threading

# Create sound library dictionary with lists of sounds for different categories
soundLibrary = {
    "gratitude": [
        "Sounds/Gratitude/NiceComany.wav",
        "Sounds/Gratitude/PleasantSensation.wav",
        "Sounds/Gratitude/ReallyEnjoyedThat.wav",
        "Sounds/Gratitude/ThankYouVeryMuch"
    ],
    # Add other sound categories here as needed, like:
    # "alerts": ["Sounds/Alert/Beep.wav", "Sounds/Alert/Warning.wav"]
}

Window = Tk()
Window.geometry("800x600")
Window.title("Jackeson")
Window.resizable(True, True)
Window.configure(bg="#2A2929")

def Create_Window():
    # Icon photo
    photo = Image.open("chicken.png").resize((300, 100))
    Iconphoto = ImageTk.PhotoImage(photo, Image.LANCZOS)
    Window.iconphoto(True, Iconphoto)

    # Soundboard Button Image
    SoundboardButton = ImageTk.PhotoImage(file="Neuromancer.jpg")

    # Create the Greetings button
    greetingsButton = Button(Window, text="Greetings", image=SoundboardButton, compound="center", height=200, width=150, background="#000000", relief="solid", activebackground="#000000", command=playRandomGreeting)
    greetingsButton.grid(row=1, column=1, padx=20, pady=20, sticky="we")

    #Bind key
    Window.bind('<g>', lambda event: playRandomGreeting())
    # Keep reference to the image to avoid garbage collection
    greetingsButton.image = SoundboardButton

# Function that plays a random greeting sound
def playRandomGreeting():
    # Randomly choose a sound from the "greetings" list
    randomSound = random.choice(soundLibrary["gratitude"])
    winsound.PlaySound(randomSound, winsound.SND_ASYNC + winsound.SND_FILENAME)

def handleHotkeys():
    # Listen for the 'g' key globally
    keyboard.add_hotkey('g', playRandomGreeting)

    # Keep the program running to listen for key events
    keyboard.wait()

hotkey_thread = threading.Thread(target=handleHotkeys, daemon=True)
hotkey_thread.start()

Create_Window()

# Create the window loop
Window.mainloop()
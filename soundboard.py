import tkinter as Tk
from tkinter import *
from PIL import Image, ImageTk
import winsound
import random
import keyboard
import threading

#Sound library
soundLibrary = {
    
    "acknowledged": [

    ],
    "completeMission": [
    ],
    "funfact": [
        "Sounds/Done/FunFact/FunArcadeaaasfas.wav",
        "Sounds/Done/FunFact/FunBanana.wav",
        "Sounds/Done/FunFact/FunCouch.wav",
        "Sounds/Done/FunFact/FunDallas.wav",
        "Sounds/Done/jFunFact/FunDecaptation.wav",
        "Done/Sounds/FunFact/FunDoomsday.wav",
        "Done/Sounds/FunFact/FunFlash.wav",
        "Done/Sounds/FunFact/FunHome.wav",
        "Done/Sounds/FunFact/FunIdentity.wav",
        "Done/Sounds/FunFact/FunNeeds.wav",
        "Done/Sounds/FunFact/FunNeon.wav",
        "Done/Sounds/FunFact/FunNes.wav",
        "DoneSounds/FunFact/FunNutrition.wav",
        "Done/Sounds/FunFact/FunPlants.wav",
        "Done/Sounds/FunFact/FunSpace.wav",
        "DoneSounds/FunFact/FunTelevision.wav",
        "DoneSounds/FunFact/FunTv.wav",
        "Done/Sounds/FunFact/FunWeapon.wav",
        "DoneSounds/FunFact/FunZebra.wav"
    ],
    "greeting": [
        "Sounds/Greeting/DontFeedTheAnimals.wav",
        "Sounds/Greeting/GermanHi.wav",
        "Sounds/Greeting/Greetings.wav",
        "Sounds/Greeting/Hello.wav",
        "Sounds/Greeting/HelloLady.wav",
        "Sounds/Greeting/HelloWelcome.wav",
        "Sounds/Greeting/Hi.wav",
        "Sounds/Greeting/HiHello.wav",
        "Sounds/Greeting/HiSpanish.wav"
    ],
    "gratitude": [
        "Sounds/Gratitude/AreYouADoctor.wav",
        "Sounds/Gratitude/ExpressSatisfaction.wav",
        "Sounds/Gratitude/HiThankYou.wav",
        "Sounds/Gratitude/HowNice.wav",
        "Sounds/Gratitude/IdLikeAnotherOne.wav",
        "Sounds/Gratitude/IExpected.wav",
        "Sounds/Gratitude/IHadAGreatTime.wav",
        "Sounds/Gratitude/IReallyEnjoyedThat.wav",
        "Sounds/Gratitude/ItHasArrived.wav",
        "Sounds/Gratitude/Pleasant.wav",
        "Sounds/Gratitude/ServiceHere.wav",
        "Sounds/Gratitude/ThanksInAdvance.wav",
        "Sounds/Gratitude/ThankYou.wav",
        "Sounds/Gratitude/ThankYouVeryMuch.wav"
    ],
    "helpme": [

    ],
    "helpTeam": [
        "Sounds/HelpingTeam/FirstAidLocate.wav",

    ],
    "incoming": [

    ],
    "intimidation": [

    ],
    "inspire": [

    ],
    "initiating": [

    ],
    "responsewait":[

    ],
    "roberry":[

    ]
    


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

#Play sound function
def playSound(soundGroup):
    if soundGroup in soundLibrary:
        randomSound = random.choice(soundLibrary[soundGroup])
        winsound.PlaySound(randomSound, winsound.SND_ASYNC + winsound.SND_FILENAME)

#Button generator based on category
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

generateButton("Greeting", "greeting", "g", row=1, col=0)
generateButton("Gratitude", "gratitude", "h", row=1, col=1)
generateButton("FunFact", "funfact", "j", row=1, col=2)
generateButton("Help Team", "helpTeam", "k", row=2, col=0)

Window.grid_columnconfigure(0, weight=1, uniform="equal")
Window.grid_columnconfigure(1, weight=1, uniform="equal")  
Window.grid_columnconfigure(2, weight=1, uniform="equal")

def runBackground():
    keyboard.wait()

hotkeyThread = threading.Thread(target=runBackground, daemon=True)
hotkeyThread.start()

Create_Window()

Window.mainloop()
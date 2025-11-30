import pyttsx3
import threading

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Use a female voice if available
    for v in voices:
        if "Zira" in v.name or "female" in v.name.lower():
            engine.setProperty('voice', v.id)
            break

    # Slow down the speed for a smoother, more natural tone
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 💬")
    while True:
        x = input("Enter what you want me to speak (or 'q' to quit): ")
        if x.lower() == 'q':
            print("Goodbye! 👋")
            break
        threading.Thread(target=speak, args=(x,)).start()
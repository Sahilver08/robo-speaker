🤖 RoboSpeaker 💬

A fun and interactive Python mini project that converts your text into speech — now powered with multithreading for smooth, non-blocking voice output!

This project demonstrates text-to-speech (TTS) in Python using the pyttsx3 library along with threading to handle multiple speech requests simultaneously.

🎮 Project Description

RoboSpeaker takes any text input from the user and speaks it aloud using your system’s built-in voice.
It continues taking new input until you type q to quit.

With threading, each spoken message runs in its own thread, allowing the user to continue typing without waiting for speech to finish.

🧠 Features

✅ Converts text to speech using the pyttsx3 library
✅ Supports real-time input — no lag while speaking
✅ Works offline (no internet required)
✅ Cross-platform: Works on Windows, macOS, and Linux
✅ Beginner-friendly Python project

🧩 Code Overview
import pyttsx3
import threading

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
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

🚀 How to Run

Clone this repository:

git clone https://github.com/Sahilver08/robo-speaker


Navigate to the RoboSpeaker folder:

cd mini-games/robo-speaker


Install required library:

pip install pyttsx3


Run the program:

python robospeaker.py

💡 Example Output
Welcome to RoboSpeaker 💬
Enter what you want me to speak (or 'q' to quit): Hello Sahil
💬 [Computer speaks "Hello Sahil"]
Enter what you want me to speak (or 'q' to quit): Python is fun!
💬 [Computer speaks "Python is fun!"]
Enter what you want me to speak (or 'q' to quit): q
Goodbye! 👋

🧰 Technologies Used

Python 3

pyttsx3 (Text-to-Speech Engine)

threading (for concurrency)

📚 Learning Highlights

This project helps you learn:

Using the pyttsx3 library for offline TTS

Implementing multithreading in Python

Handling user input loops

Writing clean and interactive console applications

🤝 Contributing

Feel free to fork this repository and improve RoboSpeaker —
you can add features like:

Voice customization (male/female)

Adjustable pitch or speed controls

GUI interface with Tkinter or PyQt

Pull requests are welcome! 😊

🏆 Author

Sahil Verma
Python Developer | Full Stack Learner | AI/ML Enthusiast
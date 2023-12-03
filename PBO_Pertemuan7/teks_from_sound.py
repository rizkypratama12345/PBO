from gtts import gTTS
import os
import platform
import tkinter as tk
from tkinter import Label, Entry, Button

def text_to_speech(text, language='id', output_file='output.mp3'):
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_file)

        if platform.system() == 'Windows':
            os.system(f"start {output_file}")
        else:
            print("Unsupported operating system. Please play the audio file manually.")

        # Optional: Clean up the audio file after playing
        # os.remove(output_file)

    except Exception as e:
        print(f"Error: {e}")

def convert_text():
    input_text = text_entry.get()
    text_to_speech(input_text)

# Create the main window
window = tk.Tk()
window.title("Text-to-Speech Converter")

# Styling
window.geometry("400x200")  # Set the initial size of the window
window.configure(bg="#f0f0f0")  # Set the background color

# Create GUI components
label = Label(window, text="Enter the text to convert to speech:", font=("Helvetica", 12), bg="#f0f0f0")
label.pack(pady=10)

text_entry = Entry(window, width=50, font=("Helvetica", 10))
text_entry.pack(pady=10)

convert_button = Button(window, text="Convert", command=convert_text, font=("Helvetica", 12), bg="#4CAF50", fg="white")
convert_button.pack(pady=10)

# Run the application
window.mainloop()

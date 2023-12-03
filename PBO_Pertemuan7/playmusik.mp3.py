import tkinter as tk
from tkinter import ttk, filedialog
import pygame

class SoundPlayerApp:
    def __init__(self, master):
        self.master = master
        master.title("Sound Player App")
        master.geometry("400x300")
        master.config(bg="#3E4651")

        # Inisialisasi Pygame
        pygame.init()

        self.create_widgets()
        
        title_label = tk.Label(master, text="MUHAMMAD FARHAN SAINO", font=("Helvetica", 10), bg="white")
        title_label.pack(pady=30)

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#48C9B0", foreground="#2C3E50", font=("Helvetica", 12))
        style.configure("TLabel", padding=6, background="#3E4651", foreground="#ECF0F1", font=("Helvetica", 12))
        style.configure("TFrame", padding=6, background="#3E4651")

        frame = ttk.Frame(self.master)
        frame.pack(pady=20)

        self.play_button = ttk.Button(frame, text="Play Sound", command=self.play_sound)
        self.play_button.grid(row=0, column=0, padx=10)

        self.stop_button = ttk.Button(frame, text="Stop Sound", command=self.stop_sound)
        self.stop_button.grid(row=0, column=1, padx=10)

        self.select_button = ttk.Button(self.master, text="Select Music", command=self.select_music)
        self.select_button.pack(pady=10)

        self.quit_button = ttk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack()
        

        self.selected_music = None
        self.sound_playing = False

    def play_sound(self):
        if self.selected_music:
            try:
                pygame.mixer.music.load(self.selected_music)
                pygame.mixer.music.play()
                self.sound_playing = True
            except Exception as e:
                print(f"Error playing sound: {e}")

    def stop_sound(self):
        pygame.mixer.music.stop()
        self.sound_playing = False

    def select_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Sound Files", "*.mp3;*.wav")])
        if file_path:
            self.selected_music = file_path
            print(f"Selected music: {self.selected_music}")
            if self.sound_playing:
                self.stop_sound()

if __name__ == "__main__":
    root = tk.Tk()
    app = SoundPlayerApp(root)
    root.mainloop()

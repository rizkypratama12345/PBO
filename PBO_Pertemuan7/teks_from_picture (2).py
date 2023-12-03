from tkinter import Tk, Button, Label, filedialog, Frame, LEFT, RIGHT
from PIL import Image, ImageTk
from pytesseract import pytesseract

# Define path to tesseract.exe (update this path based on your Tesseract installation on Windows)
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        process_image(file_path)

def process_image(image_path):
    pytesseract.tesseract_cmd = path_to_tesseract

    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)

    result_label.config(text=text)

    img.thumbnail((400, 400))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

# Create Tkinter window
window = Tk()
window.title("OCR with Tkinter")

# Create and pack widgets
frame = Frame(window, pady=10)
frame.pack()

open_button = Button(frame, text="Open Image", command=open_file_dialog)
open_button.pack(side=LEFT, padx=10)

result_label = Label(frame, text="", wraplength=400, justify="left", font=("Arial", 12))
result_label.pack(side=RIGHT, padx=10)

# Label to display the image (optional)
image_label = Label(window)
image_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()

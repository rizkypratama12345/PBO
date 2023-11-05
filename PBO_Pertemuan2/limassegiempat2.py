import tkinter as tk

def hitung_luas_permukaan():
    try:
        alas = float(entryAlas.get())
        tinggi = float(entryTinggi.get())
        luas_permukaan = alas * alas + 4 * (0.5 * alas * tinggi)

        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, f'Luas Permukaan: {luas_permukaan:.2f} satuan persegi')
    except ValueError:
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, 'Masukkan angka yang valid')

def hitung_volume():
    try:
        alas = float(entryAlas.get())
        tinggi = float(entryTinggi.get())
        volume = (1 / 3) * alas * alas * tinggi

        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, f'Volume: {volume:.2f} satuan kubik')
    except ValueError:
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, 'Masukkan angka yang valid')

app = tk.Tk()
app.title("Kalkulator Limas Segiempat")
app.geometry('400x450')

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

labelAlas = tk.Label(frame, text="Panjang Alas: ", font=('Arial', 12))
labelAlas.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

entryAlas = tk.Entry(frame, font=('Arial', 12))
entryAlas.grid(row=0, column=1)

labelTinggi = tk.Label(frame, text="Tinggi Limas: ", font=('Arial', 12))
labelTinggi.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

entryTinggi = tk.Entry(frame, font=('Arial', 12))
entryTinggi.grid(row=1, column=1)

luasButton = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan, font=('Arial', 12), bg='lightblue', padx=5, pady=5)
luasButton.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

volumeButton = tk.Button(frame, text="Hitung Volume", command=hitung_volume, font=('Arial', 12), bg='lightgreen', padx=5, pady=5)
volumeButton.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

textLuas = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textLuas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

textVolume = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textVolume.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()

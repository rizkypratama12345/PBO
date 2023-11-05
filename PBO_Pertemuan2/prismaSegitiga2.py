import tkinter as tk

def hitung_luas_permukaan():
    try:
        alas = float(entryAlas.get())
        tinggi_alas = float(entryTinggiAlas.get())
        tinggi_prisma = float(entryTinggiPrisma.get())

        luas_permukaan = (alas * tinggi_alas) + 3 * (alas * tinggi_prisma)
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, f'Luas Permukaan: {luas_permukaan:.2f} satuan persegi')
    except ValueError:
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, 'Masukkan angka yang valid')

def hitung_volume():
    try:
        alas = float(entryAlas.get())
        tinggi_prisma = float(entryTinggiPrisma.get())

        volume = (1/2) * alas * tinggi_prisma
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, f'Volume: {volume:.2f} satuan kubik')
    except ValueError:
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, 'Masukkan angka yang valid')

app = tk.Tk()
app.title("Kalkulator Prisma Segitiga")
app.geometry('400x450')

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

labelAlas = tk.Label(frame, text="Alas Segitiga: ", font=('Arial', 12))
labelAlas.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

entryAlas = tk.Entry(frame, font=('Arial', 12))
entryAlas.grid(row=0, column=1)

labelTinggiAlas = tk.Label(frame, text="Tinggi Alas: ", font=('Arial', 12))
labelTinggiAlas.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

entryTinggiAlas = tk.Entry(frame, font=('Arial', 12))
entryTinggiAlas.grid(row=1, column=1)

labelTinggiPrisma = tk.Label(frame, text="Tinggi Prisma: ", font=('Arial', 12))
labelTinggiPrisma.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

entryTinggiPrisma = tk.Entry(frame, font=('Arial', 12))
entryTinggiPrisma.grid(row=2, column=1)

luasButton = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan, font=('Arial', 12), bg='lightblue', padx=5, pady=5)
luasButton.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

volumeButton = tk.Button(frame, text="Hitung Volume", command=hitung_volume, font=('Arial', 12), bg='lightgreen', padx=5, pady=5)
volumeButton.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

textLuas = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textLuas.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

textVolume = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textVolume.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()

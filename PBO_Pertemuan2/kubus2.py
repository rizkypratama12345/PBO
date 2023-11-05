import tkinter as tk

def hitung_luas_permukaan():
    try:
        sisi = float(entrySisi.get())
        luas_permukaan = 6 * sisi**2
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, f'Luas Permukaan: {luas_permukaan:.2f} satuan persegi')
    except ValueError:
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, 'Masukkan angka yang valid')

def hitung_volume():
    try:
        sisi = float(entrySisi.get())
        volume = sisi**3
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, f'Volume: {volume:.2f} satuan kubik')
    except ValueError:
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, 'Masukkan angka yang valid')

app = tk.Tk()
app.title("Kalkulator Kubus")
app.geometry('400x400')

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

labelSisi = tk.Label(frame, text="Panjang Sisi: ", font=('Arial', 12))
labelSisi.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

entrySisi = tk.Entry(frame, font=('Arial', 12))
entrySisi.grid(row=0, column=1)

luasButton = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan, font=('Arial', 12), bg='lightblue', padx=5, pady=5)
luasButton.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

volumeButton = tk.Button(frame, text="Hitung Volume", command=hitung_volume, font=('Arial', 12), bg='lightgreen', padx=5, pady=5)
volumeButton.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

textLuas = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textLuas.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

textVolume = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textVolume.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

nama = tk.Label(frame, text="Rizky Pratama ", font=('Arial', 12))
nama.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

nama = tk.Label(frame, text="220511030 ", font=('Arial', 12))
nama.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)

app.mainloop()

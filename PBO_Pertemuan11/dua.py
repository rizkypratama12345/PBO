import tkinter as tk
from tkinter import messagebox

def is_prime(number):
    """Fungsi untuk memeriksa apakah suatu bilangan adalah bilangan prima atau bukan."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def check_prime():
    """Fungsi untuk menampilkan pesan apakah suatu bilangan adalah bilangan prima atau bukan."""
    try:
        user_input = int(entry.get())
        if is_prime(user_input):
            messagebox.showinfo("Hasil", f"{user_input} adalah bilangan prima.")
        else:
            messagebox.showinfo("Hasil", f"{user_input} bukan bilangan prima.")
    except ValueError:
        messagebox.showerror("Error", "Masukkan bilangan bulat saja.")

def display_primes():
    """Fungsi untuk menampilkan semua bilangan prima dalam suatu range data."""
    try:
        start = int(entry_start.get())
        end = int(entry_end.get())
        primes = [str(num) for num in range(start, end + 1) if is_prime(num)]
        result_text = "\n".join(primes)
        messagebox.showinfo("Bilangan Prima", f"Bilangan prima dalam range {start} sampai {end}:\n{result_text}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan bilangan bulat saja.")

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Pemeriksa Bilangan Prima")

# Widget dan layout untuk pemeriksa bilangan prima tunggal
label = tk.Label(root, text="Masukkan bilangan:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

check_button = tk.Button(root, text="Cek Prima", command=check_prime)
check_button.pack(pady=10)

# Widget dan layout untuk menampilkan bilangan prima dalam suatu range data
label_range = tk.Label(root, text="Masukkan range (mulai dan akhir):")
label_range.pack(pady=10)

entry_start = tk.Entry(root)
entry_start.pack(pady=5)

entry_end = tk.Entry(root)
entry_end.pack(pady=10)

display_button = tk.Button(root, text="Tampilkan Bilangan Prima", command=display_primes)
display_button.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()

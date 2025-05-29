import tkinter as tk
import random


punkti1 = 0
punkti2 = 0


def met_kaulinu(speletajs):
    global punkti1, punkti2


    metiens = random.randint(1, 6)
    rezultats_label.config(text=f"Kauliņš: {metiens}")

    if speletajs == 1:
        punkti1 += metiens
        speletajs1_label.config(text=f"Spēlētājs 1: {punkti1} punkti")
        if punkti1 >= 30:
            rezultats_label.config(text="Spēlētājs 1 uzvarēja!")
            atslēgt_pogas()
    else:
        punkti2 += metiens
        speletajs2_label.config(text=f"Spēlētājs 2: {punkti2} punkti")
        if punkti2 >= 30:
            rezultats_label.config(text="Spēlētājs 2 uzvarēja!")
            atslēgt_pogas()


def atslēgt_pogas():
    poga1.config(state="disabled")
    poga2.config(state="disabled")


def restartet_spele():
    global punkti1, punkti2
    punkti1 = 0
    punkti2 = 0
    speletajs1_label.config(text="Spēlētājs 1: 0 punkti")
    speletajs2_label.config(text="Spēlētājs 2: 0 punkti")
    rezultats_label.config(text="")
    poga1.config(state="normal")
    poga2.config(state="normal")


logs = tk.Tk()
logs.title("Kauliņu sacīkstes")
logs.geometry("350x250")


speletajs1_label = tk.Label(logs, text="Spēlētājs 1: 0 punkti", font=("Arial", 12))
speletajs1_label.pack(pady=5)

speletajs2_label = tk.Label(logs, text="Spēlētājs 2: 0 punkti", font=("Arial", 12))
speletajs2_label.pack(pady=5)


poga1 = tk.Button(logs, text="Spēlētājs 1 met", command=lambda: met_kaulinu(1))
poga1.pack(pady=5)

poga2 = tk.Button(logs, text="Spēlētājs 2 met", command=lambda: met_kaulinu(2))
poga2.pack(pady=5)


rezultats_label = tk.Label(logs, text="", font=("Arial", 14))
rezultats_label.pack(pady=10)
restart_poga = tk.Button(logs, text="Sākt no jauna", command=restartet_spele)
restart_poga.pack()


logs.mainloop()

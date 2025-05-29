import tkinter as tk


def mainit_fona_krasu(krasa):
    logs.configure(bg=krasa)


def mainit_teksta_krasu(krasa):
    virsraksts.config(fg=krasa)


logs = tk.Tk()
logs.title("Krāsu kombinētājs")
logs.geometry("500x300") 


virsraksts = tk.Label(logs, text="Izvēlies krāsas!", font=("Arial", 18))
virsraksts.pack(pady=20)


fona_ramis = tk.Frame(logs)
fona_ramis.pack(pady=10)

fona_krasas = ["blue", "green", "yellow", "red", "white"]
for krasa in fona_krasas:
    poga = tk.Button(fona_ramis, text=krasa, bg=krasa, width=10,
                     command=lambda k=krasa: mainit_fona_krasu(k))
    poga.pack(side="left", padx=5)


teksta_ramis = tk.Frame(logs)
teksta_ramis.pack(pady=10)

teksta_krasas = ["black", "red", "blue", "green", "purple"]
for krasa in teksta_krasas:
    poga = tk.Button(teksta_ramis, text=krasa, fg=krasa, width=10,
                     command=lambda k=krasa: mainit_teksta_krasu(k))
    poga.pack(side="left", padx=5)


logs.mainloop()

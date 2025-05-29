from datetime import datetime


vards = input("Ievadi savu vārdu (vismaz 3 burti): ")
while len(vards.strip()) < 3:
    vards = input("Vārds par īsu. Ievadi vēlreiz: ")


sakums = datetime.now()


with open("rezultati.txt", "a", encoding="utf-8") as f:
    f.write(f"\n--- Tests ---\n")
    f.write(f"Vārds: {vards}\n")
    f.write(f"Sākums: {sakums}\n")


print("\n1. Kā Python lasa failu?")
print("a) open  b) write  c) print")
atbilde = input("Atbilde: ")
punkti = 1 if atbilde.strip().lower() == "a" else 0

beigas = datetime.now()
ilgums = beigas - sakums


with open("rezultati.txt", "a", encoding="utf-8") as f:
    f.write(f"Beigas: {beigas}\n")
    f.write(f"Punkti: {punkti}\n")
    f.write(f"Ilgums: {ilgums.seconds} sekundes\n")


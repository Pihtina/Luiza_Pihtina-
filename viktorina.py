
def sanemt_jautajumus():
    return [
        {
            "jautajums": "Kāda ir Latvijas galvaspilsēta?",
            "atbildes": ["Daugavpils", "Rīga", "Liepāja", "Jelgava"],
            "pareiza": 1
        },
        {
            "jautajums": "Kurā gadā Latvija atguva neatkarību?",
            "atbildes": ["1918", "1940", "1990", "2004"],
            "pareiza": 2
        },
        {
            "jautajums": "Kur atrodas Gaujas Nacionālais parks?",
            "atbildes": ["Kurzemē", "Zemgalē", "Vidzeme", "Latgalē"],
            "pareiza": 2
        }
    ]


def uzdot_jautajumu(jautajums_obj):
    print("\n" + jautajums_obj["jautajums"])
    for i, atbilde in enumerate(jautajums_obj["atbildes"]):
        print(f"{i + 1}. {atbilde}")
    
    atbilde = input("Ievadi pareizās atbildes numuru (1-4): ")

    if atbilde.isdigit():
        if int(atbilde) - 1 == jautajums_obj["pareiza"]:
            print("Pareizi!")
            return 1
        else:
            print("Nepareizi!")
            return 0
    else:
        print("Nederīga ievade. Skaitlis jāievada!")
        return 0


def viktorina():
    print("=== Viktorīna: Ko tu zini par Latviju? ===")
    jautajumi = sanemt_jautajumus()
    punkti = 0

    for jaut in jautajumi:
        punkti += uzdot_jautajumu(jaut)

    print(f"\nTavs rezultāts: {punkti} no {len(jautajumi)} punktiem.")
    if punkti == len(jautajumi):
        print("Apsveicu! Tev ir visas pareizās atbildes!")
    elif punkti >= 2:
        print("Labi padarīts!")
    else:
        print("Pamēģini vēlreiz!")


viktorina()

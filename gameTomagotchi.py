def tampilkanStatus(status:dict):
    print(f"Nama: {status['nama']}")
    print(f"Power: {status['power']}")
    print(f"Strength: {status['strength']}")
    print(f"Stamina: {status['stamina']}")

def makan(status:dict):
     status["power"] += 10
     status["strength"] += 50
     status["stamina"] += 50
     print("Monster telah makan. Power, strength, dan stamina bertambah!")
       
def latihan(status:dict):
    status["power"] *= 2
    status["strength"] *= 2
    status["stamina"] -= 20
    print("Monster habis latihan. Power dan strength bertambah, stamina berkurang")
   
def latihanExtra(status:dict):
    status["power"] *= 3
    status["strength"] *= 3
    status["stamina"] += 200
    print("Monster habis latihan. Power, strength dan stamina bertambah")

def bertarung(monster:dict, musuh:dict):
    monster['stamina'] -= 100
    musuh['stamina'] -= 100
        
    totalMonster = monster["power"] + monster["stamina"]
    totalMusuh = musuh["power"] + musuh["stamina"]

    if totalMonster > totalMusuh:
        print("Monster menang!")
    else:
        print("Monster kalah!")
   
statusMonster = {"nama": "bima", "power": 0, "strength": 0, "stamina": 0}
statusMusuh = {"nama": "hatori", "power": 1000, "strength": 10000, "stamina": 2000}

while True:   
    print("""
        1. status monster
        2. makan
        3. latihan
        4. latihan extra
        5. status musuh
        6. bertarung
        """)
    menu = input("Pilih menu: ")

    try:
        if menu == "":
            raise Exception("menu harus dipilih")
        if menu == "1":
            tampilkanStatus(statusMonster)
        elif menu == "2":
            makan(statusMonster)
        elif menu == "3":
            latihan(statusMonster)
        elif menu == "4":
            latihanExtra(statusMonster)
        elif menu == "5":
            tampilkanStatus(statusMusuh)
        elif menu == "6":
            bertarung(statusMonster, statusMusuh)
        else:
            print("Menu tidak tersedia. Silakan pilih menu yang tersedia.")

        main_lagi = input("Apakah Anda ingin main lagi? (y/t): ").lower()
        if main_lagi == "t":
            break

    except Exception as e:
        print(e)

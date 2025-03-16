print("Tere! Olen sinu uus sõber - Python!")

nimi = input("Palun sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")

valik = input(f"{nimi}! Kas leian Sinu keha indeksi? EI või JAH => ")
if valik == "JAH":
    try:
        pikkus = int(input("Palun sisesta oma pikkus sentimeetrites: "))
        if pikkus <= 0:
            raise ValueError("Pikkus peab olema positiivne number!")
        mass = float(input("Palun sisesta oma kehakaal kilogrammides: "))
        if mass <= 0:
            raise ValueError("Mass peab olema positiivne number!")
        kmi = mass / (pikkus / 100) ** 2
        print(f"{nimi}! Sinu keha indeks on: {kmi:.1f}")
        if kmi < 16:
            hinnang = "Tervisele ohtlik alakaal"
        elif 16 <= kmi < 20:
            hinnang = "Alakaal"
        elif 20 <= kmi < 26:
            hinnang = "Normaalkaal"
        elif 26 <= kmi < 31:
            hinnang = "Ülekaal"
        elif 31 <= kmi < 36:
            hinnang = "Rasvumine"
        elif 36 <= kmi < 41:
            hinnang = "Tugev rasvumine"
        else:
            hinnang = "Tervisele ohtlik rasvumine"
        print(hinnang)
    except ValueError as e:
        print(f"Viga: {e}")
else:
    print("Kahju! See on väga kasulik info!")

print(f"Kohtumiseni, {nimi}! sinu, Python!")


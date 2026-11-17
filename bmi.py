def kalkulator():
    try:
        waga = float(input("Waga (kg): "))
        wzrost = float(input("Wzrost (cm): "))
        wiek = int(input("Wiek (lata): "))
    except ValueError:
        print("Błąd: podaj liczbę.")
        return
    
    plec = input("Płeć (k/m): ").lower()

    bmi = waga / ((wzrost / 100) ** 2)
    
    if bmi < 18.5:
        opis = "niedowaga"
    elif bmi < 25:
        opis = "waga prawidłowa"
    elif bmi < 30:
        opis = "nadwaga"
    else:
        opis = "otyłość"

    bmr = 10 * waga + 6.25 * wzrost - 5 * wiek + (5 if plec == "m" else -161)

    print(f"Twoje BMI: {bmi:.1f} ({opis})")
    print(f"Podstawowe zapotrzebowanie (BMR): {bmr:.0f} kcal/dzień")

kalkulator()

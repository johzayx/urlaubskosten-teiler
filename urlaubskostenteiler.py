# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 18:54:33 2025

@author: Clai
"""

# Urlaubskosten-Teiler
# Dieses Programm verteilt die Urlaubsausgaben gerecht auf alle Teilnehmer.


# Teilnehmer eingeben
def teilnehmer_eingeben():
    namen = input("Gib die Teilnehmer des Urlaubs ein (getrennt mit Komma): ").split(
        ","
    )
    return [name.strip() for name in namen]


# Eine Ausgabe erfassen
def ausgabe_erfassen(teilnehmer, ausgaben):
    bezahlt_von = input(f"Wer hat bezahlt? ({', '.join(teilnehmer)}): ").strip()
    if bezahlt_von not in teilnehmer:
        print("Ungültiger Name!")
        return

    try:
        betrag = float(input("Betrag: "))
    except ValueError:
        print("Bitte eine gültige Zahl eingeben!")
        return

    beteiligt = input("Wer war beteiligt? (Namen mit Komma trennen): ").split(",")
    beteiligt = [name.strip() for name in beteiligt if name.strip() in teilnehmer]

    if not beteiligt:
        print("Mindestens eine gültige Person muss beteiligt sein!")
        return

    ausgaben.append(
        {"bezahlt_von": bezahlt_von, "betrag": betrag, "beteiligt": beteiligt}
    )
    print("Ausgabe gespeichert!\n")


# Berechnung der Schulden
def berechnung(teilnehmer, ausgaben):
    saldo={name: 0 for name in teilnehmer} #### spaces removed to check linter

    for ausgabe in ausgaben:
        betrag_pro_person = ausgabe["betrag"] / len(ausgabe["beteiligt"])
        saldo[ausgabe["bezahlt_von"]] += ausgabe["betrag"]
        for person in ausgabe["beteiligt"]:
            saldo[person] -= betrag_pro_person

    return saldo


# Hauptprogramm
def main():
    teilnehmer = teilnehmer_eingeben()
    ausgaben = []

    while True:
        action = input("(N)eue Ausgabe, (B)erechnen oder (Q)uit? ").lower()
        if action == "n":
            ausgabe_erfassen(teilnehmer, ausgaben)
        elif action == "b":
            saldo = berechnung(teilnehmer, ausgaben)
            print("Schulden-Berechnung:")
            for name, betrag in saldo.items():
                print(f"{name}: {betrag:.2f} EUR")
        elif action == "q":
            break
        else:
            print("Ungültige Eingabe!")


if __name__ == "__main__":
    main()

"""
Pokersimulator ( noch nicht fertig)
Kann bisher: Karten erstellen, 5 Karten ziehen, Paar / Drilling / Poker / Flush
erkennen, 100000 Spiele simulieren und Prozentanteile berechnen.
"""
import random

FARBEN = ["Herz", "Karo", "Pik", "Kreuz"]
WERTE = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 11=Bube, 12=Dame, 13=Koenig, 14=Ass
ANZAHL_SPIELE = 100000


def erstelle_kartenspiel():
    kartenspiel = []
    for farbe in FARBEN:
        for wert in WERTE:
            kartenspiel.append((wert, farbe))
    return kartenspiel


def ziehe_hand(kartenspiel):
    return random.sample(kartenspiel, 5)


def zaehle_gleiche(hand):
    anzahl = {}
    for karte in hand:
        wert = karte[0]
        if wert in anzahl:
            anzahl[wert] += 1
        else:
            anzahl[wert] = 1
    haeufigkeiten = list(anzahl.values())
    haeufigkeiten.sort(reverse=True)
    return haeufigkeiten


def ist_paar(hand):
    return zaehle_gleiche(hand) == [2, 1, 1, 1]


def ist_drilling(hand):
    return zaehle_gleiche(hand) == [3, 1, 1]


def ist_poker(hand):
    return zaehle_gleiche(hand) == [4, 1]


def ist_flush(hand):
    erste_farbe = hand[0][1]
    for karte in hand:
        if karte[1] != erste_farbe:
            return False
    return True


# TODO: ist_zwei_paare, ist_full_house, ist_strasse, Straight/Royal Flush

def bewerte_hand(hand):
    if ist_poker(hand):
        return "Poker"
    if ist_flush(hand):
        return "Flush"
    if ist_drilling(hand):
        return "Drilling"
    if ist_paar(hand):
        return "Paar"
    return "Sonstiges"    # enthaelt noch Zwei Paare, Full House, Strasse usw.


def main():
    kartenspiel = erstelle_kartenspiel()
    ergebnis = {"Poker": 0, "Flush": 0, "Drilling": 0, "Paar": 0, "Sonstiges": 0}

    for i in range(ANZAHL_SPIELE):
        hand = ziehe_hand(kartenspiel)
        ergebnis[bewerte_hand(hand)] += 1

    for name in ergebnis:
        prozent = ergebnis[name] / ANZAHL_SPIELE * 100
        print(f"{name:<10}{ergebnis[name]:>8}{prozent:>10.3f} %")

    # TODO: echte Wahrscheinlichkeiten recherchieren und vergleichen


if __name__ == "__main__":
    main()
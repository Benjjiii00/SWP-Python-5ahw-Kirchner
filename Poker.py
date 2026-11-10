import random

Karte = tuple[int, str]    # z.B. (14, "Pik")
Hand = list[Karte]         # 5 Karten

FARBEN = ["Herz", "Karo", "Pik", "Kreuz"]
WERTE = list(range(2, 15))
ANZAHL_SPIELE = 100000

# Echte Wahrscheinlichkeiten
ECHTE_PROZENT = {
    "Royal Flush": 0.000154,
    "Straight Flush": 0.001385,
    "Poker": 0.0240,
    "Full House": 0.1441,
    "Flush": 0.1965,
    "Strasse": 0.3925,
    "Drilling": 2.1128,
    "Zwei Paare": 4.7539,
    "Paar": 42.2569,
    "Hohe Karte": 50.1177,
}


def erstelle_kartenspiel() -> list[Karte]:
    # Erstellt alle 52 Karten (4 Farben x 13 Werte)
    return [(wert, farbe) for farbe in FARBEN for wert in WERTE]


def ziehe_hand(kartenspiel: list[Karte]) -> Hand:
    # Zieht 5 verschiedene Karten zufaellig.
    return random.sample(kartenspiel, 5)



def hole_werte(hand: Hand) -> list[int]:
    #Gibt die Kartenwerte sortiert zurueck, z.B. [3, 5, 5, 9, 14]
    return sorted(karte[0] for karte in hand)


def zaehle_gleiche(hand: Hand) -> list[int]:
    #Zaehlt, wie oft jeder Wert vorkommt (absteigend). Paar: [2, 1, 1, 1]
    anzahl: dict[int, int] = {}
    for wert in hole_werte(hand):
        anzahl[wert] = anzahl.get(wert, 0) + 1   # 0, falls der Wert neu ist
    return sorted(anzahl.values(), reverse=True)



def ist_paar(hand: Hand) -> bool:
    return zaehle_gleiche(hand) == [2, 1, 1, 1]


def ist_zwei_paare(hand: Hand) -> bool:
    return zaehle_gleiche(hand) == [2, 2, 1]


def ist_drilling(hand: Hand) -> bool:
    return zaehle_gleiche(hand) == [3, 1, 1]


def ist_full_house(hand: Hand) -> bool:
    return zaehle_gleiche(hand) == [3, 2]


def ist_poker(hand: Hand) -> bool:
    return zaehle_gleiche(hand) == [4, 1]


def ist_flush(hand: Hand) -> bool:
    farben = {karte[1] for karte in hand}
    return len(farben) == 1


def ist_strasse(hand: Hand) -> bool:
    werte = hole_werte(hand)
    if werte == [2, 3, 4, 5, 14]:
        return True
    return werte == list(range(werte[0], werte[0] + 5))


def ist_royal(hand: Hand) -> bool:
    return hole_werte(hand) == [10, 11, 12, 13, 14]


def bewerte_hand(hand: Hand) -> str:
    if ist_flush(hand) and ist_royal(hand):
        return "Royal Flush"
    if ist_flush(hand) and ist_strasse(hand):
        return "Straight Flush"
    if ist_poker(hand):
        return "Poker"
    if ist_full_house(hand):
        return "Full House"
    if ist_flush(hand):
        return "Flush"
    if ist_strasse(hand):
        return "Strasse"
    if ist_drilling(hand):
        return "Drilling"
    if ist_zwei_paare(hand):
        return "Zwei Paare"
    if ist_paar(hand):
        return "Paar"
    return "Hohe Karte"




def simuliere(anzahl_spiele: int) -> dict[str, int]:
    kartenspiel = erstelle_kartenspiel()
    ergebnis = {name: 0 for name in ECHTE_PROZENT}
    for _ in range(anzahl_spiele):
        name = bewerte_hand(ziehe_hand(kartenspiel))
        ergebnis[name] += 1
    return ergebnis


def berechne_prozent(anzahl: int, gesamt: int) -> float:
    return anzahl / gesamt * 100


def zeige_ergebnis(ergebnis: dict[str, int], gesamt: int) -> None:
    print(f"{'Kombination':<16}{'Anzahl':>8}{'Simuliert %':>14}{'Echt %':>10}")
    for name, anzahl in ergebnis.items():
        prozent = berechne_prozent(anzahl, gesamt)
        print(f"{name:<16}{anzahl:>8}{prozent:>14.4f}{ECHTE_PROZENT[name]:>10.4f}")


def main() -> None:
    ergebnis = simuliere(ANZAHL_SPIELE)
    zeige_ergebnis(ergebnis, ANZAHL_SPIELE)


if __name__ == "__main__":
    main()

from collections import Counter
import random

def lottoziehung(anzahlZahlen=6, max_zahl=45):
    pool = list(range(1, max_zahl + 1))
    gezogeneZahlen = []

    for i in range(anzahlZahlen):
        index = random.randrange(len(pool))
        zahl = pool.pop(index)
        gezogeneZahlen.append(zahl)

    return gezogeneZahlen

def lotto_statistik(anzahlZiehungen, anzahlZahlen=6, maxZahl=45):
    statistik = Counter()

    for i in range(anzahlZiehungen):
        statistik.update(lottoziehung(anzahlZahlen, maxZahl))

    return statistik

print("Eine Ziehung:", lottoziehung())

for anzahl in [1000, 10_000, 100_000]:
    print(f"\n=== Statistik nach {anzahl:,} Ziehungen ===")
    ergebnis = lotto_statistik(anzahl)

    for zahl in range(1, 11):
        print(f"Zahl {zahl:2d}: {ergebnis[zahl]} mal gezogen")
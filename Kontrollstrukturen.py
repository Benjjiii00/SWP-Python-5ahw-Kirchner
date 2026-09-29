# Python Kontrollstrukturen - Überblick mit je einem Beispiel

# 1. if / elif / else  (Verzweigung)
# Das Programm entscheidet anhand einer Bedingung, welcher Block ausgeführt wird.

punkte = 75

if punkte >= 90:
    print("Sehr gut")
elif punkte >= 75:
    print("Gut")
elif punkte >= 50:
    print("Genügend")
else:
    print("Nicht genügend")


# 2. for-Schleife  (Wiederholung mit bekannter Anzahl)
# Geht eine Folge (z.B. Liste oder range) Element für Element durch.

fruechte = ["Apfel", "Birne", "Banane"]

for frucht in fruechte:
    print("Ich mag", frucht)

# range(1, 6) erzeugt die Zahlen 1, 2, 3, 4, 5 (die 6 ist nicht mehr dabei)
for zahl in range(1, 6):
    print("Zahl:", zahl)


# 3. while-Schleife  (Wiederholung, solange eine Bedingung stimmt)

zaehler = 3

while zaehler > 0:
    print("Countdown:", zaehler)
    zaehler = zaehler - 1   # ohne diese Zeile würde die Schleife nie enden!

print("Start!")


# 4. break  (Schleife sofort verlassen)

for zahl in range(1, 10):
    if zahl == 4:
        print("4 gefunden, ich höre auf!")
        break               # Schleife wird hier komplett beendet
    print("Zahl:", zahl)


# 6. pass  (Platzhalter, tut nichts)
# Python erlaubt keine leeren Blöcke. Mit pass kann man einen Block
# "vorläufig leer" lassen, z.B. wenn man den Code später schreiben will.

alter = 20

if alter >= 18:
    pass                    # TODO: hier kommt später noch etwas hin
else:
    print("Zugang verweigert")

print("pass hat nichts gemacht, das Programm läuft trotzdem weiter.")


# 7. try / except / else / finally  (Fehlerbehandlung)
# Ohne try/except würde das Programm bei einem Fehler abstürzen.
print("\n--- 7. try / except ---")

eingabe = "abc"             # Das ist keine Zahl -> das gibt einen Fehler

try:
    zahl = int(eingabe)     # Hier kann ein Fehler passieren
    print("Die Zahl ist", zahl)
except ValueError:
    print("Fehler: Das war keine gültige Zahl!")
else:
    print("Alles ok, es gab keinen Fehler.")   # nur wenn KEIN Fehler auftrat
finally:
    print("Ich werde immer ausgeführt (mit oder ohne Fehler).")

# Noch ein Beispiel: Division durch 0
try:
    ergebnis = 10 / 0
except ZeroDivisionError:
    print("Fehler: Durch 0 darf man nicht teilen!")
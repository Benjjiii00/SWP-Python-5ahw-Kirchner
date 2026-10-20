
# HU: Comprehensions mit if/else

zahlen = [4, 7, 10, 13, 16, 19, 22]

# 1) List Comprehension mit if/else
# Gerade Zahlen verdoppeln, ungerade Zahlen mit 3 multiplizieren
liste = [zahl * 2 if zahl % 2 == 0 else zahl * 3 for zahl in zahlen]
print("List:", liste)

# 2) Set Comprehension mit if/else
# Gerade Zahlen -> "gerade", ungerade Zahlen -> "ungerade"
mengen = {"gerade" if zahl % 2 == 0 else "ungerade" for zahl in zahlen}
print("Set:", mengen)

# 3) Dict Comprehension mit if/else
# Zahl als Key, Wert abhängig davon, ob sie gerade oder ungerade ist
dictionary = {zahl: "gerade" if zahl % 2 == 0 else "ungerade" for zahl in zahlen}
print("Dict:", dictionary)

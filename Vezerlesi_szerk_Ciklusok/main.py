# Iteráció (ciklus)
# Olyan vezérlési szerkezet, melyet utasítások ismétlésére használunk
# Ciklusok fajtái:
# - klasszikus növekményes ciklus (for, NINCS a Python-ban)
# - for-in ciklus (speciális ciklus a Python-ban, foreach ciklushoz hasonlít leginkább)
# - elöltesztelő ciklus (while)
# - hátultesztelő ciklus (NINCS a Python-ban)
import random

# Klasszikus növekményes ciklus megvalósítása for-in ciklussal:
for i in range(8):
    print(i, end=' ')
print()
for i in range(-5, 5):
    print(i, end=' ')
print()
for i in range(1, 11, 2):
    print(i, end=' ')
print()
t = ['alma', 'körte', 'szilva']
for i in range(len(t)):
    print(f't[{i}]={t[i]}', end=' ')
print()

# Elöltesztelő ciklus példa: lottószámok generálása
lotto90 = set()
while len(lotto90) < 5:
    lotto90.add(random.randint(1, 90))  # 1 >= vélszám <= 90
print(lotto90)
# Halmaz elemei növekvő sorrendben:
lotto90rendezve = []
for i in range(1, 90):
    if i in lotto90:
        lotto90rendezve.append(i)
print(lotto90rendezve)

import random
import re
class q:
  def __init__(self, voltant, mina, mostrat):
    self.voltant = voltant
    self.mina = mina
    self.mostrat = mostrat
# Escollim la dificultat, que de moment no és necessari
# d = input("Dificultat (f)àcil, (m)itjana o (d)ifícil")
d = "f"
if d == "f":
    total = 25
    mines = 5
elif d == "m":
    total = 64
    mines = 8
else:
    total = 100
    mines = 20
# Afegim mines i espais buits
llista = []
for i in range(total - mines):
    a = q(0, "o", False)
    llista.append(a)
for j in range(mines):
    a = q(0, "x", False)
    llista.append(a)
random.shuffle(llista) # Desordenem la llista

matriu = []
comptador = 0
for i in range(5):
  matriu.append([])
  for j in range(5):
    matriu[i].append(llista[comptador])
    comptador += 1
nums = "[0123456789]"
for i in range(5):
  for j in range(5):
    if matriu[i][j].mina == "x":
      if i == 0 and j == 0:
        matriu[i][j+1].voltant += 1
        matriu[i+1][j].voltant += 1
        matriu[i+1][j+1].voltant += 1
      elif i == 0 and j == 4:
        matriu[i][j-1].voltant += 1
        matriu[i+1][j-1].voltant += 1
        matriu[i+1][j].voltant += 1
      elif i == 4 and j == 0:
        matriu[i-1][j].voltant += 1
        matriu[i-1][j+1].voltant += 1
        matriu[i][j+1].voltant += 1
      elif i == 4 and j == 4:
        matriu[i-1][j-1].voltant += 1
        matriu[i-1][j].voltant += 1
        matriu[i][j-1].voltant += 1
      elif i == 0 and j > 0:
        matriu[i][j-1].voltant += 1
        matriu[i][j+1].voltant += 1
        matriu[i+1][j-1].voltant += 1
        matriu[i+1][j].voltant += 1
        matriu[i+1][j+1].voltant += 1
      elif i > 0 and j == 0:
        matriu[i-1][j].voltant += 1
        matriu[i-1][j+1].voltant += 1
        matriu[i][j+1].voltant += 1
        matriu[i+1][j].voltant += 1
        matriu[i+1][j+1].voltant += 1
      elif i > 0 and j == 4:
        matriu[i-1][j-1].voltant += 1
        matriu[i-1][j].voltant += 1
        matriu[i][j-1].voltant += 1
        matriu[i+1][j-1].voltant += 1
        matriu[i+1][j].voltant += 1
      elif i == 4 and j > 0:
        matriu[i-1][j-1].voltant += 1
        matriu[i-1][j].voltant += 1
        matriu[i-1][j+1].voltant += 1
        matriu[i][j-1].voltant += 1
        matriu[i][j+1].voltant += 1
      else:
        matriu[i-1][j-1].voltant += 1
        matriu[i-1][j].voltant += 1
        matriu[i-1][j+1].voltant += 1
        matriu[i][j-1].voltant += 1
        matriu[i][j+1].voltant += 1
        matriu[i+1][j-1].voltant += 1
        matriu[i+1][j].voltant += 1
        matriu[i+1][j+1].voltant += 1

for i in range(5): # Amb això es mostra el taulell sencer
  linia = ""
  for j in range(5):
    if matriu[i][j].mina == "x":
      linia += str(matriu[i][j].mina)
    elif matriu[i][j].voltant == 0:
      linia += "·"
    else:
      linia += str(matriu[i][j].voltant)
  print(linia)

# █

tir = ""
while tir != "exit":
  print("  12345\n")
  for i in range(5): # Mostrem taulell amagat
    linia = chr(97 + i) + " "
    for j in range(5):
      if matriu[i][j].mostrat == False:
        linia += "█"
      elif matriu[i][j].mostrat == True and matriu[i][j].mina == "x":
        linia += str(matriu[i][j].mina)
      else:
        linia += str(matriu[i][j].voltant)
    print(linia)
  tir = input("Fila i columna (a1): ").lower()
  fila = ord(tir[0]) - 97
  colu = int(tir[1]) - 1
  if matriu[fila][colu].mina == "x":
    tir = "exit"
    for i in range(5): # Amb això es mostra el taulell sencer
      linia = ""
      for j in range(5):
        if matriu[i][j].mina == "x":
          linia += str(matriu[i][j].mina)
        elif matriu[i][j].voltant == 0:
          linia += "·"
        else:
          linia += str(matriu[i][j].voltant)
      print(linia)
    print("Has perdut! =(")
  else:
    matriu[fila][colu].mostrat = True

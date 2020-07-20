import random
import re
import bm_classes

# Funcions

def mostrarMenu():
  '''
  Mostra el menú principal
  '''
  print("1. Començar el joc")
  print("2. Dificultat")
  print("3. Idioma (properament)")
  print("4. Sortir")

def escollirOpcio(n:int)->int:
    '''Escollim l'opció del menú, ha de retornar un número entre 1 i n
    ha de ser enter
    :param n: Valor entre 1 i n que representa l'opció escollida del menú.
    :return: Retorna el valor n introduït.
    '''
    while True:
        try:
            o = int(input("Opció: "))
            if (1<= o <=n):
                break
            else:
                raise ValueError('Ha d''estar entre 1 i 2')
        except:
            print("Error")
    return o

def escollirDificultat():
  '''
  Aquí escollim el nivell de dificultat del joc (fàcil, mitjà o difícil)
  '''
  facil = bm_classes.dif(25, 5, 5)
  mitja = bm_classes.dif(49, 10, 7)
  dificil = bm_classes.dif(81, 20, 9)
  print("Quin nivell vols? (f)àcil, (m)itjà o (d)ifícil")
  d = input()
  if d == "d":
    return dificil
  elif d == "m":
    return mitja
  else:
    return facil

def iniciJoc(dificultat):
  '''
  Funció que inicia el joc amb la variable donada del nivell de dificultat.
  '''
  total = dificultat.total
  mines = dificultat.mines
  cols = dificultat.cols
  # Afegim mines i espais buits
  llista = []
  for i in range(total - mines):
      a = bm_classes.q(0, "o", False)
      llista.append(a)
  for j in range(mines):
      a = bm_classes.q(0, "x", False)
      llista.append(a)
  random.shuffle(llista) # Desordenem la llista

  matriu = []
  comptador = 0
  for i in range(cols):
    matriu.append([])
    for j in range(cols):
      matriu[i].append(llista[comptador])
      comptador += 1
  # nums = "[0123456789]"
  cols1 = cols -1
  for i in range(cols): # Si hi ha mina, sumem 1 a les caselles del voltant
    for j in range(cols):
      if matriu[i][j].mina == "x":
        if i == 0 and j == 0:
          matriu[i][j+1].voltant += 1
          matriu[i+1][j].voltant += 1
          matriu[i+1][j+1].voltant += 1
        elif i == 0 and j == cols1:
          matriu[i][j-1].voltant += 1
          matriu[i+1][j-1].voltant += 1
          matriu[i+1][j].voltant += 1
        elif i == cols1 and j == 0:
          matriu[i-1][j].voltant += 1
          matriu[i-1][j+1].voltant += 1
          matriu[i][j+1].voltant += 1
        elif i == cols1 and j == cols1:
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
        elif i > 0 and j == cols1:
          matriu[i-1][j-1].voltant += 1
          matriu[i-1][j].voltant += 1
          matriu[i][j-1].voltant += 1
          matriu[i+1][j-1].voltant += 1
          matriu[i+1][j].voltant += 1
        elif i == cols1 and j > 0:
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

  '''
  for i in range(cols): # Amb això es mostra el taulell sencer per proves
    linia = ""
    for j in range(cols):
      if matriu[i][j].mina == "x":
        linia += str(matriu[i][j].mina)
      elif matriu[i][j].voltant == 0:
        linia += "·"
      else:
        linia += str(matriu[i][j].voltant)
    print(linia)'''


  # █

  tir = ""

  while tir != "exit":
    # Bucle que mostra número de columna
    columnes = "  "
    for i in range(cols):
      columnes += str(i + 1)
    print(columnes)

    # Mostrem el taulell
    for i in range(cols): 
      linia = chr(97 + i) + " "
      for j in range(cols):
        if matriu[i][j].mostrat == False:
          linia += "█"
        elif matriu[i][j].mostrat == True and matriu[i][j].mina == "x":
          linia += str(matriu[i][j].mina)
        elif matriu[i][j].mostrat == True and matriu[i][j].voltant == 0:
          linia += "·"
        else:
          linia += str(matriu[i][j].voltant)
      print(linia)

    tir = input("Fila i columna (a1): ").lower()
    try:
      fila = ord(tir[0]) - 97
      colu = int(tir[1]) - 1
    except:
      break
    if tir == "exit":
      tir = "exit"
      print("Menú")
    elif matriu[fila][colu].mina == "x":
      for i in range(cols): # Amb això es mostra el taulell sencer quan perds
        linia = ""
        for j in range(cols):
          if matriu[i][j].mina == "x":
            linia += str(matriu[i][j].mina)
          elif matriu[i][j].voltant == 0:
            linia += "·"
          else:
            linia += str(matriu[i][j].voltant)
        print(linia)
      print("Has perdut! =(")
      break
    else:
      matriu[fila][colu].mostrat = True

def sortir():
  '''
  Funció per sortir del programa.
  '''
  print("Arreveure!")
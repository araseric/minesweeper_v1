import bm_modules
import bm_classes

# Dificultat per defecte (fàcil)
dificultat = bm_classes.dif(25, 5, 5)

# Base del programa
while True:
  bm_modules.mostrarMenu()
  opcio = bm_modules.escollirOpcio(4)
  if opcio == 1: # Començar el joc
    bm_modules.iniciJoc(dificultat)
  elif opcio == 2: # Dificultat
    dificultat = bm_modules.escollirDificultat()
  elif opcio == 3: # Idioma
    break
  elif opcio == 4: # Sortir
    bm_modules.sortir()
    break

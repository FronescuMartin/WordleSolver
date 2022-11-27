import wordle_func
import random

cuvinte = open("Cuvinte.in")
cuvLista = cuvinte.readlines()
cuvGhicit = random.choice(cuvLista)
cuvinte.close()
rez = open("rezultate.out", "w")
rez.truncate(0)
rez.close()
nrGuess = open("numarguessuri.out", "w")
nrGuess.truncate(0)
nrGuess.close()

if cuvGhicit != "ZVONI":
    rezStr = cuvGhicit[:-1]
else:
    rezStr = cuvGhicit

rezStr += ", "
rez = open("rezultate.out", "w")
rezStr += wordle_func.func_wordle(cuvGhicit)
rezStr = rezStr[:-3]
rez.write(rezStr)
rez.close()

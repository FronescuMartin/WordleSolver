import wordle_func

rez = open("rezultate.out", "w")
rez.truncate(0)
rez.close()
nrGuess = open("numarguessuri.out", "w")
nrGuess.truncate(0)
nrGuess.close()

rezStr = ""

cuvinte = open("cuvinte_mic.in")
cuvLista = cuvinte.readlines()

for i in range(len(cuvLista)):
    rez = open("rezultate.out", "a")
    #rez.write(cuvLista[i])
    #rez.close()
    if i != len(cuvLista) -1:
        rezStr += cuvLista[i][:-1] + ", "
    else:
        rezStr += cuvLista[i] + ", "
    rezStr += wordle_func.func_wordle(cuvLista[i])
    if i != len(cuvLista) - 1:
        rezStr = rezStr[:-3]
        rezStr += "\n"
    rez.write(rezStr)
    rezStr = ""
    rez.close()
'''
print(rezStr)
rez = open("rezultate.out", "w")
rez.write(rezStr)
'''
import time
import pygame
import os
from pygame.locals import *

def func_wordle(CuvantDeGhicit):
    #rezultat_cuv = open("rezultate.out", "a")
    #print(CuvantDeGhicit.rstrip(), file=rezultat_cuv)
    #rezultat_cuv.close()
    ##rezultat_cuv = open("rezultate.out", "a")
    #rezultat_cuv.write(", ")
    pygame.font.init()
    pygame.font.get_init()

    os.startfile("a.exe")
    
    class Square(pygame.sprite.Sprite):
        def __init__(self, color):
            super(Square, self).__init__()
            self.surf = pygame.Surface((100, 100))
            self.surf.fill(color)
            self.rect = self.surf.get_rect()

    rect_update = pygame.Rect(0, 0, 500, 100)
    font1 = pygame.font.SysFont('timesnewroman.ttf', 170)
    text = [font1.render(str(i), True, (0, 0, 0)) for i in range(5)]

    pygame.init()
    screen = pygame.display.set_mode((800,800))#, pygame.RESIZABLE)
    square = [Square((128, 128, 128)) for i in range(5)]

    '''
    guess = open("guess.txt", "w")
    guess.truncate(0)
    guess.close()
    '''

    nr_guesses = 0
    #nr_text = font1.render(str(nr_guesses), True, (0, 0, 0))


    #cuvinte = open("cuvinte.in")
    #cuvLista = cuvinte.readlines()
    #guess = open("guess.txt")
    #cuv_guess = guess.readlines()
    #feedback_in = open("feedback.txt")
    #fin = feedback_in.readline()
    rezultate_str = ""
    Rezultat = [0 for i in range(5)]
    #CuvantDeGhicit = random.choice(cuvLista)
    CuvantIntrodus = "xxxxx"
    #CuvantDeGhicit = "TARTA"
    #print("Introduceti un cuvant de 5 litere din limba romana: ")
    #print("ATENTIE! Cuvintele introduse trebuie scrise cu majuscule si fara diacritice! ")
    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
        guesses_in = open("guesses.txt", "r")
        gin = guesses_in.readlines()
        while True:
            if len(gin) != 0:
                break
            guesses_in.close()
            guesses_in = open("guesses.txt", "r")
            gin = guesses_in.readlines()
            time.sleep(2.44)
        if CuvantIntrodus != gin[0]:
            nr_guesses += 1
            ##rezultat_cuv.write(gin[0])
            rezultate_str += gin[0]
            if gin[0] != CuvantDeGhicit:
                ##rezultat_cuv.write(", ")
                rezultate_str += ", "
            #print(rezultate_str)
        CuvantIntrodus = gin[0]
        #print(gin)
        #guesses_in.truncate(0)
        guesses_in.close()
        feedback = open("feedback.txt", "w", encoding = "utf-8")
        #print(CuvantIntrodus)
        for j in range(5):
            if CuvantIntrodus[j] == CuvantDeGhicit[j]:
                Rezultat[j] = '\U0001F7E9'
                square[j] = Square((0, 255, 0))
            elif CuvantIntrodus[j] in CuvantDeGhicit:
                Rezultat[j] = '\U0001F7E8'
                square[j] = Square((255, 255, 0))
            else:
                Rezultat[j] = '\U0001F7E5'
                square[j] = Square((128, 128, 128))
        rez_nr = [k for k in range(5)]
        for k in range(5):
            if Rezultat[k] == '\U0001F7E9':
                rez_nr[k] = '2'
            elif Rezultat[k] == '\U0001F7E8':
                rez_nr[k] = '1'
            elif Rezultat[k] == '\U0001F7E5':
                rez_nr[k] = '0'
        if '\U0001F7E8' not in Rezultat and '\U0001F7E5' not in Rezultat:
            Rezultat = ['\U0001F7E9' for j in range(5)]
            square = [Square((0, 255, 0)) for j in range(5)]
            for j in range(5):
                text[j] = font1.render(str(CuvantIntrodus[j]), True, (0, 0, 0))
                screen.blit(square[j].surf, (150+j*100, 100*nr_guesses))
                screen.blit(text[j], (150+j*100, 100*nr_guesses, 100, 100))
            pygame.display.flip()
            #print('Felicitari! Ati ghicit cuvantul!')
            feedback.truncate(0)
            feedback.close()
            #print(nr_guesses)
            time.sleep(5)
            pygame.quit()
            ##rezultat_cuv.write("\n")
            rezultate_str += "\n"
            numarGuess = open("numarguessuri.out", "a")
            numarGuess.write(str(nr_guesses)+"\n")
            #numarGuess.write("\n")
            numarGuess.close()
            ##rezultat_cuv.close()
            return rezultate_str
        scr_rez = "".join(Rezultat)
        #print(scr_rez)
        feedback.write(" ".join(rez_nr))
        feedback.close()
        time.sleep(1)
        feedback = open("feedback.txt", "w", encoding = "utf-8")
        feedback.truncate(0)
        feedback.close()
        #feedback.truncate(0)
        for j in range(5):
            text[j] = font1.render(str(CuvantIntrodus[j]), True, (0, 0, 0))
            screen.blit(square[j].surf, (150+j*100, 100*nr_guesses))
            screen.blit(text[j], (150+j*100, 100*nr_guesses, 100, 100))
        #nr_text = font1.render(str(nr_guesses), True, (0, 0, 0))
        #screen.blit(nr_text, (0, 0, 0, 0))
        pygame.display.flip()
        #time.sleep(5)

    '''
    if CuvantIntrodus not in cuvinte.Cuvinte:
        while CuvantIntrodus not in cuvinte.Cuvinte:
            CuvantIntrodus = input("CUVANT INVALID! Introduceti alt cuvant: ")


    if CuvantIntrodus == CuvantDeGhicit:
            Rezultat = ['\U0001F7E9' for i in range(5)]
            print("".join(Rezultat))
            print('Felicitari! Ati ghicit cuvantul!')


    while CuvantIntrodus != CuvantDeGhicit:
        for i in range(5):
            if CuvantIntrodus[i] == CuvantDeGhicit[i]:
                Rezultat[i] = '\U0001F7E9'
            elif (CuvantIntrodus[i] in CuvantDeGhicit):
                Rezultat[i] = '\U0001F7E8'
            else:
                Rezultat[i] = '\U0001F7E5'
        print("".join(Rezultat))

        CuvantIntrodus = input("Introduceti un alt cuvant: ")
        if CuvantIntrodus not in cuvinte.Cuvinte:
            while CuvantIntrodus not in cuvinte.Cuvinte:
                CuvantIntrodus = input("CUVANT INVALID! Introduceti alt cuvant: ")


        if CuvantIntrodus == CuvantDeGhicit:
            Rezultat = ['\U0001F7E9' for i in range(5)]
            print("".join(Rezultat))
            print('Felicitari! Ati ghicit cuvantul!')
            break
    '''
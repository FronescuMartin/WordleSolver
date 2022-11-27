# Wordle Solver

## Informatii generale:

Programul face in medie **4.146** incercari pentru a ghici un cuvant.  
In solutii.txt se gaseste lista de incercari pentru fiecare cuvant din dictionar.  
Cel mai bun cuvant de inceput (opener) este **TAREI**.  
De asemenea am inclus in fisierul Entropie.out lista cu toate cuvintele si entropia fiecaruia.  

### Requirements:

Sistem de operare Windows (utilizeaza batch file-uri si executabile compilate pentru Windows)  
Python si pip instalate, pygame 2.1.2

Observatie:
Daca pygame nu poate fi instalat din terminal (cu comanda **pip install pygame**) il puteti instala folosind fisierul .whl (pentru Python 3.10!) (executand direct fisierul sau alternativ ruland comanda **py -3.10 -m pip install pygame-2.1.2-cp310-cp310-win_amd64.whl**).

### Pornire:

Sunt doua versiuni ale programului: 
* versiunea normala (alege un cuvant random din **Cuvinte.in** pe care joaca optim Wordle; poate fi rulata cu **solver_normal.bat**)
* versiunea bulk (ghiceste mai multe cuvinte unul dupa altul, citite din fisierul **cuvinte_mic.in**; poate fi rulata cu **solver_bulk.bat**).  
In fisierul **cuvinte_mic.in**, cuvintele trebuie sa fie scrise pe randuri diferite.
In **rezultate.out** sunt scrise incercarile pentru fiecare cuvant din cuvinte_mic.in.  
In fisierul **runtime.out** este scris timpul de executie pentru ultimul cuvant ghicit.

## Interfata grafica:

Partea de GUI este facuta in Python, utilizand modulul **pygame**. Pygame deschide o fereastra care arata utilizatorului corectitudinea fiecarui guess generat (ca si jocul original Wordle) pentru cuvantul de ghicit respectiv. 
O fereastra generata de pygame se aseamana cu un canvas, in sensul ca foloseste mai multe functii (cum ar fi blit()) pentru a determina ce “deseneaza” pe window si unde, dar si pentru a actualiza fereastra (functia pygame.display.flip()). Window-ul este actualizat de fiecare data cand programul primeste un guess nou de la guesser-ul **a.exe** (scris in C++).

## Documentatie pentru Algoritmul de guessing:

I. Pentru ca guesser-ul sa aleaga un cuvant potrivit , trebuie sa calculeze care dintre cuvinte imi ofera cea mai mare informatie.
Aceste cuvinte in program sa afle in vectorul(words)
II. Informatia este calculata in functie de probabilitatea oferita de diferite cazuri de feedback. Probabilitatea este calculata cu formula:
cazuri favorabile / cazuri posibile , cazurile favorabile reprezentand lista de cuvinte care mi-ar oferi genul ala de feedback pentru
cuvantul ales din words, iar cazurile posibile fiind lista de cuvinte posibil alese de wordle (se afla in words_posibil din program).
III. feedback-ul este reprezentat de produsul cartezian a multimi {0,1,2} de 5 ori . Aceste valori sunt stocate intr-un vectori de map-uri 
prodCart[5]. Fiecare element al acestui vector reprezinte o pozitie in cuvant (adica prodCart[0] este prima litera dintr-un cuvant de 
5 litere).Restrictiile acestui feedback sunt reprezentate de valorile: 
* 0-litera nu se afla in cuvant  
* 1-litera se afla undeva in cuvant
* 2-litera se afla pozitia asta in cuvant
Un exemplu : prodCart[k]['A']=2 ne spune ca pe pozitia k in cuvant se afla litera A
prodCart[k]['B']=1 ne spune ca B se afla undeva in cuvant
prodCart[k]['C']=0 ne spune ca C nu se afla in cuvant

IV. Cu mai multe for-uri sunt generate astfel de cazuri de feedback posibil si pentru fiecare dintre ele este calculata informatia care 
urmeaza sa fie adaugata la formula de entropie.(formula de entropie este: $$\sum \left( probabilitate* log2 \left(1 \over probabilitate \right) \right)$$
V. Aceasta entropie este calculate pentru fiecare cuvant si este stocata in map-ul entropieCuvant.
VI. Entropiile sunt comparate iar guesser-ul transmite cuvantul cu entropia cea mai mare urmand sa astepte feedback de la wordle.
VII. Dupa ce primeste feedback acesta sterge din lista words_posibil cuvintele care nu respecta feedback-ul si urmeaza sa calculeze 
urmatorul cuvant care are cea mai mare entropie.
**Observatie!** Cuvintele din vector-ul words nu sunt niciodata modificate deoarce este posibil ca un cuvant care este determinat ca fiind 
imposibil sa ofere mai multa informatie decat un cuvant posibil.
VIII. Guesser se opreste in momentul in care vectorul words_posibil are un singur element(cuvantul ales de wordle).

Pentru a optimiza timpul de executie, am precalculat entropia tuturor cuvintelor (utilizand acelasi algoritm), pentru a gasi opener-ul optim. Acesta este TAREI. 

## Comunicare fisiere:

Fisierul **solver_normal.bat** va rula programul Python **wordle_single.py**, iar **solver_bulk.bat** va rula programul Python **wordle_bulk.py**, care pentru fiecare cuvant ruleaza **wordle_func.py** si **a.exe**. Dupa ghicirea fiecarui cuvant se repornesc programele mentionate anterior.
Dupa ce genereaza fiecare guess (scriindu-l in **Guesses.txt**), programul guesser **a.exe** (scris in C++, cod sursa in **main.cpp**) asteapta sa primeasca feedback (scris in **Feedback.txt**). Intre timp, programul de feedback/jocul de wordle (scris in Python) genereaza feedback-ul guess-ului curent, iar dupa aceea asteapta sa primeasca urmatorul guess. Pentru a nu exista coliziuni, fiecare program goleste fisierele in care scrie in momentul in care se asigura ca celalalt a primit informatiile necesare.

## Referinte
* https://www.pygame.org/docs/
* https://www.youtube.com/watch?v=v68zYyaEmEA
* https://en.cppreference.com/w/
* https://docs.python.org/3/reference/
* https://dr0id.bitbucket.io/legacy/pygame_tutorials.html

## Realizat de
Dan Alexandru, Fronescu Martin-Cristian, Velișan George-Daniel, Vizinteanu Teodora

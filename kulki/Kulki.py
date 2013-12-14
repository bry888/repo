import pygame, sys, os

if 'unix' in os.environ['DBUS_STARTER_ADDRESS']:
    # UBUNTU ENVIRONMENT
    os.environ['SDL_VIDEODRIVER']='x11'
else:
    try:
        # WINDOWS ENVIRONMENT
        os.environ['SDL_VIDEODRIVER']='windib'
    except:
        raise NameError('bad luck you dont have windows or unix!')


from pygame.locals import*
from sys import exit
import random
import time

pygame.init()

def NICK():
    def get_key():
        while 1:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key
            else:
                pass

    surface = pygame.display.set_mode((500, 200))
    pygame.display.set_caption('Kulki') #etykieta
    okno = pygame.display.get_surface()
    tlo = pygame.image.load('nick.png')
    okno.blit(tlo, (0,0))        

    font = pygame.font.SysFont("comicsansms", 25, True, False) #bold, ital
    text = font.render('Twoj nick: (litery od A do Z)', True,(0,0,0))#col, (background
    okno.blit(text, (50,30))
    pygame.display.flip()

    nazwa = []

    while True:
        inkey = get_key()
        
        if 97 <=inkey <= 122:
            nazwa.append(chr(inkey))
        elif inkey == K_RETURN:
            pygame.quit()
            break
        
        
        okno.blit(text, (50,30))
        okno.blit(font.render(''.join(nazwa).upper(), True,(0,0,0)), (50,100))
        pygame.display.flip()

    return nazwa


def sortBy(lista1, lista2):
    '''sortuje lista1 i lista 2 wzgledem lista1'''
    points = zip(lista1, lista2)   
    sorted_points = sorted(points)
    return [point[0] for point in sorted_points], [point[1] for point in sorted_points]


class NajlepszeWyniki(object):
    def __init__(self):
        self.surface = pygame.display.set_mode((400,500))
        pygame.display.set_caption('Najlepsze Wyniki') #etykieta
        self.okno = pygame.display.get_surface()
        self.tlo = pygame.image.load('wyniki.png')
        self.okno.blit(self.tlo, (0,0))
        self.nscores = 10
        
    def zapisz(self, punkty, nazwa):
        pygame.font.init()
        text_file = open("wynik.txt", "r") #read
        score = []
        names = []
        for line in text_file:
            ls = line.strip().split("\t")
            score.append(int(ls[1]))
            names.append(ls[0])
            
        score.append(punkty)
        names.append(nazwa)
        scoreSorted, namesSorted = sortBy(score, names) 
        scoreSorted.reverse()
        namesSorted.reverse()
        text_file.close()
        
        text_file = open("wynik.txt", "w")
        for i in range(min(self.nscores, len(score))):
            text_file.write(namesSorted[i]+"\t"+str(scoreSorted[i])+"\n")
        text_file.close()
        pygame.font.quit()
        
    def czytaj(self):
        pygame.font.init()
        ile = 0
        text_file = open("wynik.txt", "r") #read
        for line in text_file:
            linia = line.strip().split()
            font = pygame.font.SysFont("comicsansms", 25, True, False) #bold, ital
            text = font.render(str(linia[0]).upper()+': '+str(linia[1]), True,(0,0,0))#col, (background
            self.okno.blit(text, (50,25+ile))
            ile += 45
        text_file.close()
        pygame.font.quit()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
barwa = ['zielona.png', 'rozowa.png', 'niebieska.png', 'zolta.png', 'czerwona.png', 'pomaranczowa.png', 'biala.png']

def LosKolor():
    return random.choice(barwa)

def ListaMiejsc(plansza):
    lista = []
    for i in range(len(plansza)):
        if plansza.values()[i] == 'nic':
            lista.append(plansza.keys()[i])
    return lista
  
def nowaKulka(plansza, miejsca, punkty, kolor_kulki):
    kulka = pygame.image.load(kolor_kulki).convert()

    if len(miejsca) == 0:
        global gamestate
        gamestate = 0
        return 0
    else:
        gdzie = random.choice(miejsca)
        screen.blit(kulka, (gdzie[0]*60+1, gdzie[1]*60+1))
        plansza[(gdzie[0],gdzie[1])] = kolor_kulki

        #czy cos nie znika samo
        listaKul = CzyKasuj(gdzie[0],gdzie[1],plansza) 
        Kasuj5(listaKul)
        return len(listaKul)
        
    pygame.display.flip()

def TrzyNowe():
    Nowe = []
    Nowe.append(LosKolor())
    Nowe.append(LosKolor())
    Nowe.append(LosKolor())
    return Nowe

def WyswietlNext(cos):
    x=0
    for i in cos:
        kul = pygame.image.load(i).convert()
        screen.blit(kul, (630,250+x))
        x += 60
        
def Podswietl(x,y):
    podsw = pygame.image.load('podswietl.png')
    screen.blit(podsw, (x*60+1, y*60+1))

def Zgas(x,y):
    zga = pygame.image.load('zgas.png')
    screen.blit(zga, (x*60+1, y*60+1))

def PustePole(x,y):
    puste = pygame.image.load('pusta.png').convert()
    screen.blit(puste, (x*60+1, y*60+1))

def PrzeniesKulke(x,y, a,b, kulka):
    kul = pygame.image.load(kulka)
    screen.blit(kul, (a*60+1, b*60+1))
    PustePole(x,y)

def Kasuj5(SET):#,plansza???
    puste = pygame.image.load('pusta.png')
    for i in SET: # w secie tuple x,y
        screen.blit(puste, (i[0]*60+1, i[1]*60+1))
        plansza[i] = 'nic'

def CzyKasuj(X,Y, plansza):
    skos1 = piecWrzedzieSkos1(X,Y,plansza)
    skos2 = piecWrzedzieSkos2(X,Y,plansza)
    pion = piecWrzedziePionowo(X,Y,plansza)
    poziom = piecWrzedziePoziomo(X,Y,plansza)
    SET = set([])
    for i in skos1 + skos2 + pion + poziom:
        SET.add(i)
    return SET

def Punkty(punkty):
    font = pygame.font.SysFont("comicsansms", 30, True, False) #bold, ital
    text = font.render('PUNKTY:', True,(0,0,0), (128,128,128))#col, background
    screen.blit(text, (580,20))
    text2 = font.render(str(punkty) + ' ', True,(0,0,0), (128,128,128))#col, background
    screen.blit(text2, (580,70))
    text3 = font.render('Przyjda:', True,(0,0,0), (128,128,128))#col, background
    screen.blit(text3, (580, 150))
    
# # # # ##### 5 w rzedzie ##### # # # #
def piecWrzedzieSkos1(Xklik, Yklik, plansza):
    lista = [(Xklik, Yklik)] #lista z tuplami
    a = 1
    while (Xklik +a, Yklik -a) in plansza.keys() and plansza[(Xklik, Yklik)] == plansza[(Xklik +a, Yklik -a)]:
        lista.append((Xklik +a, Yklik -a))
        a += 1
        
    b = 1
    while (Xklik -b, Yklik +b) in plansza.keys() and plansza[(Xklik, Yklik)] == plansza[(Xklik -b, Yklik +b)]:
        lista.append((Xklik -b, Yklik +b))
        b += 1

    if a + b >= 6:
        return lista
    else:
        return []
    
# # 
def piecWrzedzieSkos2(Xklik, Yklik, plansza):
    lista = [(Xklik, Yklik)]
    a = 1
    while (Xklik +a, Yklik +a) in plansza.keys() and plansza[(Xklik, Yklik)] == plansza[(Xklik +a, Yklik +a)]:
        lista.append((Xklik +a, Yklik +a))
        a += 1
        
    b = 1
    while (Xklik -b, Yklik -b) in plansza.keys() and plansza[(Xklik, Yklik)] == plansza[(Xklik -b, Yklik -b)]:
        lista.append((Xklik -b, Yklik -b))
        b += 1

    if a + b >= 6:
        return lista
    else:
        return []

# #
def piecWrzedziePoziomo(Xklik, Yklik, plansza):
    lista = [(Xklik, Yklik)]
    a = 1
    while (Xklik +a, Yklik) in plansza.keys() and plansza[(Xklik, Yklik)] == plansza[(Xklik +a, Yklik)]:
        lista.append((Xklik +a, Yklik))
        a += 1
        
    b = 1
    while (Xklik -b, Yklik) in plansza.keys() and plansza[(Xklik, Yklik)] == plansza[(Xklik -b, Yklik)]:
        lista.append((Xklik -b, Yklik))
        b += 1

    if a + b >= 6:
        return lista
    else:
        return []
# #
def piecWrzedziePionowo(Xklik, Yklik, plansza):
    lista = [(Xklik, Yklik)]
    a = 1
    while (Xklik, Yklik +a) in plansza.keys() and plansza[(Xklik, Yklik)] == plansza[(Xklik, Yklik +a)]:
        lista.append((Xklik, Yklik +a))
        a += 1
        
    b = 1
    while (Xklik, Yklik -b) in plansza.keys() and plansza[(Xklik, Yklik)] == plansza[(Xklik, Yklik -b)]:
        lista.append((Xklik, Yklik -b))
        b += 1
        
    if a + b >= 6:
        return lista
    else:
        return []
# # # # # # # # # # # # # # # # # # # #
################ szukaj przejscia ####################

def szukaj(plansza, start, x, f): # x = [start]

    node = start
    x.append(start)

    if (node[0]+1, node[1]) in plansza and (node[0]+1, node[1]) not in x and plansza[(node[0]+1, node[1])] == 'nic' and (node[0]+1, node[1]) not in f:
        f.append((node[0]+1, node[1]))
    if (node[0]-1, node[1]) in plansza and (node[0]-1, node[1]) not in x and plansza[(node[0]-1, node[1])] == 'nic' and (node[0]-1, node[1]) not in f:
        f.append((node[0]-1, node[1]))
    if (node[0], node[1]+1) in plansza and (node[0], node[1]+1) not in x and plansza[(node[0], node[1]+1)] == 'nic' and (node[0], node[1]+1) not in f:
        f.append((node[0], node[1]+1))
    if (node[0], node[1]-1) in plansza and (node[0], node[1]-1) not in x and plansza[(node[0], node[1]-1)] == 'nic' and (node[0], node[1]-1) not in f:
        f.append((node[0], node[1]-1))
    if len(f) == 0:
        return x
    elif len(f) == 1:
        return szukaj(plansza, f[0], x, [])
    else:
        return szukaj(plansza, f[0], x, f[1:])

################################################################################

def Loop(plansza, PUNKTY, podswietlony, przyjdzie, gamestate):
    while gamestate == 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                gamestate=0
                pygame.quit()
                exit()        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    '''zaznaczenie kulki'''
                    if (X,Y) in plansza.keys() and plansza[(X,Y)] != 'nic' and podswietlony == False:
                        Podswietl(X,Y)
                        Xo = X
                        Yo = Y
                        kulka = plansza[(X,Y)]
                        podswietlony = True
                        '''przeniesienie wybranej kulki'''
                    elif (X,Y) in plansza.keys() and plansza[(X,Y)] == 'nic' and podswietlony == True:
                        lista_dojsc = szukaj(plansza, (Xo,Yo), [], [])
                        if (X,Y) in lista_dojsc:
                            PrzeniesKulke(Xo,Yo, X,Y, kulka)
                            plansza[(Xo,Yo)] = 'nic'
                            plansza[(X,Y)] = kulka
                            podswietlony = False

                            listaKul = CzyKasuj(X,Y, plansza)
                            if len(listaKul) != 0:
                                PUNKTY += len(listaKul)
                                Kasuj5(listaKul)
                            else:
                                for i in range(3):
                                    pygame.time.wait(300) #przerwa miedzy pojawianiem sie kulek
                                    PUNKTY += nowaKulka(plansza, ListaMiejsc(plansza), PUNKTY, przyjdzie[i])
                                    pygame.display.flip()
                                przyjdzie = TrzyNowe()
                                WyswietlNext(przyjdzie)
                        else:
                            pass
                                   
                        '''zmiana zdania'''
                    elif (X,Y) in plansza.keys() and podswietlony == True and plansza[(X,Y)] != 'nic' and (X,Y) != (Xo,Yo):
                        Zgas(Xo,Yo)
                        Podswietl(X,Y)
                        Xo = X
                        Yo = Y
                        kulka = plansza[(X,Y)]
                        '''odloz kulke'''
                    elif (X,Y) in plansza.keys() and podswietlony == True and plansza[(X,Y)] != 'nic' and (X,Y) == (Xo,Yo):
                        Zgas(Xo,Yo)
                        podswietlony = False
                    elif (X,Y) not in plansza.keys():
                        pass


        myszX, myszY = pygame.mouse.get_pos()
        X = int(myszX)/60
        Y = int(myszY)/60

        Punkty(PUNKTY)
        
        if len(ListaMiejsc(plansza)) == 0:
            gamestate = 0
            
        pygame.display.flip()


    pygame.time.wait(1000)
    font = pygame.font.SysFont("comicsansms", 100, True, False) #bold, ital
    text = font.render('GAME OVER!', True,(0,0,0), (255,255,0))#col, background
    screen.blit(text, (70,200))
    pygame.display.flip()
    pygame.time.wait(2000)
    #plansza zapchana
    pygame.quit()

    pygame.init()  
    nazwa = NICK()
    pygame.quit()

    pygame.init()
    wynik = NajlepszeWyniki()
    wynik.zapisz(PUNKTY, ''.join(nazwa))
    wynik.czytaj()
    pygame.display.flip()

    while True:
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT or (evento.type==KEYDOWN and evento.key==K_ESCAPE):
                gamestate == 0
                pygame.quit()
                exit()
                #break 

#GRA    
okno = pygame.display.set_mode((780, 542)) #dlugosc, wysokosc
pygame.display.set_caption('Kulki') #etykieta

tlo = pygame.image.load('siatka.png').convert()
screen = pygame.display.get_surface() #info o tle ekranu
screen.blit(tlo,(0,0))
pygame.display.flip()

plansza = {}
for i in range(9):
    for j in range(9):
        plansza[(i,j)] = 'nic' # dict: key= x,y value='nic' lub 'biala.png' np

PUNKTY = 0

nowaKulka(plansza, ListaMiejsc(plansza), PUNKTY, LosKolor())
nowaKulka(plansza, ListaMiejsc(plansza), PUNKTY, LosKolor())
nowaKulka(plansza, ListaMiejsc(plansza), PUNKTY, LosKolor())
nowaKulka(plansza, ListaMiejsc(plansza), PUNKTY, LosKolor())
nowaKulka(plansza, ListaMiejsc(plansza), PUNKTY, LosKolor())

przyjdzie = TrzyNowe()
WyswietlNext(przyjdzie)

podswietlony = False
gamestate = 1

pygame.display.flip()

Loop(plansza, PUNKTY, podswietlony, przyjdzie, gamestate)
pygame.quit()

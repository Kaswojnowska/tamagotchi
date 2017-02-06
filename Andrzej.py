#komentarz
class Tamagotchi:
    def __init__(self, plec_Tamagotchi, imie_Tamagotchi, zwierze_Tamagotchi):
        self.plec = plec_Tamagotchi
        self.wiek = 0
        self.imie = imie_Tamagotchi
        self.zwierze = zwierze_Tamagotchi
        self.najedzenie = 100
        self.szczescie = 100
        self.czystosc = 100
        self.zdrowie = 100
        self.glaszcz = 1000


    def powitanie(self):
        print('Cześć, mam na imię', self.imie)

    def jaka_plec(self):
        print('Moja płeć to:', self.plec)

    def wybierz_zwierzatko(self):
        print('Jestem', self.zwierze)

    def karmienie(self, jedz):
        self.najedzenie += 25
        print('Jem', jedz)

    def mycie(self, kapanie):
        self.czystosc += 25
        print('Myję się', kapanie)

    def leczenie(self, choroba):
        self.zdrowie += 25
        print('Jestem chory, potrzebuję', choroba)

    def zabawa(self, gra):
        self.szczescie += 25
        print('Bawię się', gra)

    def glaskanie(self):
        print('Moew moew')

    def uaktualnij(self):
        self.najedzenie -= 30
        self.czystosc -= 25
        self.szczescie -= 50
        self.zdrowie -=10

        if self.najedzenie < 25:
            print('glodny')
        elif self.czystosc < 40:
            print('Tamagotchi brudny - wykąp %s' % (imie))
        elif self.szczescie < 20:
            print('%s jest smutny' % (imie))
        elif self.zdrowie < 10:
            print('apsik')



if __name__ == '__main__':
    print('Witaj w świecie Tamagotchi')
    imie = input('Nadaj imie swojemu Tamagotchi \n')

    while True:
        plec = input('Wybierz płeć:  \n Jeśli dziewczynka, wciśnij 2.\n Jeśli chłopiec, wciśnij 1.\n')
        if plec == '1':
            a = 'Chłopiec'
            break
        elif plec == '2':
            a = 'Dziewczynka'
            break
        else:
            print('Wybierz prawidłową cyfrę!')

    while True:
        zwierze = input('Jakie zwierzę Cię interesuje: \n 1.Chomik \n 2.Piesek \n 3.Kotek \n')
        if zwierze == '1':
            b = 'Chomik\n'
            break
        elif zwierze == '2':
            b = 'Piesek\n'
            break
        elif zwierze == '3':
            b = 'Kotek\n'
            break
        else:
            print('Wybierz zwierzę!')

    potworek = Tamagotchi(a, imie, b)
    potworek.powitanie()
    potworek.jaka_plec()
    potworek.wybierz_zwierzatko()
    print('Pogłaszcz mnie!')

    while True:
        czynnosci = input('\n Co chcesz zrobić z %s ? \n 1.Karmienie\n 2.Mycie\n 3.Leczenie\n 4.Zabawa\n 5.Mizianie\n' % (imie))
        if czynnosci == '1':
            karmienie = input('Napisz co ma jeść %s\n' % (imie))
            c = potworek.karmienie(karmienie)

            if karmienie == 'karma':

                print('Mniam!')

        elif czynnosci == '2':
            kapanie = input('Wpisz gdzie ma się umyć\n')
            d = potworek.mycie(kapanie)

        elif czynnosci == '3':
            leczenie = input('Wpisz co potrzebuje Twój Tamagotchi, gdy jest chory\n')
            e = potworek.leczenie(leczenie)

        elif czynnosci == '4':
            zabawa = input('Napisz w co chcesz się bawić z %s\n' % (imie))
            f = potworek.zabawa(zabawa)

        elif czynnosci == '5':
            glaskanie = input(':poop:\n')
            g= potworek.glaszcz


        potworek.uaktualnij()



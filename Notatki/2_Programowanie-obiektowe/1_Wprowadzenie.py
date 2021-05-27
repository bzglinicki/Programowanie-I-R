# Programowanie I R
# Programowanie obiektowe: wprowadzenie

# **********************************************************************************
# Paradygmat programowania
# **********************************************************************************

# Paradygmat programowania to, mówiąc prosto, styl programowania, określający,
# w jaki sposób rzeczywistość, którą modelujemy w programie, jest reprezentowana
# w jego kodzie źródłowym. Definiuje on zestaw mechanizmów, jakie ma do dyspozycji
# programista pisząc program, oraz określa, jak ów program zostanie wykonany
# przez komputer.

# *** Dla zainteresowanych ***
# Więcej informacji o paradygmatach programowania i przegląd paradygmatów:
#    http://wazniak.mimuw.edu.pl/index.php?title=Paradygmaty_programowania/Wyk%C5%82ad_1:_Co_to_jest_paradygmat_programowania%3F
#    http://zuig.el.pcz.czest.pl/jackrat/progob/bylina.pdf

# Niektóre języki programowania wspierają tylko jeden paradygmat programowania,
# inne pozwalają programiście stosować różne paradygmaty. Python należy do drugiej
# grupy - wspiera m.in. programowanie proceduralne, funkcyjne i obiektowe.
# Zajmiemy się teraz tym ostatnim.


# **********************************************************************************
# Programowanie obiektowe w Pythonie
# **********************************************************************************

# Programowanie obiektowe (ang. object-oriented programming, OOP) jest paradygmatem,
# w którym podstawową rolę odgrywają obiekty - struktury mające reprezentować
# pewne konkretne "wycinki rzeczywistości" oraz łączące je relacje. Program obiektowy
# jest zbiorem mogących się ze sobą komunikować obiektów - to one przechowują dane
# i wykonują na nich operacje, realizując zadania, jakie stawiamy przed programem.

# Obiekty **************************************************************************

# Obiekty zbudowane są ze składowych, które można podzielić na dwie kategorie:
# - pola - określają stan obiektu, jego właściwości - czyli przechowują związane
#   z obiektem dane,
# - metody - określają "zachowanie" obiektu, są w istocie związanymi z obiektem
#   podprogramami, które wykonują na nim operacje.

# Być może będzie nam łatwiej zrozumieć istotę programowania obiektowego,
# gdy przyjrzymy się przykładom obiektów modelujących proste byty z rzeczywistego
# świata.
# 1) Obiekt reprezentujący drzwi mógłby na przykład mieć pola opisujące ich wysokość,
#    szerokość, kolor i stan: otwarte lub zamknięte, oraz metody pozwalające
#    na otwarcie drzwi i na ich zamknięcie.
# 2) Obiekt modelujący psa mógłby posiadać pola: imię, wiek, rasa, właściciel etc. oraz
#    metody: biegnij, szczekaj, aport etc.
# 3) Wiadomość e-mail mogłaby być reprezentowana obiektem posiadającym pola takie,
#    jak np. nadawca, lista adresatów, temat, treść wiadomości i lista załączników
#    oraz metody umożliwiające wysłanie wiadomości, dodanie załącznika etc.

# Proste typy danych, predefiniowane w języku Python - np. liczby zmiennoprzecinkowe,
# łańcuchy tekstowe czy listy - mogą posłużyć do reprezentowania prostych informacji
# - np. promienia koła, tytułu filmu czy listy nazwisk pracowników firmy. Gdy jednak
# chcemy modelować w naszym programie bardziej złożone byty - np. koło, film
# lub przedsiębiorstwo, grupując w logiczne jednostki związane z nimi dane
# i zachowania, najwygodniej będzie posłużyć się bardziej wyrafinowanymi obiektami.

# Warto podkreślić, że dotychczas stosowaliśmy głównie podejście proceduralne - dane
# i procedury wykonujące operacje na tych danych nie były ze sobą bezpośrednio
# powiązane, a program stanowił zbiór pogrupowanych w funkcje instrukcji, które
# wykonywane kolejno prowadziły do rozwiązania postawionego przed programem problemu.
# W programowaniu obiektowym dane i operujące na nich metody są ze sobą związane
# i tworzą logiczne jednostki - obiekty, które definiują strukturę programu.

# Klasy ****************************************************************************

# Klasa jest w języku Python definicją, szablonem obiektu. To ona określa pola
# i metody posiadane przez obiekt. Sama nie przechowuje jednak żadnych danych
# ani nie wykonuje żadnych operacji - czynią tak dopiero obiekty utworzone na jej
# podstawie. Obiekt utworzony na bazie danej klasy nazywany jest jej instancją.

# Tak więc, klasa reprezentująca psa będzie opisywała go abstrakcyjnie, w oderwaniu
# od konkretnych psów, określając po prostu, jakie posiada właściwości (np. imię, rasę,
# właściciela) oraz jego możliwe działania i zachowania (np. biegnij, szczekaj, aport).
# Instancje tej klasy będą zaś reprezentowały konkretne psy, z ustalonymi wartościami
# właściwości (z konkretnymi imieniem, rasą i właścicielem) oraz z możliwością
# wywołania poszczególnych działań i zachowań.

# O klasach można myśleć jako o nowych, złożonych typach danych, zaś o instancjach
# klasy - jako o zmiennych typu określanego przez tę klasę. W istocie niektóre z typów
# danych predefiniowanych w języku Python - np. łańcuch tekstowy albo lista - są
# zaprogramowane jako klasy. Pisząc

rzeczy = []

# tworzymy de facto instancję klasy list, o czym łatwo się przekonać:

print(type(rzeczy))

# zaś instrukcja

rzeczy.append("ABC")

# jest wywołaniem metody append() zdefiniowanej w klasie list na instancji tej klasy
# o nazwie rzeczy. Podobnie, pisząc

"abc".capitalize()

# wywołujemy metodę capitalize() zdefiniowaną w klasie str na obieckie "abc", który
# jest instancją tej klasy.

# Każda klasa może posiadać dowolnie wiele instancji - tak, jak może istnieć dowolnie
# wiele list i łańcuchów tekstowych.
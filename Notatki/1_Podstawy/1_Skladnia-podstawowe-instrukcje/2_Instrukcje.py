# Programowanie I R
# Instrukcje (statements)

# Instrukcja to fragment kodu źródłowego określający pewną konkretną akcję, którą
# ma wykonać program. Program napisany w języku Python jest w istocie ciągiem
# instrukcji, wykonywanych jedna po drugiej. Możemy wyróżnić dwa typy instrukcji:
# instrukcje proste i instrukcje złożone.


# Instrukcje proste (simple statements) ********************************************

# Instrukcjami prostymi nazywamy instrukcje definiujące pojedyncze akcje. Tego typu
# instrukcjami są między innymi przypisanie zmiennej wartości, np.

x = 13         # przypisanie zmiennej o nazwie x wartości 13,

# i wywołanie funkcji, np.

print("ABC")   # wywołanie funkcji o nazwie print.

# W języku Python instrukcja prosta kończy się wraz z końcem linii. Tak więc kod

x = 2      # pierwsza instrukcja: przypisanie,
print(x)   # druga instrukcja: wywołanie funkcji,

# zawiera dwie instrukcje. Istnieje jednak możliwość rozbicia instrukcji na wiele
# linii - należy w tym celu użyć ukośnika (\). Znak ten umieszczony na końcu linii
# informuje, że kod źródłowy zawarty w kolejnej linii jest kontynuacją instrukcji
# z linii bieżącej. Na przykład, poniższe trzy linie zawierają jedną instrukcję:

x = 1 + 3 + \
    2 + 5 + \
    8 + 9       # jedna instrukcja: przypisanie zmiennej x wartości 28.

# Instrukcje zawierające nawiasy (dowolnego typu: okrągłe (), kwadratowe [] lub
# klamrowe {}) mogą zostać podzielone na linie bez stosowania ukośnika: jeśli
# odpowiadające sobie nawiasy otwierający i zamykający znajdują się w różnych
# liniach, Python traktuje te linie i wszystkie linie między nimi jak jedną instrukcję:

x = (1 + 3 +
    2 + 5 +
    8 + 9)      # jedna instrukcja: przypisanie zmiennej x wartości 28.

# Możliwe jest również umieszczenie kilku instrukcji prostych w jednej linii - należy
# je wówczas oddzielić średnikiem (;):

a = 1; b = 3; print(a + b)


# Instrukcje złożone (compound statements) i bloki kodu ****************************

# Instrukcja złożona, w przeciwieństwie do instrukcji prostej, nie określa
# pojedynczej, konkretnej akcji, lecz jest sekwencją innych instrukcji (prostych
# i złożonych), stanowiących logiczną całość.

# Instrukcje złożone są często wykorzystywane do sterowania wykonywaniem kodu, np.
# do wykonania określonego fragmentu kodu wielokrotnie (tzw. pętle) lub tylko wtedy,
# gdy spełniony jest pewien warunek (tzw. instrukcje warunkowe). Stosuje się je
# również m.in. w mechanizmie obsługi tzw. wyjątków, czyli nieoczekiwanych sytuacji.

# Instrukcja złożona zbudowana jest z nagłówka, określającegeo jej tożsamość i pewne
# dodatkowe jej cechy (np. w przypadku instrukcji warunkowej - warunek, który musi
# być spełniony, by fragment kodu objęty tą instrukcją został wykonany), oraz z bloku
# kodu nazywanego ciałem instrukcji. Pomiędzy nagłówkiem i ciałem znajduje się
# dwukropek (:).

# Język Python do definiowania bloków kodu wykorzystuje wcięcia, czyli znaki białe
# umieszczone na początku linii: każda linia kodu tworząca blok musi zawierać takie
# samo wcięcie. Wcięcie to może być zbudowane ze znaków spacji i tabulatora w dowolnej
# ilości i kolejności, istotne jest jedynie to, by wcięcie było identyczne w każdej
# linii tworzącej dany blok kodu. Zwykle jako wcięcie wykorzystuje się trzy lub cztery
# znaki spacji.

# Przykładem instrukcji złożonej jest instrukcja warunkowa if. Kod źródłowy zawarty
# w jej ciele zostanie wykonany tylko wówczas, gdy spełniony jest warunek określony
# w jej nagłówku. Na przykład:

if x < 50:     # nagłówek instrukcji,
    print(x)   # ciało instrukcji - linia 1.,
    x = 90     # ciało instrukcji - linia 2.,
    print(x)   # ciało instrukcji - linia 3.

# Instrukcje złożone można również zapisywać w jednej linii, oddzielając instrukcje
# stanowiące ciało instrukcji złożonej średnikami:

if x < 50: print(x); x = 90; print(x)

# Zapis taki najlepiej stosować wtedy, gdy ciało instrukcji zbudowane jest tylko
# z jednej instrukcji prostej, np.

if x < 50: x = 90

# W przypadku bardziej rozbudowanych instrukcji złożonych zapis w jednej linii
# może okazać się nieczytelny.

# Instrukcje złożone mogą być zagnieżdżane - oznacza to, że w ciele instrukcji
# złożonej mogą się znaleźć, obok instrukcji prostych, także instrukcje złożone.
# Na przykład

if x < 500:      # nagłówek instrukcji "zewnętrznej",
    print(x)     # ciało instrukcji "zewnętrznej" - linia 1.,
    if x > 10:   # ciało instrukcji "zewnętrznej" - linia 2.: nagłówek instrukcji "wewnętrznej",
        x = 25   # ciało instrukcji "wewnętrznej" (zawiera tylko jedną linię),
    print(x)     # ciało instrukcji "zewnętrznej" - linia 3.

# Zagnieżdzanie może być oczywiście "wielopoziomowe" - w ciele zagnieżdżonej
# instrukcji mogą znajdować się kolejne instrukcje złożone, na przykład

if x < 350:
    print("Wartość zmiennej x jest mniejsza od 350...")
    if x < 300:
        print("...oraz od 300.")
        if x < 250:
            print("...oraz od 250.")

# Należy pamiętać, że blok kodu stanowiący ciało instrukcji wewnętrznej 
# musi mieć wcięcie większe niż blok będący ciałem instrukcji zewnętrznej.

# Niepoprawne rozmieszczenie wcięć może skutkować wystąpieniem błędu
# IndentationError, program nie zostanie wówczas wykonany poprawnie.
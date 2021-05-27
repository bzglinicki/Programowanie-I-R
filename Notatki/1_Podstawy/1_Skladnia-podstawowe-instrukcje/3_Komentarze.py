# Programowanie I R
# Komentarze (comments)

# Komentarze to fragmenty kodu źródłowego ignorowane przez interpreter języka Python.
# Nie mają one zatem żadnego wpływu na działanie programu, są przeznaczone dla ludzi,
# którzy czytają kod źródłowy i mają pomóc im go zrozumieć. Komentarze powinny zatem
# informować, co dany fragment kodu ma wykonać, oraz zwracać uwagę na jego istotne
# cechy. To, jakie informacje przekażemy w komentarzach, zależy wyłącznie od nas.

# Pisanie komentarzy jest niezwykle pożyteczne. Pomogą one zapewne zaoszczędzić
# sporo czasu i wysiłku nie tylko osobom, którym pokażemy nasz kod, ale także
# nam samym, gdy wrócimy do napisanego przez siebie kodu po dłuższej przerwie.

# Komentarze mogą być również wykorzystywane podczas testowania działania programu
# w celu chwilowego "wyłączenia" fragmentu jego kodu źródłowego. Oznaczenie fragmentu
# kodu jako komentarz spowoduje, że nie zostanie on wzięty pod uwagę podczas
# wykonywania programu; gdy zdecydujemy, że chcemy "przywrócić" ten fragment kodu,
# wystarczy usunąć oznaczenie jako komentarz.


#***********************************************************************************
# Komentarze "standardowe"
#***********************************************************************************

# Komentarz w języku Python rozpoczyna się znakiem # i kończy wraz z końcem linii.
# Wszystkie opisy w niniejszych notatkach są komentarzami (również ten tekst).
# Wartko podkreślić, że komentarz nie musi zaczynać się wraz z początkiem linii:

print("Tu jest właściwy kod źródłowy...") # ...a tu komentarz.

# Komentarze wieloliniowe w Pythonie nie istnieją, gdy zatem chcemy rozbić komentarz
# na kilka linii, musimy w każdej z nich umieścić znak #.


#***********************************************************************************
# Łańcuchy tekstowe jako komentarze
#***********************************************************************************

# Łańcuchy tekstowe umieszczone w kodzie źródłowym bez żadnego kontekstu, a zatem
# nie stanowiące wartości przypisywanych zmiennym ani wartości argumentów funkcji,
# są ignorowane przez interpreter, mogą zatem pełnić rolę komentarzy.

x = "Ten łańcuch zostanie przypisany do zmiennej x."
print("Ten łańcuch zostanie wartością pierwszego argumentu funkcji print.")

"Ten łańcuch zostanie zignorowany, może zatem pełnić rolę komentarza!"

# W języku Python istnieją wieloliniowe łańcuchy tekstowe - w odróżenieniu od
# "zwykłych" łańcuchów są one ujęte nie w pojedymczy, a w potrójny cudzysłów (")
# lub apostrof ('); powiemy o tym więcej przy okazji omawiania łańcuchów tekstowych.
# Takie wieloliniowe łańcuchy również są ignorowane przez interpreter i mogą dzięki
# temu pełnić rolę wieloliniowych komentarzy.

"""
Ten wieloliniowy łańcuch tekstowy
zostanie zignorowany, może zatem
pełnić rolę komentarza.
"""

# Istnieje pewien wyjątek od zasady mówiącej, że interpreter Pythona ignoruje
# łańcuchy tekstowe, które nie są częścią żadnej instrukcji. Łańcuchy takie
# umieszczone w definicji funkcji, klasy lub modułu bezpośrednio po jej nagłówku
# są interpretowane jako dokumentacja i pełnią szczególną rolę. Wyjaśnimy to
# przy okazji omawiania sposobów dokumentowania kodu.
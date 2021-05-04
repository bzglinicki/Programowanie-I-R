# Programowanie I R
# Operacje na plikach: podstawy

# Wykonywanie operacji na pliku, czyli odczyt i zapis jego zawartości,
# wymaga otwarcia pliku na samym początku i zamknięcia go na końcu.

# Zamknięcie pliku jest bardzo ważne - zwalniane są wówczas zasoby
# związane z tym plikiem, a niektóre operacje zapisu do pliku mogą
# z powodu buforowania zostać wykonane dopiero w chwili jego zamknięcia.

# Operacje na pliku przebiegają zatem zgodnie z następującym schematem:
#    1. Otwarcie pliku - metoda open().
#    2. Właściwe operacje na pliku (odczyt, zapis).
#    3. Zamknięcie pliku - metoda close() lub automatyczne.

# Schemat ten można zrealizować na trzy sposoby, z których jeden jest niezalecany.

# Operacje na pliku - sposób I: bezpośredni   - ŹLE ********************************

f = open("plik.txt")
# --- Właściwe operacje na f. ---
f.close()

# Ten sposób nie jest bezpieczny, gdyby bowiem podczas wykonywania operacji na pliku,
# pomiędzy wywołaniami funkcji open() i close(), wystąpił wyjątek, wykonywanie
# programu zostałoby przerwane i funkcja close() nie zostałaby wywołana.

# Operacje na pliku - sposób II: try...finally   - DOBRZE **************************

try:
   f = open("plik.txt")
   # --- Właściwe operacje na f. ---
finally:
   f.close()

# Ten sposób gwarantuje, że plik zostanie poprawnie zamknięty, nawet jeśli podczas
# wykonywania na nim operacji wystąpi wyjątek.

# Operacje na pliku - sposób III: with   - NAJLEPIEJ *******************************

with open("plik.txt") as f:
   # --- Właściwe operacje na f. ---

# Nie ma tu potrzeby jawnego wywoływania funkcji close() - dzieje się to samoistnie.
# Ten sposób jest w pełni bezpieczny i gwarantuje, że plik zostanie poprawnie
# zamknięty, gdy program opuści blok kodu instrukcji with, nawet jeśli wewnątrz
# tego bloku wystąpi wyjątek.

# Poniższa linijka nie ma żadnego znaczenia, została tu umieszczona tylko ze względu
# na kosntrukcję tego pliku (powyższy blok with nie zawiera żadnych instrukcji poza
# komentarzami, co przez interpreter Pythona traktowane jest jako błąd, dlatego
# dodajemy instrukcję pass definiującą pusty blok, by kod był uznany za poprawny).
   pass



# **********************************************************************************
# Kursor
# **********************************************************************************

# Istotną rolę w procesach odczytu z pliku i zapisu do pliku odgrywa kursor.
# Wskazuje on miejsce w pliku, w którym rozpocznie się operacja odczytu lub
# zapisu: odczytywane będą kolejne znaki (lub bity) znajdujące się za kursorem,
# zapisywane znaki (lub bity) będą umieszczane tam, gdzie aktualnie znajduje
# się kursor. O kursorze w Pythonie można myśleć dokładnie tak samo, jak
# o kursorze w dowolnym edytorze tekstu.

# Więcej informacji na temat kursora pojawi się przy omawianiu operacji
# odczytu i zapisu zawartości pliku.



# **********************************************************************************
# Otwieranie pliku - metoda open()
# **********************************************************************************

# Metoda open() przyjmuje jako argument nazwę pliku do otwarcia i zwraca obiekt
# specjalnego typu (tzw. file object), nazywany niekiedy uchwytem, pozwalający
# odwoływać się do otwartego pliku.

open("plik.txt")             # Otwarcie pliku plik.txt z bieżącego folderu.
open("C:\\Dane\\plik.txt")   # Otwarcie pliku plik.txt z folderu C:\Dane.

# Tryb (ang. mode) *****************************************************************

# Metoda open() ma opcjonalny argument mode, występujący jako drugi w kolejności,
# który pozwala określić, w jakim trybie otwierany jest plik.

# Tryb definiowany jest przez łańcuch tekstowy zbudowany z jednego, dwóch lub
# trzech znaków i określa:

#    a) jakie operacje na pliku są dopuszczalne:

#       - "r" - tryb odczytu (ang. read), domyślny:
#         * możliwy jest odczyt zawartości pliku, zaś jej modyfikacja - nie,
#         * po otwarciu pliku kursor zostanie umieszczony na jego początku,
#         * jeśli plik nie istnieje, zgłoszony zostanie wyjątek FileNotFoundError,

#       - "w" - tryb zapisu (ang. write):
#         * możliwy jest zapis do pliku, zaś odczyt z pliku - nie,
#         * jeśli plik nie istnieje, zostanie utworzony (początkowo pusty),
#           a kursor zostanie umieszczony na jego początku,
#         * jeśli plik istnieje, cała jego zawartość zostanie skasowana,
#           a kursor zostanie umieszczony na jego początku;
#           nowa zawartość pliku zastąpi więc starą,

#       - "a" - tryb dołączania (ang. append):
#         * możliwy jest zapis do pliku, zaś odczyt z pliku - nie,
#         * jeśli plik nie istnieje, zostanie utworzony (początkowo pusty),
#           a kursor zostanie umieszczony na jego początku;
#         * jeśli plik istnieje, jego zawartość nie zostanie skasowana,
#           kursor zaś zostanie umieszczony na jego końcu,
#         * nowa zawartość pliku będzie zawsze dopisywana na jego końcu,
#           (niezależnie od położenia kursora), dotychczasowa zawartość
#           nie zostanie nigdy nadpisana,

#       - "x" - tryb tworzenia:
#         * możliwy jest zapis do pliku, zaś odczyt z pliku - nie,
#         * jeśli plik nie istnieje, zostanie utworzony (początkowo pusty),
#           a kursor zostanie umieszczony na jego początku,
#         * jeśli plik istnieje, zgłoszony zostanie wyjątek FileExistsError,

#       - "+" - tryb edycji:
#         * tryb ten jest zawsze "rozszerzoną" wersją jednego z powyższych trybów,
#           znak "+" towarzyszy zatem zawsze jednemu ze znaków: "r", "w", "a" lub "x",
#         * dodanie "+" do litery określającej jeden z powyższych trybów powoduje,
#           że tryb ten dopuszcza "przeciwną" operację, zabronioną w standardowej
#           jego wersji; tak więc tryb "r+" jest identyczny z trybem "r", oprócz
#           odczytu z pliku możliwy jest jednak również zapis do pliku, zaś tryby
#           "w+", "a+" i "x+" są identyczne z trybami, odpowiednio, "w", "a" i "x",
#           z tą różnicą, że dopuszczają dodatkowo odczyt zawartości pliku,

#    a) jak interpretowana jest zawartość pliku:

#       - "t" - tryb tekstowy (ang. text), domyślny:
#         * zawartość pliku jest interpretowana jako tekst: odczytywane i zapisywane
#           dane są łańcuchami tekstowymi; z "technicznego" punktu widzenia
#           oznacza to, że podczas odczytu i zapisu kolejne bity danych
#           (w odpowiedniej ilości) są interpretowane jako znaki alfanumeryczne
#           zgodnie z przyjętym kodowaniem (patrz niżej, sekcja "Kodowanie"),
#         * tryb właściwy dla plików tekstowych, czyli plików zawierających dane w postaci
#           alfanumerycznej, które należy traktować jako ciągi znaków (liter, liczb etc.),
#         * przykłady plików tekstowych: dokumenty bez formatowania (np. .txt, .tex, .md), 
#           pliki opisujące strony internetowe (np. .html, .css), tekstowe pliki z danymi
#           (np. .csv, .tsv, .xml, .json), kody źródłowe programów (np. .py, .c, .cpp, .h,
#           .cs, .xaml, .vb, .js, .java),

#       - "b" - tryb binarny (ang. binary):
#         * zawartość pliku nie jest w żaden sposób interpretowana: odczytywane i zapisywane
#           dane są traktowane jako dane binarne (typ bytes),
#         * tryb właściwy dla plików binarnych, czyli plików, które nie są
#           plikami tekstowymi,
#         * przykłady plików binarnych: obrazy (np. .bmp, .png, .jpg, .gif), pliki audio
#           (np. .mp3, .wav), pliki wideo (np. .avi, .mp4, .mov), pliki wykonywalne
#           (np. .exe, .dll), dokumenty z formatowaniem (np. .pdf, .docx, .odt),
#           archiwa (np. .zip, .rar, .7z, .gz).

# Informacje o dopuszczalnych operacjach i sposobie interpretowania zawartości pliku
# są niezależne, obie powinny się znaleźć w łańcuchu tekstowym określającym tryb.
# Tak więc, możliwe tryby to:
#    "r" (równoważnie "rt"), "w" (równ. "wt"), "a" (równ. "at"), "x" (równ. "xt"),
#    "r+" (równ. "r+t"), "w+" (równ. "w+t"), "a+" (równ. "a+t"), "x+" (równ. "x+t"),
#    "rb", "wb", "ab", "xb", "r+b", "w+b", "a+b", "x+b".

# W sytuacji, w której zależy nam wyłącznie na odczycie zawartości pliku (zawierającego
# na przykład dane, które mamy analizować), najlepiej zatem zastosować tryb "r" (lub "rb"
# w przypadku danych binarnych). Gdy chcemy edytować już istniejący plik, a więc
# odczytywać jego zawartość i wprowadzać w nim zmiany, najlepiej sprawdzi się tryb "r+"
# (lub "r+b"); należy jednak pamiętać, aby przed wykonaniem operacji odczytu lub zapisu
# ustawić kursor we właściwym miejscu. Tryb "w" (lub "wb") będzie idealny, gdy chcemy
# zbudować zawartość pliku (już istniejącego lub jeszcze nie) od zera (by np. zapisać
# stan jakiegoś obiektu lub konfigurację programu); jeśli potrzebujemy dodatkowo
# możliwości odczytu zawartości pliku, właściwym trybem będzie "w+" (lub "w+b").

# Przykłady

# Początkowo pliki plik1.txt i plik2.txt nie istnieją.

with open("plik1.txt", "w") as f:
   f.write("ab\n")

# plik1.txt:
# ab
# (pusta linia)

with open("plik1.txt", "w+") as f:
   f.write("c")

# plik1.txt:
# c

with open("plik2.txt", "r+") as f:
   f.write("ab\n")

# Wyjątek:
#    FileNotFoundError: [Errno 2] No such file or directory: 'file2.txt'

with open("plik2.txt", "w") as f:
   f.write("ab\n")

# plik2.txt:
# ab
# (pusta linia)

with open("plik2.txt", "r+") as f:
   f.write("c")

# plik2.txt:
# cb
# (pusta linia)

# Kodowanie (ang. encoding) ********************************************************

# Kodowanie to przyporządkowanie każdemu ze znaków alfanumerycznych (liter, cyfr,
# znaków białych, znaków specjalnych etc.) jego reprezentacji binarnej. Odgrywa ono
# istotną rolę przy pracy z plikami tekstowymi, informuje bowiem, jak zamienić łańcuch
# tekstowy na kod binarny, który można zapisać w pliku, i vice versa.

# Więcej informacji na temat kodowania znaków znaleźć można m.in. na stronach
#    https://www.flynerd.pl/2019/09/kodowanie-znakow-ascii-unicode-utf-co-to-znaczy.html
#    http://kursdlaopornych.pl/iso-ascii-unicode-kodowanie-znakow/

# Metoda open() posiada opcjonalny argument encoding, pozwalający określić kodowanie
# używane podczas pracy z plikiem. Domyślna wartość zależy od systemu operacyjnego
# (można ją sprawdzić, korzystając z funkcji getpreferredencoding() z modułu locale),
# dlatego warto zawsze wprost określać kodowanie, jakiego chcemy używać.

# Obecnie standardem wydaje się być kodowanie UTF-8, obejmujące m.in. polskie znaki
# (oraz znaki charakterystyczne dla większości alfabetów świata). Jego użycie
# wymaga przypisania argumentowi encoding metody open() wartości "utf-8":
open("plik.txt", mode = "r", encoding = "utf-8")

# Należy podkreślić, że kodowanie dotyczy wyłącznie plików tekstowych, nie ma więc
# potrzeby określać kodowania, gdy otwieramy plik w trybie binarnym ("b").
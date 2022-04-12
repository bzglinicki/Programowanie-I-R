# Programowanie I R
# Programowanie obiektowe: klasy i obiekty

# Klasy ****************************************************************************

# Klasy definiujemy, używając słowa kluczowego "class", po którym należy umieścić nazwę
# klasy oraz dwukropek. W kolejnych liniach powinien znaleźć się blok kodu tworzący
# ciało klasy, wyrózniony - jak zwykle w Pythonie - wcięciem.

# Przykład (pustej) klasy o nazwie "MyClass":
class MyClass:
    pass   # Instrukcja pass oznacza - jak zwykle - pusty blok kodu.

# Taka pusta klasa nie ma zbyt wiele do zaoferowania (choć nie jest całkowicie
# bezużyteczna - o tym za chwilę), niebawem nauczymy się, jak definiować w ciele
# klasy pola i metody obiektów, które będą jej instancjami.


# Obiekty (instancje) **************************************************************

# Mając już klasę, możemy utworzyć jej instancję:
obj = MyClass()

# To właśnie teraz powstał "realny" byt - obiekt, który może przechowywać
# i przetwarzać informacje. Instancji danej klasy możemy utworzyć dowolnie wiele.


# Metody ***************************************************************************

# Jak wspomnieliśmy we wprowadzeniu, z obiektami związane są dwa typy składowych
# (atrybutów): pola i metody. Zajmiemy się na początek omówieniem tych drugich.

# Metody związane z obiektem są definiowane jako funkcje w ciele klasy, której
# instancją jest ten obiekt. Funkcje takie mają jedną szczególną cechę: przyjmują
# zawsze argument o nazwie "self"; gdy metoda przyjmuje wiele argumentów, "self"
# musi być pierwszym z nich. Argument "self" ma szczególne znaczenie: reprezentuje
# on obiekt, na rzecz którego została wywołana metoda. Dzięki jego obecności metoda
# ma dostęp do wartości pól obiektu, na którym została wywołana, oraz może
# sama wywoływać inne metody tego obiektu. Wywołując metodę, nie przypisujemy
# wartości argumentowi "self", Python zrobi to za nas; wyłołujemy zatem metodę
# tak, jak gdyby argument "self" nie istniał.

# Rozważmy dla przykładu następującą klasę:

class MethodExample:
    def Method1(self):
        return f"Metoda Method1 pozdrawia!\nTyp argumentu self: {type(self)}"
    
    def Method2(self, message):
        return f"Metoda Method2 pozdrawia!\nPrzesłanie: {message}"
    
    def Method3(self, x, y):
        result = x + y
        return f"Metoda Method3 pozdrawia!\n{x} + {y} = {result}"

# Definiuje ona trzy metody: "Method1", "Method2" i "Method3". Możemy teraz
# utworzyć instancję tej klasy:

obj = MethodExample()

# a następnie wywołać na niej którąś z metod. Wywołanie metody wymaga zastosowania
# operatora "." (kropka) i powinno zawsze mieć postać
#    obiekt.metoda(ewentualne argumenty)
# Na przykład

obj.Method1()

# Należy tu koniecznie zwrócić uwagę, że wywołując metodę zignorowaliśmy
# jej argument "self", ponieważ - jak już wspomnieliśmy - Python sam przypisuje
# mu wartość; jest nią zawsze obiekt, na rzecz którego metoda jest wywoływana,
# a więc w tym przypadku "obj". W istocie powyższa instrukcja jest równoważna instrukcji

MethodExample.Method1(obj)

# Pozostałe metody określone w klasie "MethodExample" mają oprócz "self" jeszcze
# inne argumenty, którym przypisujemy wartości w standardowy sposób, np.

obj.Method2("In omnibus requiem quaesivi, et nusquam inveni nisi in angulo cum libro.")

# Możemy teraz upewnić się, że metody rzeczywiście działają, wypisując zwracane
# przez nie wartości.

print(obj.Method1())
# Równoważnie: print(MethodExample.Method1(obj))

print(obj.Method2("In omnibus requiem quaesivi, et nusquam inveni nisi in angulo cum libro."))
# Równoważnie: print(MethodExample.Method2(obj,
#              "In omnibus requiem quaesivi, et nusquam inveni nisi in angulo cum libro."))

print(obj.Method3(2, 3))
# Równoważnie: print(MethodExample.Method3(obj, 2, 3))


# Metoda __init__ (konstruktor) **************************************************

# Każda klasa może definiować specjalną metodę o nazwie "__init__" (na początku
# i na końcu nazwy znajdują się dwa podkreślniki). Metoda ta zachowuje się pod
# każdym względem tak samo, jak inne metody, ma jednak pewną szczególną cechę:
# jest wywoływana automatycznie bezpośrednio po utworzeniu obiektu klasy.

# Zilustrujemy to na przykładzie następującego programu:

class InitExample1:
    def __init__(self):
        print("Witam!")

obj = InitExample1()

# Wykonanie tego programu skutkuje wyświetleniem napisu "Witam!", mimo że nigdzie
# nie następuje jawne wywołanie metody "__init__". Jest ona zatem w istocie
# wywoływana automatycznie, natychmiast po utworzeniu instancji klasy InitExample.
# To automatyczne wywołanie jest równoważne instrukcji
#    obj.__init__()

# Metody wywoływane natychmiast po utworzeniu obiektu nazywa się zwykle w terminologii
# programowania obiektowego kosntruktorami. Tak więc, metoda "__init__" pełnie w Pythonie
# rolę konstruktora klasy.

# Konstruktory wykorzystuje się zwykle do ustalenia stanu początkowego obiektu,
# czyli do przypisania początkowych wartości jego polom, oraz do wykonania operacji,
# które mają przygotować obiekt do pracy.

# Metoda "__init__", jak każda metoda, może oprócz "self" przyjmować również inne
# argumenty. Wartości tych argumentów należy określić w chwili tworzenia instancji
# klasy, wymieniając je w nawiasach po nazwie klasy. Ilustruje to następujący przykład:

class InitExample2:
    def __init__(self, name):
        print(f"Witam Cię, {name}!")

obj = InitExample2("Bartek")

# Wykonanie tego programu skutkuje wypisaniem "Witam Cię, Bartek!"
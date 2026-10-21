# ZADANIE 3.1
# Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?
#
# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
# for i in "axby": if ord(i) < 100: print (i)
# for i in "axby": print (ord(i) if ord(i) < 100 else i)
#
# ODPOWIEDŹ:
# 1. `x = 2; y = 3;`
#    POPRAWNY. W Pythonie średnik może rozdzielać instrukcje proste w jednej linii.
#    Średnik na końcu linii jest dozwolony, choć domyślam się że niezalecany
#
# 2. `if (x > y): ... else: ...`
#    POPRAWNY. Nawiasy wokół warunku są dopuszczalne (choć redundantne),
#    a średniki na końcach instrukcji są dozwolone.
#
# 3. `for i in "axby": if ord(i) < 100: print (i)`
#    NIEPOPRAWNY SKŁADNIOWO.
#    Po dwukropku instrukcji złożonej (np. for) w tej samej linii
#    nie można umieszczać kolejnej instrukcji złożonej. W jednej linii
#    dopuszczalne są jedynie instrukcje proste.
#
# 4. `for i in "axby": print (ord(i) if ord(i) < 100 else i)`
#    POPRAWNY. Po dwukropku pętli for znajduje się pojedyncza instrukcja prosta (print),
#    wewnątrz której użyto wyrażenia warunkowego


# ZADANIE 3.2
# Co jest złego w kodzie:
#
# 1. `L = [3, 5, 4] ; L = L.sort()`
#    BŁĄD: Metoda list.sort() sortuje listę w miejscu i zwraca None.
#    Przypisanie L = L.sort() powoduje, że L staje się None i tracimy referencję do listy.
#    Samo `L.sort()` lub `L = sorted(L)`.
#
# 2. `x, y = 1, 2, 3`
#    BŁĄD: ValueError: too many values to unpack (expected 2, got 3).
#    Próba rozpakowania 3-elementowej krotki do tylko 2 zmiennych.
#    x, y, z = 1, 2, 3 lub x, *y = 1, 2, 3.
#
# 3. X = 1, 2, 3 ; X[1] = 4
#    BŁĄD: TypeError: 'tuple' object does not support item assignment.
#    X jest krotką (tuple), a krotki są niemutowalne (immutable).
#
# 4. `X = [1, 2, 3] ; X[3] = 4`
#    BŁĄD: IndexError: list assignment index out of range.
#    Lista X ma 3 elementy o indeksach 0, 1, 2. Indeks 3 wykracza poza zakres listy.
#
# 5. `X = "abc" ; X.append("d")`
#    BŁĄD: AttributeError: 'str' object has no attribute 'append'.
#    Napisy (str) są niemutowalne i nie posiadają metody append.
#
# 6. `L = list(map(pow, range(8)))`
#    BŁĄD: TypeError: pow expected at least 2 arguments, got 1.
#    Funkcja pow(x, y) wymaga co najmniej 2 argumentów (podstawy i wykładnika).

# ZADANIE 3.3
# Wypisać w pętli liczby od 0 do 30 włącznie, z wyjątkiem liczb podzielnych przez 3.
# Podać dwa rozwiązania, jedno z pętlą for, drugie z pętlą while.
# W zadaniach budujemy całe napisy, a nie wyświetlamy po kawałku.

# for:
numbers_for = []
for i in range(31):
    if i % 3 == 0:
        continue
    numbers_for.append(str(i))
result_for = " ".join(numbers_for)
print("Zadanie 3.3 (for):", result_for)

# while:
numbers_while = []
i = 0
while i <= 30:
    if i % 3 != 0:
        numbers_while.append(str(i))
    i += 1
result_while = " ".join(numbers_while)
print("Zadanie 3.3 (while):", result_while)

expected_3_3 = "1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 23 25 26 28 29"
assert result_for == expected_3_3
assert result_while == expected_3_3


# ZADANIE 3.4
# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float)
# i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu
# z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma
# wypisać komunikat o błędzie i kontynuować pracę.

# Aby uzyskać liczbę rzeczywistą x (typ float), rzutujemy: x = float(entry).
# Jeśli użytkownik wpisze słowo "stop" -> kończymy pętlę.
# Jeśli użytkownik wpisze inny napis (np. "abc") -> float() rzuci ValueError,

def process_number_input(entry: str) -> tuple[str, tuple[float, float] | None]:
    cleaned = entry.strip()
    if cleaned.lower() == "stop":
        return "stop", None
    try:
        val = float(cleaned)  # tutaj z napisu powstaje liczba rzeczywista (float)
        return "ok", (val, val ** 3)
    except ValueError:
        return "error", None

# Testy asercji logiki zadania 3.4:
assert process_number_input("stop") == ("stop", None)
assert process_number_input("STOP") == ("stop", None)
assert process_number_input("2.5") == ("ok", (2.5, 15.625))
assert process_number_input("-3") == ("ok", (-3.0, -27.0))
assert process_number_input("tekst") == ("error", None)

def task_3_4():
    """Główna funkcja programu pobierająca dane z klawiatury."""
    while True:
        user_input = input("Podaj liczbę rzeczywistą (lub 'stop' aby zakończyć): ")
        status, data = process_number_input(user_input)
        if status == "stop":
            print("Zakończono program.")
            break
        elif status == "ok":
            assert data is not None
            x, cube = data
            # Budujemy cały napis przed wypisaniem:
            result = f"x = {x}, x^3 = {cube}"
            print(result)
        else:
            print(f"Błąd: '{user_input.strip()}' nie jest poprawną liczbą rzeczywistą!")

task_3_4()


# ZADANIE 3.5
# Napisać program rysujący "miarkę" o zadanej długości. Długość miarki (x) ma być
# zapisana w osobnej zmiennej jako parametr programu. Należy prawidłowo obsłużyć
# liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się
# pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

def make_ruler(x: int) -> str:
    top = "|" + "....|" * x
    bottom = "0" + "".join(f"{i:>5}" for i in range(1, x + 1))
    return f"{top}\n{bottom}"

x = 12
ruler = make_ruler(x)
print(ruler)

expected_ruler_12 = (
    "|....|....|....|....|....|....|....|....|....|....|....|....|\n"
    "0    1    2    3    4    5    6    7    8    9   10   11   12"
)
assert ruler == expected_ruler_12
assert make_ruler(1) == "|....|\n0    1"


# ZADANIE 3.6
# Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować
# pełny string, a potem go wypisać. Liczby kratek w wierszach (y) i kolumnach (x)
# mają być zapisane w osobnych zmiennych jako parametry programu.

def make_grid(x: int, y: int) -> str:
    horizontal = "+---" * x + "+"
    vertical = "|   " * x + "|"
    lines = [horizontal]
    for _ in range(y):
        lines.append(vertical)
        lines.append(horizontal)
    return "\n".join(lines)

x = 4
y = 2
grid = make_grid(x, y)
print(grid)

expected_grid_4_2 = (
    "+---+---+---+---+\n"
    "|   |   |   |   |\n"
    "+---+---+---+---+\n"
    "|   |   |   |   |\n"
    "+---+---+---+---+"
)
assert grid == expected_grid_4_2
assert make_grid(1, 1) == "+---+\n|   |\n+---+"


# ZADANIE 3.7
# 1. Jeżeli zdefiniujemy tylko __repr__, to zostanie ona użyta również jako fallback
#    dla __str__ (np. przy print(obj)).
# 2. Jeżeli zakomentujemy __repr__ a zostawimy __str__:
#    print(time1, time2) wypisze postać ze __str__ ("12 sec 3456 sec"),
#    ale print([time1, time2]) wypisze reprezentację domyślną z object.__repr__,
#    czyli np. "[<__main__.Time object at 0x...>, <__main__.Time object at 0x...>]",
#    ponieważ kontenery (listy, słowniki, krotki) wywołują repr() na swoich elementach.

class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "{} sec".format(self.s)

    def __repr__(self):
        return "Time({})".format(self.s)

time1 = Time(12)
time2 = Time(3456)
assert str(time1) == "12 sec"
assert repr(time1) == "Time(12)"
assert str([time1, time2]) == "[Time(12), Time(3456)]"


# ZADANIE 3.8
# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

def common_elements(seq1, seq2):
    """(a) Lista elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń)."""
    return list(set(seq1) & set(seq2))

def all_elements(seq1, seq2):
    """(b) Lista wszystkich elementów z obu sekwencji (bez powtórzeń)."""
    return list(set(seq1) | set(seq2))

seq_a = [1, 2, 3, 4, 3, 2, 1]
seq_b = [3, 4, 5, 6, 4]
common_nums = common_elements(seq_a, seq_b)
all_nums = all_elements(seq_a, seq_b)
print("Zadanie 3.8 - wspólne liczby:", sorted(common_nums))
print("Zadanie 3.8 - wszystkie liczby:", sorted(all_nums))
assert sorted(common_nums) == [3, 4]
assert sorted(all_nums) == [1, 2, 3, 4, 5, 6]

# Przykład dla sekwencji znaków:
seq_str1 = "abracadabra"
seq_str2 = "barbados"
common_chars = common_elements(seq_str1, seq_str2)
all_chars = all_elements(seq_str1, seq_str2)
print("Zadanie 3.8 - wspólne znaki:", sorted(common_chars))
print("Zadanie 3.8 - wszystkie znaki:", sorted(all_chars))
assert sorted(common_chars) == ['a', 'b', 'd', 'r']
assert sorted(all_chars) == ['a', 'b', 'c', 'd', 'o', 'r', 's']
# sortujemy ponieważ set() nie gwarantuje że elementy są w tej samej kolejności

# ZADANIE 3.9
# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
# Znaleźć listę zawierającą sumy liczb z tych sekwencji.
# Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

seq_list = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
sums_result = [sum(seq) for seq in seq_list]
print("Zadanie 3.9 sumy:", sums_result)
assert sums_result == [0, 4, 3, 7, 18]


# ZADANIE 3.10
# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami
# I, V, X, L, C, D, M jako stringami) na liczby arabskie (podać kilka sposobów
# tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

# Sposób 1:
roman_dict_1 = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Sposób 2: Konstruktor dict ze słowami kluczowymi
roman_dict_2 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

# Sposób 3: Konstruktor dict() z listą krotek (klucz, wartość)
roman_dict_3 = dict([
    ("I", 1), ("V", 5), ("X", 10), ("L", 50),
    ("C", 100), ("D", 500), ("M", 1000)
])

# Sposób 4: Funkcja zip() parująca sekwencję symboli i sekwencję wartości
roman_dict_4 = dict(zip("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000]))

# Sposób 5: Wyrażenie słownikowe
roman_dict_5 = {r: v for r, v in zip("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000])}

# Sprawdzenie równoważności wszystkich sposobów:
assert roman_dict_1 == roman_dict_2 == roman_dict_3 == roman_dict_4 == roman_dict_5
print("Słownik rzymski:", roman_dict_1)

def roman2int(roman: str) -> int:
    """Tłumaczy całą liczbę w notacji rzymskiej na liczbę całkowitą (system arabski)."""
    roman_dict = roman_dict_1
    total = 0
    prev_val = 0
    # Iterujemy od prawej do lewej (od końca)
    for char in reversed(roman.upper()):
        val = roman_dict[char]
        if val < prev_val:
            total -= val
        else:
            total += val
            prev_val = val
    return total

print("MCMXCIV ->", roman2int("MCMXCIV"))
print("MMXXIV  ->", roman2int("MMXXIV"))

# Testy asercji dla funkcji roman2int
assert roman2int("I") == 1
assert roman2int("IV") == 4
assert roman2int("IX") == 9
assert roman2int("LVIII") == 58
assert roman2int("CDXLIV") == 444
assert roman2int("MCMXCIV") == 1994
assert roman2int("MMXXIV") == 2024
assert roman2int("MMMCMXCIX") == 3999

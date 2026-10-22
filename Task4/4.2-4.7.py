# ZADANIE 4.2
#
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.
#
# def make_ruler(n): pass
#
# def make_grid(rows, cols): pass

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


# ZADANIE 4.3
#
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
#
def factorial(n: int) -> int:
    total = 1;
    for i in range(1, n + 1):
        total *= i

    return total

fac = factorial(5)
# print(fac)
expected_fac = 120
assert fac == expected_fac
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(6) == 720

# ZADANIE 4.4
#
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
#
def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# ZADANIE 4.5
#
# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
#

def odwracanie(L: list, left: int, right: int) -> None:
    # [1, 3, 4, 5, 7]
    n = right - left + 1
    for i in range(n // 2):
        L[left + i], L[right - i] = L[right - i], L[left + i]

num = [1, 3, 4, 5, 7]
odwracanie(num, 1, 4)
print(num)
assert num == [1, 7, 5, 4, 3]

# ZADANIE 4.6
#
# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
#

def sum_seq(sequence: list) -> int:
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
            print(total)
        else:
            total += item
    return total

assert sum_seq([1, 2, 3, [4, 5, 6]]) == 21
assert sum_seq([1, 2, 3, [4, 5, [6, 7]]]) == 28

# ZADANIE 4.7
#
# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
#

def flatten(sequence: list) -> list:
    answer = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            for x in flatten(item):
                answer.append(x)
        else:
            answer.append(item)

    return answer

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]


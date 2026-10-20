# ZADANIE 2.10
# Mamy dany string wielowierszowy line. Podać sposób obliczenia liczby wyrazów w stringu. Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).
line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
words = len(line.split())
print(words)
assert words == 8
line = "Lorem ipsum\ndolor sit"
words = len(line.split())
print(words)
assert words == 4

# ZADANIE 2.11
# Podać sposób wyświetlania stringu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.
line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
word = "_".join(line)
print(word)
assert word == "L_o_r_e_m_ _i_p_s_u_m_ _d_o_l_o_r_ _s_i_t_ _a_m_e_t_,_ _c_o_n_s_e_c_t_e_t_u_r_ _a_d_i_p_i_s_c_i_n_g_ _e_l_i_t_."

# ZADANIE 2.12
# Zbudować string stworzony z pierwszych znaków wyrazów ze stringu line. Zbudować napis stworzony z ostatnich znaków wyrazów ze stringu line.
line = "Lorem ipsum"
helper = line.split()
word = "".join(word[0] for word in helper)
word2 = "".join(word[-1] for word in helper)

print(word, word2)
assert word == "Li"
assert word2 == "mm"

# ZADANIE 2.13
# Znaleźć łączną długość wyrazów w stringu line. Wskazówka: można skorzystać z funkcji sum().
line = "Lorem ipsum"
length = sum(len(word) for word in line.split())
print(length)
assert length == 10

# ZADANIE 2.14
# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w stringu line.
line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print(max(line.split(), key=len))
print(len(max(line.split(), key=len)))
assert max(line.split(), key=len) == "consectetur"
assert len(max(line.split(), key=len)) == 11

# ZADANIE 2.15
# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć string będący ciągiem cyfr kolejnych liczb z listy L.
L = [2, 3, 5, 7, 11, 13, 17, 19, 21]
answer = "".join(str(number) for number in L)
print(answer)
assert answer == "23571113171921"

# ZADANIE 2.16
# W tekście znajdującym się w stringu line zamienić ciąg znaków "GvR" na "Guido van Rossum".
line = "GvR is a Swedish programmer."
line = line.replace("GvR", "Guido van Rossum")
print(line)
assert line == "Guido van Rossum is a Swedish programmer."

# ZADANIE 2.17
# Posortować wyrazy ze stringu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().
line = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
sorted_alpha = sorted(line.split(), key=lambda x: x.lower())
sorted_length = sorted(line.split(), key=len)

print(sorted_alpha)
print(sorted_length)
assert sorted_alpha == ["adipiscing", "amet", "consectetur", "dolor", "elit", "ipsum", "Lorem", "sit"]
assert sorted_length == ['sit', 'amet', 'elit', 'Lorem', 'ipsum', 'dolor', 'adipiscing', 'consectetur']

# ZADANIE 2.18
# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na string.
number = 6700076
zeros = str(number).count("0")
print(zeros)
assert zeros == 3

# ZADANIE 2.19
# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować string z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().
L = [123, 456, 789, 10, 15, 67, 1, 8, 7]
answer = "\n".join(str(number).zfill(3) for number in L)
print(answer)

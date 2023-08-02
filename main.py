def find_consecutive_chars(s):
    previous_char = ""
    for char in s:
        if char == previous_char:
            print(char, end="")
        previous_char = char

s = "C++ ni muvaffaqiyatli"
find_consecutive_chars(s)
def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    
    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in matrix:
            matrix.append(ch)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]
        else:
            b = "X"

        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2

    return result


def encrypt_playfair(text, matrix):
    cipher = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


key = input("Enter key: ")
text = input("Enter plaintext: ")

matrix = create_matrix(key)

print("\nPlayfair Matrix:")
for row in matrix:
    print(row)

text = prepare_text(text)

cipher = encrypt_playfair(text, matrix)

print("Prepared text:", text)
print("Encrypted text:", cipher)

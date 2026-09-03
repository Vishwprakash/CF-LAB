import numpy as np

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")

    if len(text) % 2 != 0:
        text += "X"

    cipher = ""

    for i in range(0, len(text), 2):
        p1 = ord(text[i]) - ord('A')
        p2 = ord(text[i + 1]) - ord('A')

        p = np.array([[p1], [p2]])

        c = np.dot(key, p) % 26

        cipher += chr(int(c[0][0]) + ord('A'))
        cipher += chr(int(c[1][0]) + ord('A'))

    return cipher


def hill_decrypt(text, key):
    det = int(round(np.linalg.det(key))) % 26
    det_inverse = pow(det, -1, 26)

    inverse_key = np.array([
        [key[1][1], -key[0][1]],
        [-key[1][0], key[0][0]]
    ])

    inverse_key = (det_inverse * inverse_key) % 26

    plain = ""

    for i in range(0, len(text), 2):
        c1 = ord(text[i]) - ord('A')
        c2 = ord(text[i + 1]) - ord('A')

        c = np.array([[c1], [c2]])

        p = np.dot(inverse_key, c) % 26

        plain += chr(int(p[0][0]) + ord('A'))
        plain += chr(int(p[1][0]) + ord('A'))

    if len(plain) % 2 != 0:
        plain = plain[:-1]

    return plain


key = np.array([[3, 3],
                [2, 5]])

text = input("Enter plaintext: ")

cipher = hill_encrypt(text, key)

print("Encrypted text:", cipher)

plain = hill_decrypt(cipher, key)

print("Decrypted text:", plain)

def Encryption(p, k):
    output = ""

    for char in p:
        if char.isalpha():
            if char.isupper():
                output += chr((ord(char) - ord('A')) * k % 26 + ord('A'))
            else:
                output += chr((ord(char) - ord('a')) * k % 26 + ord('a'))
        else:
            output += char

    return output


def Decryption(c, k):
    output = ""

    # Find multiplicative inverse of k
    for i in range(26):
        if (k * i) % 26 == 1:
            inverse = i
            break

    output = ""

    for char in c:
        if char.isalpha():
            if char.isupper():
                output += chr((ord(char) - ord('A')) * inverse % 26 + ord('A'))
            else:
                output += chr((ord(char) - ord('a')) * inverse % 26 + ord('a'))
        else:
            output += char

    return output


plaintext = input('Enter plain text : ')
key = int(input('Enter the key value : '))

result1 = Encryption(plaintext, key)
result2 = Decryption(result1, key)

print('Cipher text : ', result1)
print('Plain text : ', result2)

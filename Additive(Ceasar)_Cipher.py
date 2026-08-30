def Encryption(p, k):
    output = ""

    for char in p:
        if char.isalpha():
            if char.isupper():
                output += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            else:
                output += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            output += char

    return output


def Decryption(p, k):
    output = ""

    for char in p:
        if char.isalpha():
            if char.isupper():
                output += chr((ord(char) - ord('A') - k) % 26 + ord('A'))
            else:
                output += chr((ord(char) - ord('a') - k) % 26 + ord('a'))
        else:
            output += char

    return output


plaintext = input('Enter plain text : ')
key = int(input('Enter the key value : '))

result1 = Encryption(plaintext, key)
result2 = Decryption(result1, key)

print('cipher text : ', result1)
print('plain text : ', result2)

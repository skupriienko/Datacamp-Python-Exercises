alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text, key):

    encrypted_text = ''

    # Fill in the blanks to create an encrypted text
    for char in text.lower():
        idx = (alphabet.index(char) + key) % len(alphabet)
        encrypted_text = encrypted_text + alphabet[idx]

    return encrypted_text

# Check the encryption function with the shift equals to 10
print(encrypt("datacamp", 10))

#decription
# idx = alphabet.index(char) - key

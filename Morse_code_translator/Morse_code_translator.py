user_input = input("Enter your text: ").lower()
morse_code = ""

alphabet = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": ".-",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}

for idx in range(len(user_input)):
    if user_input[idx] in alphabet:
        morse_code += alphabet[user_input[idx]]
    else:
        print(f"'{user_input[idx]}' is not a valid symbol!")
        exit()
print(morse_code)

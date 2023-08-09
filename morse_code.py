morse_code = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-.": "k", ".-..": "l", "--": "m", "-.":"n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-":"t", "..-":"u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": 'z' }

while True:
    word = input("What is the morse code in (- and .) ")
    if word.strip():
        break
    else:
        print("Please enter a non-empty string.")

transcribe = word.split(" ")
english = []
for i in transcribe:
    if i in morse_code.keys():
        english.append(morse_code[i])
answer = " ".join(english)
print(answer)

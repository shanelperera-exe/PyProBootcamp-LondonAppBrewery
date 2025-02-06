MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def main():
    print("Mose Code Converter\n")
    print("MAIN MENU")
    print("-" * 9)
    print("[1] Text-to-Morse code")
    print("[2] Morse code-to-Text")
    print("[3] Exit\n")

    while True:
        try:
            choice = int(input("Enter Option: ").strip())
            if choice not in [1, 2, 3]:
                print("Invalid option. Please enter a valid option.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid option.")

    match choice:
        case 1:
            text_to_morse()
        case 2:
            morse_to_text()
        case 3:
            exit()
        case _:
            print("Enter a valid Input.")


def text_to_morse():
    text = input("Enter text: ").strip().upper()
    
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append(' ')

    print(' '.join(morse_code))

def morse_to_text():
    morse_code = input("Enter Morse code: ").strip().split(" ")
    text = ""
    for char in morse_code:
        if char == "":
            text += " "
        else:
            for key, value in MORSE_CODE_DICT.items():
                if value == char:
                    text += key
                    break
    print(text.title())

if __name__ == "__main__":
    main()
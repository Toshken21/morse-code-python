def morsecode():
    my_string = input("Enter a string: ")
    my_string = my_string.upper()
    morse_string = ""
    accumulator = 0
    for r in my_string:
        chara = my_string[accumulator]
        if chara == " ":
            morse_string += " "
        elif chara == ",":
            morse_string += "--..--"
        elif chara == ".":
            morse_string += ".-.-.-"
        elif chara == "?":
            morse_string += "..--.."
        elif chara == "0":
            morse_string += "-----"
        elif chara == "1":
            morse_string += ".----"
        elif chara == "2":
            morse_string += "..---"
        elif chara == "3":
            morse_string += "...--"
        elif chara == "4":
            morse_string += "....-"
        elif chara == "5":
            morse_string += "....."
        elif chara == "6":
            morse_string += "-...."
        elif chara == "7":
            morse_string += "--..."
        elif chara == "8":
            morse_string += "---.."
        elif chara == "9":
            morse_string += "----."
        elif chara == "A":
            morse_string += ".-"
        elif chara == "B":
            morse_string += "-..."
        elif  chara == "C":
            morse_string += "-.-."
        elif chara == "D":
            morse_string += "-.."
        elif chara == "E":
            morse_string += "."
        elif chara == "F":
            morse_string += "..-."
        elif chara == "G":
            morse_string += "--."
        elif chara == "H":
            morse_string += "...."
        elif chara == "I":
            morse_string += ".."
        elif chara == "J":
            morse_string += ".---"
        elif chara == "K":
            morse_string += "-.-"
        elif chara == "L":
            morse_string += ".-.."
        elif chara == "M":
            morse_string += "--"
        elif chara == "N":
            morse_string += "-."
        elif chara == "0":
            morse_string += "---"
        elif chara == "P":
            morse_string += ".--."
        elif chara == "Q":
            morse_string += "--.-"
        elif chara == "R":
            morse_string += ".-."
        elif chara == "S":
            morse_string += "..."
        elif chara == "T":
            morse_string += "-"
        elif chara == "U":
            morse_string += "..-"
        elif chara == "V":
            morse_string += "...-"
        elif chara == "W":
            morse_string += ".--"
        elif chara == "X":
            morse_string += "-..-"
        elif chara == "Y":
            morse_string += "-.-"
        elif chara == "Z":
            morse_string += "--.."

        accumulator += 1
    print(morse_string)
morsecode()

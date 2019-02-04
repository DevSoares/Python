TO_MORSE_DICT = {
    ' ' : ' ',
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm' : '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-',
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..'
}

FROM_MORSE_DICT = {value: key for key, value in TO_MORSE_DICT.items()}

mensagem = 'Uma mensagem qualquer'

msgCriptL = [TO_MORSE_DICT[char.lower()] for char in mensagem]

msgDeCriptL = [FROM_MORSE_DICT[char.lower()] for char in msgCriptL]

msgCriptString = ''.join(msgCriptL)

msgDeCriptString = ''.join(msgDeCriptL)

print(msgCriptString)
print(msgDeCriptString)

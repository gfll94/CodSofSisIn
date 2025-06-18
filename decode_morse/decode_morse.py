from preloaded import MORSE_CODE

def decode_morse(morse_code):
    words = morse_code.strip().split('   ')
    res = []
    for word in words:
        letters = word.split(' ')
        dword = ''.join(MORSE_CODE.get(letter, '') for letter in letters)
        res.append(dword)
    return ' '.join(res)
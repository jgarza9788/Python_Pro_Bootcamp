#morse code

alpha_to_morse = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '0':'-----',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
}
morse_to_alpha = { v:k for (k,v) in alpha_to_morse.items() }

def is_alpha(string):
    len0 = len(string)
    string = string.replace('-','').replace('.','').replace(' ','')
    len1 = len(string)

    if len1/len0 > 0.1:
        return True
    else:
        return False

def convert_0(string, lu_dict):
    result = ''
    for w in string.split(' '):
        for l in w:
            result += lu_dict.get(l.upper(), ' ') + ' '
        result += ' '*5

    return result

def convert(string):
    if is_alpha(string):
        return convert_0(string,alpha_to_morse)
    else:
        return convert_0(string,morse_to_alpha)

def main():
    print('morse_code\n',convert('morse_code'))
    print('Just Type, Below\n', convert('Just Type, Below'))
    print()

    while True:
        x = input('')
        print(convert(x))


if __name__ == '__main__':
    main()
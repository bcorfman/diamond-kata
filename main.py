ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def diamond(letter):
    if not letter:
        return ''
    widest = letter.upper()
    idx = ALPHABET.find(widest)
    if idx < 0:
        raise SyntaxError('Unrecognized letter as input')
    indices = list(range(idx+1)) + list(range(idx-1, -1, -1))
    output = ''
    for i in indices:
        leading_spaces = ' ' * (idx - i)
        output += leading_spaces + ALPHABET[i]
        num_chars = min(i + 1, 2)
        if num_chars > 1:
            output += ' ' * ((i - 1) * 2 + 1) + ALPHABET[i] 
        output += '\n'
    return output


if __name__ == '__main__':
    print(diamond('f'))

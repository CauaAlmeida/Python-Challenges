def main():
    lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
    sentence = input('Type what you would like translated into nagi-latin and press ENTER: ')
    sentence = sentence.split()
    for k in range(len(sentence)):
        i = sentence[k]
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            sentence[k] = i + 'nagi'
        elif t(i) in lst:
            sentence[k] = i[2:] + i[:2] + 'nyagi'
        elif not i.isalpha():
            sentence[k] = i
        else:
            sentence[k] = i[1:] + i[0] + 'nyannyagi'
    return ' '.join(sentence)


def t(string):
    return string[0] + string[1]


if __name__ == "__main__":
    x = main()
    print(x)

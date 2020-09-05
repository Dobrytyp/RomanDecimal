from django.shortcuts import render


def Roman_to_Decimal(a):
    text = []
    atext = []

    for i in a:
        text.append(i)

    while len(text) > 1:
        if text[0] == 'M':
            atext.append(1000)
            text.remove(text[0])
        elif text[0] == 'C' and text[1] == 'M':
            atext.append(900)
            text.remove(text[0])
            text.remove(text[0])
        elif text[0] == 'D':
            atext.append(500)
            text.remove(text[0])
        elif text[0] == 'C' and text[1] == 'D':
            atext.append(400)
            text.remove(text[0])
            text.remove(text[0])
        elif text[0] == 'C':
            atext.append(100)
            text.remove(text[0])
        elif text[0] == 'X' and text[1] == 'C':
            atext.append(90)
            text.remove(text[0])
            text.remove(text[0])
        elif text[0] == 'L':
            atext.append(50)
            text.remove(text[0])
        elif text[0] == 'X' and text[1] == 'L':
            atext.append(40)
            text.remove(text[0])
            text.remove(text[0])
        elif text[0] == 'X':
            atext.append(10)
            text.remove(text[0])
        elif text[0] == 'I' and text[1] == 'X':
            atext.append(9)
            text.remove(text[0])
            text.remove(text[0])
        elif text[0] == 'V':
            atext.append(5)
            text.remove(text[0])
        elif text[0] == 'I' and text[1] == 'V':
            atext.append(4)
            text.remove(text[0])
            text.remove(text[0])
        elif text[0] == 'I':
            atext.append(1)
            text.remove(text[0])

    while len(text) > 0:
        if text[0] == 'M':
            atext.append(1000)
            text.remove(text[0])
        elif text[0] == 'D':
            atext.append(500)
            text.remove(text[0])
        elif text[0] == 'C':
            atext.append(100)
            text.remove(text[0])
        elif text[0] == 'L':
            atext.append(50)
            text.remove(text[0])
        elif text[0] == 'X':
            atext.append(10)
            text.remove(text[0])
        elif text[0] == 'V':
            atext.append(5)
            text.remove(text[0])
        elif text[0] == 'I':
            atext.append(1)
            text.remove(text[0])
    return sum(atext)

a = input()
print(Roman_to_Decimal(a))


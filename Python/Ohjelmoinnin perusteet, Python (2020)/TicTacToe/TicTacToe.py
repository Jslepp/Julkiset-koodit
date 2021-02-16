import random
a = "-"
b = "-"
c = "-"
d = "-"
e = "-"
f = "-"
g = "-"
h = "-"
i = "-"
def pelialusta(): 
    print(a, b, c, d, e, f, g, h, i)

def tarkista():
    if a == "x" and b == "x" and c == "x":
        print("Voitit pelin")
        pelialusta()
        exit()
    if a == "o" and b == "o" and c == "o":
        print("Hävisit pelin")
        pelialusta()
        exit()
    if b == "x" and c == "x" and d == "x":
        print("Voitit pelin")
        pelialusta()
        exit()
    if b == "o" and c == "o" and d == "o":
        print("Hävisit pelin")
        pelialusta()
        exit()
    if c == "x" and d == "x" and e == "x":
        print("Voitit pelin")
        pelialusta()
        exit()
    if c == "o" and d == "o" and e == "o":
        print("Hävisit pelin")
        pelialusta()
        exit()
    if d == "x" and e == "x" and f == "x":
        print("Voitit pelin")
        pelialusta()
        exit()
    if d == "o" and e == "o" and f == "o":
        print("Hävisit pelin")
        pelialusta()
        exit()
    if e == "x" and f == "x" and g == "x":
        print("Voitit pelin")
        pelialusta()
        exit()
    if e == "o" and f == "o" and g == "o":
        print("Hävisit pelin")
        pelialusta()
        exit()
    if f == "x" and g == "x" and h == "x":
        print("Voitit pelin")
        pelialusta()
        exit()
    if f == "o" and g == "o" and h == "o":
        print("Hävisit pelin")
        pelialusta()
        exit()
    if g == "x" and h == "x" and i == "x":
        print("Voitit pelin")
        pelialusta()
        exit()
    if g == "o" and h == "o" and i == "o":
        print("Hävisit pelin")
        pelialusta()
        exit()

pelialusta()
aloitus = random.randint(0,1)
if aloitus == 1:
    vuoro = input()
    if vuoro == "x - - - - - - - -":
        a = "x"
    if vuoro == "- x - - - - - - -":
        b = "x"
    if vuoro == "- - x - - - - - -":
        c = "x"
    if vuoro == "- - - x - - - - -":
        d = "x"
    if vuoro == "- - - - x - - - -":
        e = "x"
    if vuoro == "- - - - - x - - -":
        f = "x"
    if vuoro == "- - - - - - x - -":
        g = "x"
    if vuoro == "- - - - - - - x -":
        h = "x"
    if vuoro == "- - - - - - - - x":
        i = "x"
    tarkista()

    vastustaja = 1
    while vastustaja == 1:
        vastustajanvuoro = random.randint(1,9)
        if vastustajanvuoro == 1:
            if a == "x" or a == "o":
                vastustaja = 1
            else:
                a = "o"
                vastustaja += 1
        if vastustajanvuoro == 2:
            if b == "x" or b == "o":
                vastustaja = 1
            else:
                b = "o"
                vastustaja += 1
        if vastustajanvuoro == 3:
            if c == "x" or c == "o":
                vastustaja = 1
            else:
                c = "o"
                vastustaja += 1
        if vastustajanvuoro == 4:
            if d == "x" or d == "o":
                vastustaja = 1
            else:
                d = "o"
                vastustaja += 1
        if vastustajanvuoro == 5:
            if e == "x" or e == "o":
                vastustaja = 1
            else:
                e = "o"
                vastustaja += 1
        if vastustajanvuoro == 6:
            if f == "x" or f == "o":
                vastustaja = 1
            else:
                f = "o"
                vastustaja += 1
        if vastustajanvuoro == 7:
            if g == "x" or g == "o":
                vastustaja = 1
            else:
                g = "o"
                vastustaja += 1
        if vastustajanvuoro == 8:
            if h == "x" or h == "o":
                vastustaja = 1
            else:
                h = "o"
                vastustaja += 1
        if vastustajanvuoro == 9:
            if i == "x" or i == "o":
                vastustaja = 1
            else:
                i = "o"
                vastustaja += 1
    tarkista()

    pelialusta()

    vuoro = input()
    if vuoro == "x - - - - - - - -":
        a = "x"
    if vuoro == "- x - - - - - - -":
        b = "x"
    if vuoro == "- - x - - - - - -":
        c = "x"
    if vuoro == "- - - x - - - - -":
        d = "x"
    if vuoro == "- - - - x - - - -":
        e = "x"
    if vuoro == "- - - - - x - - -":
        f = "x"
    if vuoro == "- - - - - - x - -":
        g = "x"
    if vuoro == "- - - - - - - x -":
        h = "x"
    if vuoro == "- - - - - - - - x":
        i = "x"
    tarkista()    

    vastustaja = 1
    while vastustaja == 1:
        vastustajanvuoro = random.randint(1,9)
        if vastustajanvuoro == 1:
            if a == "x" or a == "o":
                vastustaja = 1
            else:
                a = "o"
                vastustaja += 1
        if vastustajanvuoro == 2:
            if b == "x" or b == "o":
                vastustaja = 1
            else:
                b = "o"
                vastustaja += 1
        if vastustajanvuoro == 3:
            if c == "x" or c == "o":
                vastustaja = 1
            else:
                c = "o"
                vastustaja += 1
        if vastustajanvuoro == 4:
            if d == "x" or d == "o":
                vastustaja = 1
            else:
                d = "o"
                vastustaja += 1
        if vastustajanvuoro == 5:
            if e == "x" or e == "o":
                vastustaja = 1
            else:
                e = "o"
                vastustaja += 1
        if vastustajanvuoro == 6:
            if f == "x" or f == "o":
                vastustaja = 1
            else:
                f = "o"
                vastustaja += 1
        if vastustajanvuoro == 7:
            if g == "x" or g == "o":
                vastustaja = 1
            else:
                g = "o"
                vastustaja += 1
        if vastustajanvuoro == 8:
            if h == "x" or h == "o":
                vastustaja = 1
            else:
                h = "o"
                vastustaja += 1
        if vastustajanvuoro == 9:
            if i == "x" or i == "o":
                vastustaja = 1
            else:
                i = "o"
                vastustaja += 1
    tarkista()

    pelialusta()

    vuoro = input()
    if vuoro == "x - - - - - - - -":
        a = "x"
    if vuoro == "- x - - - - - - -":
        b = "x"
    if vuoro == "- - x - - - - - -":
        c = "x"
    if vuoro == "- - - x - - - - -":
        d = "x"
    if vuoro == "- - - - x - - - -":
        e = "x"
    if vuoro == "- - - - - x - - -":
        f = "x"
    if vuoro == "- - - - - - x - -":
        g = "x"
    if vuoro == "- - - - - - - x -":
        h = "x"
    if vuoro == "- - - - - - - - x":
        i = "x"
    tarkista()

    vastustaja = 1
    while vastustaja == 1:
        vastustajanvuoro = random.randint(1,9)
        if vastustajanvuoro == 1:
            if a == "x" or a == "o":
                vastustaja = 1
            else:
                a = "o"
                vastustaja += 1
        if vastustajanvuoro == 2:
            if b == "x" or b == "o":
                vastustaja = 1
            else:
                b = "o"
                vastustaja += 1
        if vastustajanvuoro == 3:
            if c == "x" or c == "o":
                vastustaja = 1
            else:
                c = "o"
                vastustaja += 1
        if vastustajanvuoro == 4:
            if d == "x" or d == "o":
                vastustaja = 1
            else:
                d = "o"
                vastustaja += 1
        if vastustajanvuoro == 5:
            if e == "x" or e == "o":
                vastustaja = 1
            else:
                e = "o"
                vastustaja += 1
        if vastustajanvuoro == 6:
            if f == "x" or f == "o":
                vastustaja = 1
            else:
                f = "o"
                vastustaja += 1
        if vastustajanvuoro == 7:
            if g == "x" or g == "o":
                vastustaja = 1
            else:
                g = "o"
                vastustaja += 1
        if vastustajanvuoro == 8:
            if h == "x" or h == "o":
                vastustaja = 1
            else:
                h = "o"
                vastustaja += 1
        if vastustajanvuoro == 9:
            if i == "x" or i == "o":
                vastustaja = 1
            else:
                i = "o"
                vastustaja += 1
    tarkista()

    pelialusta()

    vuoro = input()
    if vuoro == "x - - - - - - - -":
        a = "x"
    if vuoro == "- x - - - - - - -":
        b = "x"
    if vuoro == "- - x - - - - - -":
        c = "x"
    if vuoro == "- - - x - - - - -":
        d = "x"
    if vuoro == "- - - - x - - - -":
        e = "x"
    if vuoro == "- - - - - x - - -":
        f = "x"
    if vuoro == "- - - - - - x - -":
        g = "x"
    if vuoro == "- - - - - - - x -":
        h = "x"
    if vuoro == "- - - - - - - - x":
        i = "x"
    tarkista()

    vastustaja = 1
    while vastustaja == 1:
        vastustajanvuoro = random.randint(1,9)
        if vastustajanvuoro == 1:
            if a == "x" or a == "o":
                vastustaja = 1
            else:
                a = "o"
                vastustaja += 1
        if vastustajanvuoro == 2:
            if b == "x" or b == "o":
                vastustaja = 1
            else:
                b = "o"
                vastustaja += 1
        if vastustajanvuoro == 3:
            if c == "x" or c == "o":
                vastustaja = 1
            else:
                c = "o"
                vastustaja += 1
        if vastustajanvuoro == 4:
            if d == "x" or d == "o":
                vastustaja = 1
            else:
                d = "o"
                vastustaja += 1
        if vastustajanvuoro == 5:
            if e == "x" or e == "o":
                vastustaja = 1
            else:
                e = "o"
                vastustaja += 1
        if vastustajanvuoro == 6:
            if f == "x" or f == "o":
                vastustaja = 1
            else:
                f = "o"
                vastustaja += 1
        if vastustajanvuoro == 7:
            if g == "x" or g == "o":
                vastustaja = 1
            else:
                g = "o"
                vastustaja += 1
        if vastustajanvuoro == 8:
            if h == "x" or h == "o":
                vastustaja = 1
            else:
                h = "o"
                vastustaja += 1
        if vastustajanvuoro == 9:
            if i == "x" or i == "o":
                vastustaja = 1
            else:
                i = "o"
                vastustaja += 1
    tarkista()

    pelialusta()

    vuoro = input()
    if vuoro == "x - - - - - - - -":
        a = "x"
    if vuoro == "- x - - - - - - -":
        b = "x"
    if vuoro == "- - x - - - - - -":
        c = "x"
    if vuoro == "- - - x - - - - -":
        d = "x"
    if vuoro == "- - - - x - - - -":
        e = "x"
    if vuoro == "- - - - - x - - -":
        f = "x"
    if vuoro == "- - - - - - x - -":
        g = "x"
    if vuoro == "- - - - - - - x -":
        h = "x"
    if vuoro == "- - - - - - - - x":
        i = "x"
    tarkista()

if aloitus == 0:
    #Vastustajanvuoro
    vastustaja = 1
    while vastustaja == 1:
        vastustajanvuoro = random.randint(1,9)
        if vastustajanvuoro == 1:
            if a == "x" or a == "o":
                vastustaja = 1
            else:
                a = "o"
                vastustaja += 1
        if vastustajanvuoro == 2:
            if b == "x" or b == "o":
                vastustaja = 1
            else:
                b = "o"
                vastustaja += 1
        if vastustajanvuoro == 3:
            if c == "x" or c == "o":
                vastustaja = 1
            else:
                c = "o"
                vastustaja += 1
        if vastustajanvuoro == 4:
            if d == "x" or d == "o":
                vastustaja = 1
            else:
                d = "o"
                vastustaja += 1
        if vastustajanvuoro == 5:
            if e == "x" or e == "o":
                vastustaja = 1
            else:
                e = "o"
                vastustaja += 1
        if vastustajanvuoro == 6:
            if f == "x" or f == "o":
                vastustaja = 1
            else:
                f = "o"
                vastustaja += 1
        if vastustajanvuoro == 7:
            if g == "x" or g == "o":
                vastustaja = 1
            else:
                g = "o"
                vastustaja += 1
        if vastustajanvuoro == 8:
            if h == "x" or h == "o":
                vastustaja = 1
            else:
                h = "o"
                vastustaja += 1
        if vastustajanvuoro == 9:
            if i == "x" or i == "o":
                vastustaja = 1
            else:
                i = "o"
                vastustaja += 1
    tarkista()

    pelialusta()
    
    vuoro = input()
    if vuoro == "x - - - - - - - -":
        a = "x"
    if vuoro == "- x - - - - - - -":
        b = "x"
    if vuoro == "- - x - - - - - -":
        c = "x"
    if vuoro == "- - - x - - - - -":
        d = "x"
    if vuoro == "- - - - x - - - -":
        e = "x"
    if vuoro == "- - - - - x - - -":
        f = "x"
    if vuoro == "- - - - - - x - -":
        g = "x"
    if vuoro == "- - - - - - - x -":
        h = "x"
    if vuoro == "- - - - - - - - x":
        i = "x"
    tarkista()

    vastustaja = 1
    while vastustaja == 1:
        vastustajanvuoro = random.randint(1,9)
        if vastustajanvuoro == 1:
            if a == "x" or a == "o":
                vastustaja = 1
            else:
                a = "o"
                vastustaja += 1
        if vastustajanvuoro == 2:
            if b == "x" or b == "o":
                vastustaja = 1
            else:
                b = "o"
                vastustaja += 1
        if vastustajanvuoro == 3:
            if c == "x" or c == "o":
                vastustaja = 1
            else:
                c = "o"
                vastustaja += 1
        if vastustajanvuoro == 4:
            if d == "x" or d == "o":
                vastustaja = 1
            else:
                d = "o"
                vastustaja += 1
        if vastustajanvuoro == 5:
            if e == "x" or e == "o":
                vastustaja = 1
            else:
                e = "o"
                vastustaja += 1
        if vastustajanvuoro == 6:
            if f == "x" or f == "o":
                vastustaja = 1
            else:
                f = "o"
                vastustaja += 1
        if vastustajanvuoro == 7:
            if g == "x" or g == "o":
                vastustaja = 1
            else:
                g = "o"
                vastustaja += 1
        if vastustajanvuoro == 8:
            if h == "x" or h == "o":
                vastustaja = 1
            else:
                h = "o"
                vastustaja += 1
        if vastustajanvuoro == 9:
            if i == "x" or i == "o":
                vastustaja = 1
            else:
                i = "o"
                vastustaja += 1
    tarkista()

    pelialusta()

    vuoro = input()
    if vuoro == "x - - - - - - - -":
        a = "x"
    if vuoro == "- x - - - - - - -":
        b = "x"
    if vuoro == "- - x - - - - - -":
        c = "x"
    if vuoro == "- - - x - - - - -":
        d = "x"
    if vuoro == "- - - - x - - - -":
        e = "x"
    if vuoro == "- - - - - x - - -":
        f = "x"
    if vuoro == "- - - - - - x - -":
        g = "x"
    if vuoro == "- - - - - - - x -":
        h = "x"
    if vuoro == "- - - - - - - - x":
        i = "x"
    tarkista()

    vastustaja = 1
    while vastustaja == 1:
        vastustajanvuoro = random.randint(1,9)
        if vastustajanvuoro == 1:
            if a == "x" or a == "o":
                vastustaja = 1
            else:
                a = "o"
                vastustaja += 1
        if vastustajanvuoro == 2:
            if b == "x" or b == "o":
                vastustaja = 1
            else:
                b = "o"
                vastustaja += 1
        if vastustajanvuoro == 3:
            if c == "x" or c == "o":
                vastustaja = 1
            else:
                c = "o"
                vastustaja += 1
        if vastustajanvuoro == 4:
            if d == "x" or d == "o":
                vastustaja = 1
            else:
                d = "o"
                vastustaja += 1
        if vastustajanvuoro == 5:
            if e == "x" or e == "o":
                vastustaja = 1
            else:
                e = "o"
                vastustaja += 1
        if vastustajanvuoro == 6:
            if f == "x" or f == "o":
                vastustaja = 1
            else:
                f = "o"
                vastustaja += 1
        if vastustajanvuoro == 7:
            if g == "x" or g == "o":
                vastustaja = 1
            else:
                g = "o"
                vastustaja += 1
        if vastustajanvuoro == 8:
            if h == "x" or h == "o":
                vastustaja = 1
            else:
                h = "o"
                vastustaja += 1
        if vastustajanvuoro == 9:
            if i == "x" or i == "o":
                vastustaja = 1
            else:
                i = "o"
                vastustaja += 1
    tarkista()

    pelialusta()

    vuoro = input()
    if vuoro == "x - - - - - - - -":
        a = "x"
    if vuoro == "- x - - - - - - -":
        b = "x"
    if vuoro == "- - x - - - - - -":
        c = "x"
    if vuoro == "- - - x - - - - -":
        d = "x"
    if vuoro == "- - - - x - - - -":
        e = "x"
    if vuoro == "- - - - - x - - -":
        f = "x"
    if vuoro == "- - - - - - x - -":
        g = "x"
    if vuoro == "- - - - - - - x -":
        h = "x"
    if vuoro == "- - - - - - - - x":
        i = "x"
    tarkista()

    vastustaja = 1
    while vastustaja == 1:
        vastustajanvuoro = random.randint(1,9)
        if vastustajanvuoro == 1:
            if a == "x" or a == "o":
                vastustaja = 1
            else:
                a = "o"
                vastustaja += 1
        if vastustajanvuoro == 2:
            if b == "x" or b == "o":
                vastustaja = 1
            else:
                b = "o"
                vastustaja += 1
        if vastustajanvuoro == 3:
            if c == "x" or c == "o":
                vastustaja = 1
            else:
                c = "o"
                vastustaja += 1
        if vastustajanvuoro == 4:
            if d == "x" or d == "o":
                vastustaja = 1
            else:
                d = "o"
                vastustaja += 1
        if vastustajanvuoro == 5:
            if e == "x" or e == "o":
                vastustaja = 1
            else:
                e = "o"
                vastustaja += 1
        if vastustajanvuoro == 6:
            if f == "x" or f == "o":
                vastustaja = 1
            else:
                f = "o"
                vastustaja += 1
        if vastustajanvuoro == 7:
            if g == "x" or g == "o":
                vastustaja = 1
            else:
                g = "o"
                vastustaja += 1
        if vastustajanvuoro == 8:
            if h == "x" or h == "o":
                vastustaja = 1
            else:
                h = "o"
                vastustaja += 1
        if vastustajanvuoro == 9:
            if i == "x" or i == "o":
                vastustaja = 1
            else:
                i = "o"
                vastustaja += 1
    tarkista()

    pelialusta()

    vuoro = input()
    if vuoro == "x - - - - - - - -":
        a = "x"
    if vuoro == "- x - - - - - - -":
        b = "x"
    if vuoro == "- - x - - - - - -":
        c = "x"
    if vuoro == "- - - x - - - - -":
        d = "x"
    if vuoro == "- - - - x - - - -":
        e = "x"
    if vuoro == "- - - - - x - - -":
        f = "x"
    if vuoro == "- - - - - - x - -":
        g = "x"
    if vuoro == "- - - - - - - x -":
        h = "x"
    if vuoro == "- - - - - - - - x":
        i = "x"
    tarkista()

    vastustaja = 1
    while vastustaja == 1:
        vastustajanvuoro = random.randint(1,9)
        if vastustajanvuoro == 1:
            if a == "x" or a == "o":
                vastustaja = 1
            else:
                a = "o"
                vastustaja += 1
        if vastustajanvuoro == 2:
            if b == "x" or b == "o":
                vastustaja = 1
            else:
                b = "o"
                vastustaja += 1
        if vastustajanvuoro == 3:
            if c == "x" or c == "o":
                vastustaja = 1
            else:
                c = "o"
                vastustaja += 1
        if vastustajanvuoro == 4:
            if d == "x" or d == "o":
                vastustaja = 1
            else:
                d = "o"
                vastustaja += 1
        if vastustajanvuoro == 5:
            if e == "x" or e == "o":
                vastustaja = 1
            else:
                e = "o"
                vastustaja += 1
        if vastustajanvuoro == 6:
            if f == "x" or f == "o":
                vastustaja = 1
            else:
                f = "o"
                vastustaja += 1
        if vastustajanvuoro == 7:
            if g == "x" or g == "o":
                vastustaja = 1
            else:
                g = "o"
                vastustaja += 1
        if vastustajanvuoro == 8:
            if h == "x" or h == "o":
                vastustaja = 1
            else:
                h = "o"
                vastustaja += 1
        if vastustajanvuoro == 9:
            if i == "x" or i == "o":
                vastustaja = 1
            else:
                i = "o"
                vastustaja += 1
    tarkista()

    pelialusta()
print("Tasapeli")
pelialusta()
exit()
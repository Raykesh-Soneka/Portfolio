import string,secrets

__debug = False
Lettre = string.ascii_letters
Espace = string.whitespace
nombre = string.digits
hexa = string.hexdigits
octa = string.octdigits
ponctuation = string.punctuation
tout = string.printable
if __debug:
    print(string.__doc__)
    print([print('['+s+']') for s in [Lettre, Espace, nombre, hexa, octa, ponctuation, tout]])

Charset : string = tout


if __debug:
    print(Charset)

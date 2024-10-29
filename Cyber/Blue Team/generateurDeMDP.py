import string,secrets

__debug = True
Lettre = string.ascii_letters
Espace = string.whitespace
nombre = string.digits
hexa = string.hexdigits
octa = string.octdigits
ponctuation = string.punctuation
tout = string.printable
if __debug:
    ___debug : int = 10 # Niveau de debogage
    print(string.__doc__)
    if ___debug > 8 :
        def __debug_f( s : string ) -> string :print('['+s+']');return s
        print([__debug_f(s) for s in [Lettre, Espace, nombre, hexa, octa, ponctuation, tout]])

Charset : string = tout


if __debug:
    if ___debug > 4 :
        print(Charset)

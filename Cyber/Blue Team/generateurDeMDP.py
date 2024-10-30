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
    ___debug : int = 5 # Niveau de debogage ___debug ∈ [0 ; 10]
    if ___debug > 9 :print(string.__doc__)
    if ___debug > 8 :
        def __debug_f( s : string ) -> string :print('['+s+']');return s
        print([__debug_f(s) for s in [Lettre, Espace, nombre, hexa, octa, ponctuation, tout]])

Charset : string = tout
if __debug and ___debug > 8:print(len(Charset))
#ici le charset est plutôt court (100 caractères)
#Il faut modifier le code pour pouvoir avoir un plus grand charset (avec utf8 mais ces caractère ne sont pas pris TOUJOURS en charge)

def generateurDeMotsDePasse(n : int = 0 ) -> None:
    while n is None or n == 0:
        int(input(" Entrer le Nombre de caractère (longueur) pour génèré un mots de passe : "))




if __debug:
    if ___debug > 7 :
        print(Charset)

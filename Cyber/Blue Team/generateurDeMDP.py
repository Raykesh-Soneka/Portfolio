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

# Charset : string = tout
Charset : string = Lettre + nombre + ponctuation
if __debug and ___debug > 8:print(len(Charset))
#ici le charset est plutôt court (100 caractères)
#Il faut modifier le code pour pouvoir avoir un plus grand charset (avec utf8 mais ces caractère ne sont pas pris TOUJOURS en charge)

def generateurDeMotsDePasse(n : int = 0 , Charset : string = Charset ) -> string:
    if n == 0:int(input(" Entrer le Nombre de caractère (longueur) pour génèré un mots de passe : "))
    # MDP : string = ""
    # for i in range(n):MDP += secrets.choice(Charset)
    # return MDP
    return "".join(secrets.choice(Charset) for i in range(n))




if __debug:
    if ___debug > 7 :
        print(Charset)
    print(generateurDeMotsDePasse(50,Charset))

import string,secrets,time
from faker import Faker
fake = Faker()


c="""║                                                                                                    ║
║          .---------..---------..---------..---------..---------..---------..---------.             ║
║          |R.-----. ||A.-----. ||Y.-----. ||K.-----. ||E.-----. ||S.-----. ||H.-----. |             ║
║          | : ( ) : || (\\ //) || (\\ //) || :/  \\: || (\\  /) || :/  \\: || :/  \\: |             ║
║          | ( ) ( ) || :\\ //: || :\\ //: || :\\  /: || :\\  /: || :\\  /: || (_____) |             ║
║          | '-----'R|| '-----'A|| '-----'Y|| '-----'K|| '-----'E|| '-----'S|| '-----'H|             ║
║          `---------'`---------'`---------'`---------'`---------'`---------'`---------'             ║
║                                                                                                    ║""".replace('\\','\\\\');x=100
c="\n╔"+"="*x+"╗"+"\n"+c+"\n╚"+"="*x+"╝"

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
    while n is None or n == 0:
        try:n=int(input(" Entrer le Nombre de caractère (longueur) pour génèré un mots de passe : "))
        except ValueError as v:print("ValueError",v," Mettre seuelement un entier")
    # MDP : string = ""
    # for i in range(n):MDP += secrets.choice(Charset)
    # return MDP
    return "".join(secrets.choice(Charset) for i in range(n))

def generateurDePhraseDePasse(n : int = 0 , Charset : string = fake.get_words_list(), separateur : string = "" , separateurFinale : bool = False ) -> string:
    """ permet de générer une phrase de passe (utilise un pseudo-aléatoire cryptographiquement fort (secrets)) """
    while n is None or n == 0:
        try:n=int(input(" Entrer le Nombre de mots (longueur) pour génèré un mots de passe : "))
        except ValueError as v:print("ValueError",v," Mettre seuelement un entier")
    # MDP : string = ""
    # for i in range(n):MDP += secrets.choice(Charset)+separateur
    # return MDP[:-len(separateur)] if not separateurFinale and len(separateur)>0 else MDP
    return "".join(secrets.choice(Charset)+separateur for i in range(n))[:-len(separateur)] if not separateurFinale and len(separateur)>0 else "".join(secrets.choice(Charset)+separateur for i in range(n))



if __debug:
    if ___debug > 7 :
        print(Charset)
    print(generateurDeMotsDePasse(50,Charset))
    print(generateurDeMotsDePasse(50,Charset))
    print(generateurDeMotsDePasse(50,Charset))
    if ___debug > 7 : print(fake.get_words_list())
    with open("Cyber\Blue Team\WordList_fr","r") as a :
        WordList_fr = [l[:-1] for l in a]
        if ___debug > 8 : print(WordList_fr)
        if ___debug > 7 : print(len(WordList_fr)) # 22740
        if ___debug > 7 : print(len(fake.get_words_list())) # 971
        print(generateurDePhraseDePasse(5,fake.get_words_list()+WordList_fr,','))
        print(generateurDePhraseDePasse(10,WordList_fr,'.'))
        print(generateurDePhraseDePasse(20,[i for i in WordList_fr if i.startswith('r') or i.startswith('R')],'.'))
    print(c,'\n',generateurDeMotsDePasse())
    print(c,'\n',generateurDePhraseDePasse(Charset=[i for i in fake.get_words_list()+WordList_fr if i.startswith('r') or i.startswith('R')]))
    # print(c,'\n')
    if ___debug > 4 :
        for i in range(1000):
            print("\r"+generateurDePhraseDePasse(10,[i for i in fake.get_words_list()+WordList_fr if i.startswith('r') or i.startswith('R')],'_'),end="");time.sleep(0.001*5)
        print('\n')

# Bien sur c'est mots de passe sont « bruteforçable » mais avec une longueur suffisant est un charset varié cette opération peut être considéré impossible dans un laps de temps raisonnables.
# Vous pouvez aussi mélanger plusieurs méthodes pour complexifié le pattern des MDP.
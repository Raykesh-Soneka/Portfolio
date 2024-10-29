import string,secrets

Lettre = string.ascii_letters
Espace = string.whitespace
nombre = string.digits
hexa = string.hexdigits
octa = string.octdigits
ponctuation = string.punctuation
tout = string.printable
print(string.__doc__)
print(['\n'+s for s in [Lettre, Espace, nombre, hexa, octa, ponctuation, tout]])

Charset : string = Lettre



print(Charset)

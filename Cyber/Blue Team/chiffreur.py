
Folder = "Cyber\\Blue Team\\"
key = 0x12  # Exemple de clée pour le XOR

def xor_donnee(data, key):
    return bytes(b ^ key for b in data)

## Créé un fichier chiffrer
with open(Folder+"generateurDeMDP.py","r+b") as o :
    with open(Folder+"generateurDeMDPChiffrer.py",'w+b') as c :
        # for i in o:
        #     c.write(i)
        while True:
            morceaux = o.read(1024)  # lis des morceaux de 1024 octets
            if not morceaux:break
            c.write(xor_donnee(morceaux, key)  )  # appliquer le XOR / écrire ds le fichier

Texte:str=""
## Déchiffre le fichier chiffrer
with open(Folder+"generateurDeMDPChiffrer.py","r+b") as c :
    with open(Folder+"generateurDeMDPDéChiffrer.py",'x+b') as d :
    # if True:
        # for i in o:
        #     d.write(i)
        while True:
            morceaux = c.read(1024)  # lis des morceaux de taile 1024 octets
            if not morceaux:break
            d.write(xor_donnee(morceaux, key)  )  # appliquer le XOR / écrire ds le fichier
            Texte+=str(xor_donnee(morceaux, key))#.replace("\\r\\n",'\n')
    import generateurDeMDPDéChiffrer,os,shutil # type: ignore
    try:
        os.remove("generateurDeMDPDéChiffrer.py")
        shutil.rmtree("__pycache__")
        # os.rmdir("__pycache__") #Le répertoire n’est pas vide
    except:
        os.remove("Cyber\Blue Team\generateurDeMDPDéChiffrer.py")
        shutil.rmtree("Cyber\Blue Team\__pycache__")
        # os.rmdir("Cyber\Blue Team\__pycache__") #Le répertoire n’est pas vide

# eval(Texte)

# for s in Texte.split("\\r\\n"):
#     print(s)

# print(eval(Texte))
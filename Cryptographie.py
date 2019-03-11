from itertools import product
import time
import os

def Menu():
    #Déclaration du menu principal
    reponse = 1
    
    while (reponse < 4) and (reponse != 0) :
        
        print("\nMenu : ")
        print("------")
        print("")
        print("01. Crypter un message")
        print("02. Décrypter un message")
        print("03. Casser une clé")
        print("10. Quitter")

        reponse = int(input("\nFaites votre choix : "))

        if reponse == 1 :
            #Demande le message à crypter et le clé de cryptage
            mes=input("\nVeuillez écrire votre message à crypter ")
            cle=input("\nVeuillez entrer votre clé de cyptage ")
            print("\nVoici votre message crypté\n")
            #Appel de la fonction de cryptage
            crypteMessage(mes, cle)
			
        elif reponse == 2 :
            #Demande le message à décrypter et le clé de décryptage
            mes=input("\nVeuillez écrire votre message à décrypter ")
            cle=input("\nVeuillez entrer votre clé de décyptage ")
            print("\nVoici votre message décrypté\n")
            #Appel de la fonction de décryptage
            decrypteMessage(mes, cle)

        elif reponse == 3 :
            #Demande le message à décrypter et le nombre de lettre
            #constituant la clé de décryptage
            mes=input("\nVeuillez écrire votre message à décrypter ")
            nbLettres=int(input("\nVeuillez entrer le nombre de lettres que contient la clé "))
            #Appel de la fonction de cassage de clés
            hackCle(mes, nbLettres)

        elif reponse == 10:
            break

        input("\nAppuyez sur une touche pour continuer ... ")
        os.system('clear')


def createAlphaKey(car):
    #Fonction servant à retouner un alphabet de cryptage
    car=car.upper()#Met le caractère en majuscule
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    id=alphabet.index(car)#Recherche dans l'alphabet la position du caractère
    alphakey=""
    for i in range(26):
        alphakey+=(alphabet[id])#crée l'alphabet de cryptage
        id=(id+1)%26
    return alphakey

def decrypteCar(car, alphakey):
    #Fonction servant à retouner un caractère décrypté en utilisant un
    #alphabet de cryptage
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    car=car.upper()#Met le caractère en majuscule
    id=alphakey.index(car)#Recherche dans l'alphabet de cryptage la position du caractère crypté
    return alphabet[id]
    
def decrypteMessage(mes, cle):
    #Fonction servant à décrypter un texte en utilisant une clé
    texte="\n"
    id=0
    for i in range(len(mes)):
        if mes[i].isalpha():#Recherche les caractère alphanumériques
        #Ecriture du texte décrypté en faisant appel à la fonction "decrypte"
        #elle-même faisant appel à la fonction "createAlphaKey"
            texte+=decrypteCar(mes[i],createAlphaKey(cle[id%len(cle)]))
            id+=1
        else:
        #Recherche des caractères non alphanumériques
            texte+=mes[i]
    print(texte)

def crypteCar(car, alphakey):
    #Fonction servant à retouner un caractère crypté en utilisant un
    #alphabet de cryptage
    car=car.upper()#Met le caractère en majuscule
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    id=alphabet.index(car)#Recherche dans l'alphabet la position du caractère
    return alphakey[id]
    
def crypteMessage(mes, cle):
    #Fonction servant à décrypter un texte en utilisant une clé
    texte="\n"
    id=0
    for i in range(len(mes)):
        if mes[i].isalpha():#Recherche les caractère alphanumériques
        #Ecriture du texte crypté en faisant appel à la fonction "crypte"
        #elle-même faisant appel à la fonction "createAlphaKey"
            texte+=crypteCar(mes[i],createAlphaKey(cle[id%len(cle)]))
            id+=1
        else:
        #Recherche des caractères non alphanumériques
            texte+=mes[i]
    print(texte) 

def hackCle(mes, nbLettres):
    #Fonction servant à casser une clé de cryptage par force brute
    debutTemps = time.time()
    #Création de toutes les combinaisons possibles de l'alphabet pour un nombre
    #de lettres donné ex: ('ABC', 2) --> AA, AB, AC, BA, BB, BC, CA, CB, CC
    #Cela est réalisé par la fonction "product()"
    for cle in (product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=nbLettres)):
        print("\nVoici le message pour la cle: ", ''.join(cle))
        #Appel de la fonction "decrypteMessage
        decrypteMessage(mes, cle)
    print("\nTemps d execution : %s secondes ---" % (time.time() - debutTemps))


Menu()

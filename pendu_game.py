#jeu du pendu

#Fonction permettant l'affichage du nombre de vie et du pendu dans la console
def affichage_vie(vie):
    if vie==6:
        print("Il vous reste 6 vies")
    if vie==5:
        print("---")
        print("Il vous reste 5 vies")
    if vie==4:
        print(" |\n | \n |\n |\n---")
        print("Il vous reste 4 vies")
    if vie==3:
        print(" ___ \n | \n |\n |\n |\n---")
        print("Il vous reste 3 vies")
    if vie==2:
        print(" ___ \n | | \n |\o/ \n |\n |\n---")
        print("Il vous reste 2 vies")
    if vie==1:
        print(" ___ \n | | \n |\o/ \n | | \n |\n---")
        print("Il vous reste 1 vie")
    if vie==0:
        print(" ___ \n | | \n |\o/ \n | | \n |/ \ \n---")
        print("Vous n'avez plus de vie, DEFAITE")

# on vérifie si la lettre donnée appartient au mot du jeu
# on renvoie 1 si elle appartient 0 sinon
def win_or_lose (words,letter):
    for i in range(len(words)):
        if letter == words[i]:
            return 1
    return 0


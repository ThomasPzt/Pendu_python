# jeu du pendu
import random

# Pour gérer les lettres avec accents
accent_letter = {
    'à': 'a', 'â': 'a', 'ä': 'a',
    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'î': 'i', 'ï': 'i',
    'ô': 'o', 'ö': 'o',
    'ù': 'u', 'û': 'u', 'ü': 'u',
    'ç': 'c'
}


# Fonction pour choisir un mot au hasard
# avec un fichier au choix de l'utilisateur ou le fichier de base
def choisir_mot():
    print(
        '\nSi vous voulez utiliser un fichier texte personel pour le jeu, \nAssurez vous que le fichier contienne un '
        'mot par ligne séparé par un Entrée ')
    fiche = input('Entrez le nom du fichier .txt sinon pressez Entrée:')
    if fiche == '':
        fiche = 'mots_pendu.txt'

    # Ouverture du fichier en mode lecture
    with open(fiche, 'r') as fichier:
        contenu = fichier.read()
    # Création d'une liste de mots en éliminant les saut de ligne
    mots = contenu.split('\n')
    # mot final random
    mot = random.choice(mots)
    return ''.join(accent_letter.get(char, char) for char in mot)


def demande_lettre():
    return input('Tapez une lettre minuscule :')


# Fonction permettant l'affichage du nombre de vie et du pendu dans la console
def affichage_vie(vie):
    if vie == 6:
        print("Il vous reste 6 vies\n")
    if vie == 5:
        print("---")
        print("Il vous reste 5 vies\n")
    if vie == 4:
        print(" |\n | \n |\n |\n---")
        print("Il vous reste 4 vies\n")
    if vie == 3:
        print(" ___ \n | \n |\n |\n |\n---")
        print("Il vous reste 3 vies\n")
    if vie == 2:
        print(" ___ \n | | \n |\o/ \n |\n |\n---")
        print("Il vous reste 2 vies\n")
    if vie == 1:
        print(" ___ \n | | \n |\o/ \n | | \n |\n---")
        print("Il vous reste 1 vie \n")
    if vie == 0:
        print(" ___ \n | | \n |\o/ \n | | \n |/ \ \n---")
        print("Vous n'avez plus de vie, DEFAITE \n")


# Fonction pour afficher le mot en fonction des lettres trouvées
# words et le mot désigné par le jeu et nblettre une liste des lettres trouvées par le joueur
def affichage_mot(mot, nblettre):
    mot_affiche = ['_' if lettre not in nblettre else lettre for lettre in mot]
    print(' '.join(mot_affiche))


# on vérifie si la lettre donnée appartient au mot du jeu
# on renvoie 1 si elle appartient 0 sinon
# de plus si la lettre donnée à un accent on la remplace par la lettre sans  accent
def win_or_lose(words, letter):
    letter = accent_letter.get(letter, letter)
    for i in range(len(words)):
        if letter == words[i]:
            return 1
    return 0

#############################################
# Gestion du jeu avec les fonctions précédentes

mot = choisir_mot()
vie = 6
lettre_trouvee = []
while vie != 0 and len(lettre_trouvee) != len(mot):
    affichage_mot(mot, lettre_trouvee)
    lettre = demande_lettre()
    if win_or_lose(mot, lettre):
        lettre_trouvee.append(lettre)
        print('La lettre tapée appartient bien au mot secret!\n')
    else:
        vie -= 1
    affichage_vie(vie)

print('victoire, vous avez trouvé le mot qui était :', mot)

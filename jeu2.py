import random
import unicodedata
import os

# Identifier le répertoire où se trouve le script
dossier_script = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin du fichier French_words.txt
chemin_fichier = os.path.join(dossier_script, "French_words.txt")

# Lire les mots depuis French_words.txt avec un encodage tolérant
with open(chemin_fichier, "r", encoding="latin-1") as fichier:
    mots = fichier.read().splitlines()

# Enlever les accents
mots_sans_accents = [
    ''.join(c for c in unicodedata.normalize('NFD', mot) if unicodedata.category(c) != 'Mn')
    for mot in mots
]

# Afficher les 10 premiers mots sans accents pour vérifier
print(mots_sans_accents[:10])

# Choisir le mot secret parmi les mots sans accents
mot_secret = random.choice(mots_sans_accents)

def verifier_mot(mot_joueur, mot_secret):
    resultat = []
    for i in range(len(mot_joueur)):
        if i < len(mot_secret) and mot_joueur[i] == mot_secret[i]:
            resultat.append('V')  # Lettre correcte et bien placée
        elif mot_joueur[i] in mot_secret:
            resultat.append('J')  # Lettre correcte mais mal placée
        else:
            resultat.append('X')  # Lettre incorrecte
    return ''.join(resultat)

# Début du jeu
MAX_TENTATIVES = 6

tentatives = 0
print(f"Bienvenue dans le jeu ! Devinez le mot secret ({len(mot_secret)} lettres).")

while tentatives < MAX_TENTATIVES:
    mot_joueur = input(f"Tentative {tentatives + 1}/{MAX_TENTATIVES}: ").strip().lower()
    
    # Vérifier la validité du mot
    if len(mot_joueur) != len(mot_secret):
        print(f"Veuillez entrer un mot de {len(mot_secret)} lettres.")
        continue
    if mot_joueur not in mots_sans_accents:
        print("Mot invalide. Assurez-vous d'entrer un mot valide du dictionnaire.")
        continue
    
    # Vérifier le mot et afficher le résultat
    resultat = verifier_mot(mot_joueur, mot_secret)
    print("Résultat:", resultat)
    
    # Vérifier si le joueur a gagné
    if mot_joueur == mot_secret:
        print("Félicitations ! Vous avez trouvé le mot secret !")
        break
    
    tentatives += 1

# Si le joueur n'a pas trouvé le mot secret
if mot_joueur != mot_secret:
    print(f"Désolé, vous avez épuisé vos tentatives. Le mot secret était: {mot_secret}")

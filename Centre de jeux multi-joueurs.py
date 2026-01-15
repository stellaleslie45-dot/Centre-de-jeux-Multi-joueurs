# centre de jeux multi-joueurs / 

# main.py
# games.py
# Data _manager.py
# Leaderboard.json

import json
import os
from datetime import datetime

def creer_profil(nom_joueur=None): 
    """créer un profil joueur et le sauvegarde en json.
    si nom_joueur est None, demande le nom d'utilisateur.
    """
    print("\n--- création du profil joueur ---")

    # si aucun nom fourni, demander à l'utilisateur
    if nom_joueur is None:
        nom_joueur = input("Entrez votre nom d'utilisateur(ou laisser vide pour Eric) : ").strip()
        if nom_joueur == "":
            nom_joueur = "Eric" # par defaut pour testelse:
    else:
        nom_joueur = nom_joueur.strip()  # ex: "Eric"

    # Vérification nom vide (au cas où)
    if nom_joueur == "":
        print(" Le nom ne peut pas être vide.")
        return

    # Création du dossier profiles s'il n'existe pas
    if not os.path.exists("profiles"):
        os.mkdir("profiles")

    chemin_fichier = f"profiles/{nom_joueur}.json"

    # Vérification profil existant
    if os.path.exists(chemin_fichier):
        print(f" Le profil '{nom_joueur}' existe déjà.")
        return

    # Création du dictionnaire du profil
    profil = {
        "nom": nom_joueur,
        "date_creation": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "parties": [],
        "score_total": 0,
        "succes": []
    }

    # Sauvegarde dans un fichier JSON
    try:
        with open(chemin_fichier, "w", encoding="utf-8") as fichier:
            json.dump(profil, fichier, indent=4, ensure_ascii=False)

        print(f" Profil '{nom_joueur}' créé avec succès !")

    except Exception as e:
        print(" Erreur lors de la sauvegarde du profil :", e)


def charher_profil():
    """
    charge un profil existant depuis le dossier 'profiles/'.
    Affiche le contenu et retourne le dictionnaire du profil.
    """
    print("\n--- CHARGEMENT D'UN PROFIL ---")

    nom_joueur = input("Entrez le nom du joueur à charger (ex: Eric): ").strip()
    if nom_joueur == "":
        print("Le nom ne peut pas être vide.")
        return None
    
    chemin_profiles = f"profiles/{nom_joueur}.json"

    # verification que le fichier existe
    if not os.path.exists(chemin_profiles):
        print(f" Le profil '{nom_joueur}' n'existe pas.")
        return None
    
    # Lecture du fichier json 
    try:
        with



# main.py 
def afficher_menu():
    while True:
        print("\n====== CENTRE DE JEUX MULTI-JOUEURS ======")
        print("1. Créer un profil")
        print("2. Charger un profil")
        print("3. Jouer")
        print("4. Classements")
        print("5. Succès")
        print("6. Règles")
        print("7. Quitter")
        print("========================================")

        try:
            choix_utilisateur = int(input("Veuillez entrer un chiffre entre 1 et 7"))
            if choix_utilisateur == 1:
                creer_profil()
            elif choix_utilisateur == 2:
                print("chargement du profil")
            elif choix_utilisateur == 3:
                print("lancement des jeux")
            elif choix_utilisateur == 4:
                print("affichage des classements")
            elif choix_utilisateur == 5:
                print("affichage des succés")
            elif choix_utilisateur == 6:
                print("\n--- RÈGLES DU JEU ---")
                print("• Devine le nombre selon la difficulté")
                print("• Calcul mental en 30 secondes")
                print("• Trouver le mot au pendu")
                print("--------------------")
            elif choix_utilisateur == 7:
                print("Merci d'avoir joué ! À bientôt.")
                break
            else:
                print(" Choix invalide. Veuillez entrer un nombre entre 1 et 7.")
        except ValueError:
            print(" Entrée invalide. Veuillez entrer un chiffre.")















afficher_menu()






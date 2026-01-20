# Fichier: gestion_profils.py
import json
import os
from datetime import datetime
import donnees 

def sauvegarder(profil):
    """
    Sauvegarde les données du profil dans un fichier JSON dédié.

    Le nom du fichier est généré automatiquement à partir du nom du joueur (ex: "Alex.json").
    Cette fonction écrase le fichier existant avec les nouvelles données pour mettre à jour
    la progression.

    Args:
        profil (dict): Le dictionnaire contenant toutes les informations du joueur
                       (nom, score, historique, succès).

    Returns:
        None
    """
   
    nom_fichier = f"{profil['nom']}.json"
    chemin_complet = os.path.join(donnees.DOSSIER_PROFILS, nom_fichier)

    try:
        with open(chemin_complet, 'w', encoding='utf-8') as f:
            json.dump(profil, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erreur lors de la sauvegarde du profil : {e}")

def creer_profil():
   
    """
    Crée un nouveau profil joueur via une interface interactive.

    Cette fonction :
    1. Demande à l'utilisateur de choisir un pseudo (alphanumérique, min 3 caractères).
    2. Vérifie que le pseudo n'existe pas déjà dans le dossier de sauvegarde.
    3. Initialise la structure de données standard (score à 0, listes vides).
    4. Sauvegarde immédiatement le nouveau profil sur le disque.

    Returns:
        dict: Le dictionnaire du nouveau profil créé.
    """
   
   
    print("\n--- CRÉATION DE PROFIL ---")
    while True:
        nom = input("Entrez votre nom de joueur (lettres/chiffres seulement) : ").strip()
        
        if not nom.isalnum():
            print("Le nom ne doit contenir que des lettres et des chiffres.")
            continue
        if len(nom) < 3:
            print("Le nom doit faire au moins 3 caractères.")
            continue
            
        chemin_fichier = os.path.join(donnees.DOSSIER_PROFILS, f"{nom}.json")
        if os.path.exists(chemin_fichier):
            print(f"Le profil '{nom}' existe déjà. Choisissez un autre nom.")
            continue
            
        break

    nouveau_profil = {
        "nom": nom,
        "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "parties": [],
        "score_total": 0,
        "succes": []
    }

    sauvegarder(nouveau_profil)
    print(f"Profil '{nom}' créé avec succès !")
    return nouveau_profil

def charger_profil():
    """
    Permet à l'utilisateur de sélectionner et charger un profil existant.

    Cette fonction affiche la liste des fichiers .json trouvés dans le dossier
    de sauvegarde et demande à l'utilisateur d'en choisir un par son numéro.
    Elle gère les erreurs de lecture (fichier corrompu) et les dossiers vides.

    Returns:
        dict: Le dictionnaire du profil chargé si tout se passe bien.
        None: Si l'utilisateur annule ('q'), s'il n'y a pas de profils,
              ou si le fichier est corrompu.
    """
    print("\n--- CHARGEMENT DE PROFIL ---")
    try:
        fichiers = [f for f in os.listdir(donnees.DOSSIER_PROFILS) if f.endswith('.json')]
    except FileNotFoundError:
        print("Le dossier de profils n'existe pas encore.")
        return None

    if not fichiers:
        print("Aucun profil existant. Veuillez en créer un.")
        return None

    print("Profils disponibles :")
    for i, f in enumerate(fichiers, 1):
        print(f"{i}. {f[:-5]}") 

    while True:
        choix = input("Choisissez le numéro de votre profil (ou 'q' pour quitter) : ")
        if choix.lower() == 'q':
            return None
            
        try:
            index = int(choix) - 1
            if 0 <= index < len(fichiers):
                fichier_choisi = fichiers[index]
                break
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Veuillez entrer un chiffre.")

    chemin_complet = os.path.join(donnees.DOSSIER_PROFILS, fichier_choisi)
    try:
        with open(chemin_complet, 'r', encoding='utf-8') as f:
            profil = json.load(f)
        print(f"Profil '{profil['nom']}' chargé ! Score actuel : {profil['score_total']}")
        return profil
    except (IOError, json.JSONDecodeError) as e:
        print(f"Erreur : Le fichier de profil est corrompu ({e}).")
        return None
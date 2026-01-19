# Fichier: gestion_profils.py
import json
import os
from datetime import datetime
import donnees 

def sauvegarder(profil):
    nom_fichier = f"{profil['nom']}.json"
    chemin_complet = os.path.join(donnees.DOSSIER_PROFILS, nom_fichier)

    try:
        with open(chemin_complet, 'w', encoding='utf-8') as f:
            json.dump(profil, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erreur lors de la sauvegarde du profil : {e}")

def creer_profil():
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
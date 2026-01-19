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


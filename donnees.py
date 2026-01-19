# Fichier: donnees.py
import os

# --- CONFIGURATION DES DOSSIERS ---
DOSSIER_DATA = "data"
DOSSIER_PROFILS = os.path.join(DOSSIER_DATA, "profils")
FICHIER_CLASSEMENTS = os.path.join(DOSSIER_DATA, "classements.json")

# Création automatique du dossier profils s'il n'existe pas
if not os.path.exists(DOSSIER_PROFILS):
    os.makedirs(DOSSIER_PROFILS, exist_ok=True)


# Fichier: donnees.py
import os

# --- CONFIGURATION DES DOSSIERS ---
DOSSIER_DATA = "data"
DOSSIER_PROFILS = os.path.join(DOSSIER_DATA, "profils")
FICHIER_CLASSEMENTS = os.path.join(DOSSIER_DATA, "classements.json")

# Création automatique du dossier profils s'il n'existe pas
if not os.path.exists(DOSSIER_PROFILS):
    os.makedirs(DOSSIER_PROFILS, exist_ok=True)


# --- DESSINS DU PENDU (7 étapes : de 0 à 6 erreurs) ---
PENDU_ASCII = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========



    .
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]
# --- LISTE DE MOTS PAR THÈME ---
MOTS_PAR_THEME = {
    "Informatique": [
        "PYTHON", "ALGORITHME", "CLAVIER", "ECRAN", "INTERNET", "WIFI", "SOURIS",
        "PROCESSEUR", "MEMOIRE", "LINUX", "WINDOWS", "PROGRAMME", "FONCTION",
        "VARIABLE", "BOUCLE", "CONDITION", "RESEAU", "SERVEUR", "DONNEES", "FICHIER"
    ],
    "Animaux": [
        "ELEPHANT", "GIRAFE", "CROCODILE", "HIPPOPOTAME", "LION", "TIGRE", "SINGE",
        "PERROQUET", "DAUPHIN", "BALEINE", "REQUIN", "AIGLE", "PINGOUIN", "OURS",
        "LOUP", "RENARD", "SERPENT", "TORTUE", "LAPIN", "HAMSTER"
    ],
    "Pays": [
        "FRANCE", "CAMEROUN", "CANADA", "BRESIL", "JAPON", "CHINE", "ALLEMAGNE",
        "ESPAGNE", "ITALIE", "NIGERIA", "SENEGAL", "MAROC", "EGYPTE", "INDE",
        "AUSTRALIE", "ARGENTINE", "MEXIQUE", "RUSSIE", "SUEDE", "NORVEGE"
    ],

    "Nourriture": [
        "PIZZA", "HAMBURGER", "RIZ", "POULET", "FROMAGE", "PAIN", "CHOCOLAT",
        "PASTA", "SALADE", "SOUPE", "BANANE", "ORANGE", "FRAISE", "GATEAU",
        "GLACE", "YAOURT", "OEUF", "POISSON", "VIANDE", "LEGUME"
    ],

    "Sports": [
        "FOOTBALL", "BASKETBALL", "TENNIS", "VOLLEY", "HANDBALL", "NATATION",
        "BOXE", "JUDO", "KARATE", "RUGBY", "ATHLETISME", "CYCLISME", "SKI",
        "SURF", "GOLF", "ESCALADE", "DANSE", "YOGA", "MUSCULATION", "ESCRIME"
    ]
}




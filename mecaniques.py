# Fichier: mecaniques.py
import donnees 
import os # pour la gestion des fichiers
import json # pour lire/écrire les classements

def calculer_points(jeu, difficulte, essais=0, temps=0):
    score = 0 # score initial
    if jeu == "devinette":
        if difficulte == 1: base = 50
        elif difficulte == 2: base = 100
        else: base = 200 # plus de points pour plus de difficulté
        malus = (essais - 1) * 2 # pénalité par essai supplémentaire
        score = max(1, base - malus) #Le score ne peut jamais être inférieur à 1
    elif jeu == "calcul": 
        points_par_reponse = 10
        score = essais * points_par_reponse
    elif jeu == "pendu":
        points_par_vie = 30
        vies_restantes = 6 - essais
        score = vies_restantes * points_par_vie
        score += temps * 5
    return score

def verifier_succes(profil):
    succes_definitions = {
        "Débutant": lambda p: len(p['parties']) >= 1,
        "Habitué": lambda p: len(p['parties']) >= 10,
        "Accro": lambda p: len(p['parties']) >= 50,
        "Première Victoire": lambda p: any(partie['score'] > 0 for partie in p['parties']),
        "Score Parfait": lambda p: any("12 justes" in partie.get('details', '') or "0 essais" in partie.get('details', '') for partie in p['parties']),
        "Maître du Calcul": lambda p: any(partie['jeu'] == "Calcul Mental" and partie['score'] >= 100 for partie in p['parties']),
        "Devin": lambda p: any(partie['jeu'] == "Devinette" and partie['score'] >= 150 for partie in p['parties']),
        "Survivant": lambda p: any(partie['jeu'] == "Pendu" and "Mot :" in partie['details'] for partie in p['parties']),
        "Millionnaire": lambda p: p['score_total'] >= 1000
    }

    nouveaux_succes = []
    for nom_succes, condition in succes_definitions.items():
        if nom_succes not in profil['succes'] and condition(profil):
            profil['succes'].append(nom_succes)
            nouveaux_succes.append(nom_succes)

    if nouveaux_succes:
        print("\n" + "★" * 40)
        print("🏆 NOUVEAU(X) SUCCÈS DÉBLOQUÉ(S) !")
        for s in nouveaux_succes:
            print(f"   - {s}")
        print("★" * 40 + "\n")
        return True
    return False


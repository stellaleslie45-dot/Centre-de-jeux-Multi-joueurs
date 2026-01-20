# Fichier: mecaniques.py
import donnees
import os
import json

def calculer_points(jeu, difficulte, essais=0, temps=0):
    
    """
    Calcule le nombre de points gagnés à la fin d'une partie.

    La logique de calcul dépend du jeu :
    - Devinette : Base de points selon difficulté (50/100/200) moins les essais supplémentaires.
    - Calcul Mental : Nombre de bonnes réponses multiplié par 10.
    - Pendu : Points par vie restante + bonus selon la longueur du mot.

    Args:
        jeu (str): Le nom du jeu ("devinette", "calcul", "pendu").
        difficulte (int): Le niveau de difficulté (0 si non applicable).
        essais (int, optional): Nombre d'essais ou d'erreurs, ou de bonnes réponses (selon le jeu). Défaut à 0.
        temps (int, optional): Temps écoulé ou longueur du mot (pour le bonus Pendu). Défaut à 0.

    Returns:
        int: Le score final calculé (minimum 1 point pour la devinette si gagné, sinon peut être 0).
    """
    
    score = 0
    if jeu == "devinette":
        if difficulte == 1: base = 50
        elif difficulte == 2: base = 100
        else: base = 200
        malus = (essais - 1) * 2 
        score = max(1, base - malus)
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

def afficher_classements():
    print("\n--- 🏆 CLASSEMENT GLOBAL (TOP 10) ---")
    liste_joueurs = []
    if not os.path.exists(donnees.DOSSIER_PROFILS):
        print("Aucun profil trouvé.")
        return

    fichiers = [f for f in os.listdir(donnees.DOSSIER_PROFILS) if f.endswith('.json')]
    for fichier in fichiers:
        chemin = os.path.join(donnees.DOSSIER_PROFILS, fichier)
        try:
            with open(chemin, 'r', encoding='utf-8') as f:
                data = json.load(f)
                liste_joueurs.append( (data['nom'], data.get('score_total', 0)) )
        except:
            continue

    liste_joueurs.sort(key=lambda x: x[1], reverse=True)
    
    print(f"{'RANG':<5} | {'NOM':<15} | {'SCORE':<10}")
    print("-" * 35)
    for i, joueur in enumerate(liste_joueurs[:10], 1):
        nom, score = joueur
        prefixe = "🥇 " if i == 1 else "🥈 " if i == 2 else "🥉 " if i == 3 else ""
        print(f"{i:<5} | {prefixe}{nom:<13} | {score:<10}")
    
    input("\nAppuyez sur Entrée pour revenir au menu...")
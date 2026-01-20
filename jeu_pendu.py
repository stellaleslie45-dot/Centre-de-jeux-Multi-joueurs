# Fichier: jeu_pendu.py
import random
from datetime import datetime
import donnees
import gestion_profils
import mecaniques

def lancer(profil):
    
    """
    Lance une partie complète du jeu du Pendu.

    Le déroulement est le suivant :
    1. Le joueur sélectionne un thème parmi ceux disponibles (ex: Informatique, Animaux).
    2. Un mot est tiré au sort dans la liste correspondante.
    3. Le joueur propose des lettres :
       - Si correct : la lettre est révélée dans le mot.
       - Si faux : le compteur d'erreurs augmente et le dessin du pendu progresse.
    4. La partie s'arrête si le mot est trouvé (Victoire + Points + Sauvegarde) 
       ou si le dessin est complet (Défaite + Révélation du mot).

    Args:
        profil (dict): Le dictionnaire du joueur actif. Il est modifié en cas de victoire 
                       (ajout du score et de l'historique).

    Returns:
        None
    """
    
    print("\n--- JEU : LE PENDU ---")
    themes = list(donnees.MOTS_PAR_THEME.keys())
    for i, theme in enumerate(themes, 1):
        print(f"{i}. {theme}")
    
    while True:
        try:
            c = int(input("Choix du thème : "))
            if 1 <= c <= len(themes):
                theme = themes[c-1]
                break
        except ValueError: pass

    mot = random.choice(donnees.MOTS_PAR_THEME[theme])
    lettres_trouvees = set()
    erreurs = 0
    max_erreurs = 6
    
    while erreurs < max_erreurs:
        print(donnees.PENDU_ASCII[erreurs])
        mot_affiche = "".join([l + " " if l in lettres_trouvees else "_ " for l in mot])
        print(f"Mot : {mot_affiche}")
        
        if "_" not in mot_affiche:
            print(f"\n🎉 GAGNÉ ! Le mot était {mot}")
            points = mecaniques.calculer_points("pendu", 0, essais=erreurs, temps=len(mot))
            print(f"💰 +{points} points")
            
            profil["score_total"] += points
            profil["parties"].append({
                "jeu": "Pendu",
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "details": f"Mot : {mot}",
                "score": points
            })
            mecaniques.verifier_succes(profil)
            gestion_profils.sauvegarder(profil)
            break
            
        lettre = input("Lettre : ").upper()
        if len(lettre) != 1 or not lettre.isalpha() or lettre in lettres_trouvees:
            continue
            
        lettres_trouvees.add(lettre)
        if lettre not in mot:
            erreurs += 1
            print(f"❌ Non.")
            
    if erreurs == max_erreurs:
        print(donnees.PENDU_ASCII[-1])
        print(f"💀 PERDU ! C'était : {mot}")
    
    input("\nAppuyez sur Entrée...")
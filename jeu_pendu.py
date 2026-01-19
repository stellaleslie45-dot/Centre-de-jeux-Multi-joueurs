# Fichier: jeu_pendu.py
import random # pour générer des nombres aléatoires
from datetime import datetime  # pour enregistrer la date des parties
import donnees # contient les mots et dessins du pendu
import gestion_profils # module de gestion des profils
import mecaniques # module maison pour les points et les succès

def lancer(profil):
    print("\n--- JEU : LE PENDU ---")
    themes = list(donnees.MOTS_PAR_THEME.keys()) # obtenir les thèmes disponibles
    for i, theme in enumerate(themes, 1):
        print(f"{i}. {theme}")
    
    while True:   # boucle pour forcer l utilisateur a choisir un thème valide
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
        if len(lettre) != 1 or not lettre.isalpha() or lettre in lettres_trouvees: # verifier la validité de l entrée
            continue
            
        lettres_trouvees.add(lettre)
        if lettre not in mot:
            erreurs += 1
            print(f"❌ Non.") # indication de lettre incorrecte
            
    if erreurs == max_erreurs:
        print(donnees.PENDU_ASCII[-1])
        print(f"💀 PERDU ! C'était : {mot}") # Afficher le mot perdu
    
    input("\nAppuyez sur Entrée...")

    """ Le fichier jeu_pendu.py permet de lancer le jeu du pendu.
Le joueur choisit un thème, puis un mot est sélectionné aléatoirement.
Il doit deviner le mot lettre par lettre avec un nombre limité d’erreurs.
À chaque mauvaise lettre, le dessin du pendu progresse.
Si le mot est trouvé, le joueur gagne des points, la partie est enregistrée et le profil est sauvegardé.
En cas d’échec, le mot est révélé et la partie se termine. """
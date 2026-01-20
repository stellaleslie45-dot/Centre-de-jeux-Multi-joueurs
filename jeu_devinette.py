# Fichier: jeu_devinette.py
import random    # pour generer des nombres aléatoires
from datetime import datetime   # pour enregistrer la date des parties
import gestion_profils  # module de gestion des profils
import mecaniques  # mosule maison pour les points et les succès

def lancer(profil):
    """
    Lance une partie du jeu 'Devine le Nombre'.

    Cette fonction gère le déroulement complet d'une partie :
    1. Demande au joueur de choisir une difficulté (Facile, Moyen, Difficile).
    2. Génère un nombre aléatoire dans l'intervalle correspondant.
    3. Boucle jusqu'à ce que le joueur trouve le nombre, en donnant des indices (plus grand/plus petit).
    4. Calcule les points et met à jour le dictionnaire du profil (score et historique).
    5. Sauvegarde automatiquement la progression et vérifie les succès.

    Args:
        profil (dict): Le dictionnaire représentant le profil du joueur actuel. 
                       Ce dictionnaire est modifié sur place (ajout des points et de la partie).

    Returns:
        None
    """
    print("\n--- JEU : DEVINE LE NOMBRE ---")
    # ... le reste de ton code ...
    print("\n--- JEU : DEVINE LE NOMBRE ---")
    print("1. Facile (1-50)")
    print("2. Moyen (1-100)")
    print("3. Difficile (1-500)")
    
    while True:    # boucle qui force l utilisateur a entré une valeur correcte
        try:
            choix_diff = int(input("Choisissez la difficulté (1-3) : "))
            if 1 <= choix_diff <= 3: break
        except ValueError: pass
        print("Entrée invalide.")

           # definir la borne max selon la difficulté choisie
    if choix_diff == 1: borne_max, nom_diff = 50, "Facile"
    elif choix_diff == 2: borne_max, nom_diff = 100, "Moyen"
    else: borne_max, nom_diff = 500, "Difficile"

           # generer le nombre secret
    nombre_secret = random.randint(1, borne_max)
    essais = 0
    print(f"\nC'est parti ! Je pense à un nombre entre 1 et {borne_max}.")
    
    while True:
        essais += 1   # incrémente le nombre d essaie 
        user_input = input(f"Essai #{essais} (ou 'q' pour quitter): ")  # demande une valeur a l utilisateur
        if user_input.lower() == 'q': return  # quitter le jeu si l utilisateur le souhaite

              # verifie si l entree est un nombre
        try:
            devinette = int(user_input)
        except ValueError:
            print("Ce n'est pas un nombre.")
            essais -= 1
            continue

        if devinette < nombre_secret:  # compare la devinette avec le nombre secret
            print("📈 C'est plus grand !")
        elif devinette > nombre_secret:
            print("📉 C'est plus petit !")
        else:   # code de victoire 
            print(f"🎉 BRAVO ! Trouvé en {essais} essais.")
            points = mecaniques.calculer_points("devinette", choix_diff, essais=essais)  # calcul des points
            print(f"💰 Vous gagnez {points} points !")
            
            profil["score_total"] += points  # mise a jour du score total
            profil["parties"].append({  # enregistrement de la partie
                "jeu": "Devinette",
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "details": f"{nom_diff} - {essais} essais",
                "score": points
            })

            # verification des succes débloqués
            mecaniques.verifier_succes(profil)
            gestion_profils.sauvegarder(profil)  # sauvegarde du profil
            input("\nAppuyez sur Entrée...") # pause avant de quitter le jeu
            break


        """ resumé simple
        le jeu :
           - propose 3 niveaux de difficulté
           - génère un nombre aléatoire selon la difficulté
           - demande à l'utilisateur de deviner le nombre 
           - compte les essais
           - calcule les points selon la difficulté et le nombre d essais
           - met a jour le profil du joueur avec le score et la partie jouée 
           - sauvegarde automatiquement
             """
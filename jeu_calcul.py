# Fichier: jeu_calcul.py
import random  # Pour générer des nombres aléatoires
import time    # gerer le chronomtre (30 secondes)
from datetime import datetime   # Pour enregistrer la date des parties
import gestion_profils   # module de gestion des profils
import mecaniques   # calcul des points et succes

def lancer( profil ): # profil est le dictionnaire du joueur actuel
    print("\n--- JEU : CALCUL MENTAL ---")
    input("Appuyez sur Entrée pour lancer le chrono (30s) ! ⏱️")

    # initialisation du chronomètre et des variables
    start_time = time.time()  # Temps de début
    duree_max = 30  # Durée maximale en secondes
    bonnes_reponses = 0  # Compteur de bonnes réponses
    
    while True:    # boucle principale du jeu il continue jusqu'à ce que le temps soit écoulé
        temps_ecoule = time.time() - start_time
        if temps_ecoule >= duree_max:
            print("\n⏰ DRIIIIING ! Temps écoulé !")
            break    # si 30 secodes sont passées, on sort de la boucle
            
        operateur = random.choice(['+', '-', '*'])      # choisir un opérateur aléatoire
        if operateur == '+':
            a, b = random.randint(1, 50), random.randint(1, 50)
            reponse = a + b
        elif operateur == '-':
            a, b = random.randint(1, 50), random.randint(1, 50)
            if a < b: a, b = b, a 
            reponse = a - b
        else:
            a, b = random.randint(1, 12), random.randint(1, 12)
            reponse = a * b
            
        print(f"\nTemps : {int(duree_max - temps_ecoule)}s | Calcul : {a} {operateur} {b} = ?")
        try:
            user_input = input("Réponse : ") # obtenir la réponse de l'utilisateur
            if time.time() - start_time >= duree_max: break # vérifier le temps après la saisie
            if int(user_input) == reponse:
                print("✅ Correct !")
                bonnes_reponses += 1  # incrémenter le compteur de bonnes réponses
            else:
                print(f"❌ Faux ! C'était {reponse}")   
        except ValueError:
            pass

    points = mecaniques.calculer_points("calcul", 0, essais=bonnes_reponses)
    if points > 0:
        print(f"📊 {bonnes_reponses} justes. Vous gagnez {points} points !")
        profil["score_total"] += points
        profil["parties"].append({
            "jeu": "Calcul Mental",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "details": f"30s - {bonnes_reponses} justes",
            "score": points
        })
        mecaniques.verifier_succes(profil)  # detection des succes débloqués
        gestion_profils.sauvegarder(profil)  # sauvegarde du profil mis à jour
    else:
        print("Dommage, pas de points.")
    input("\nAppuyez sur Entrée...")

    """"""








    
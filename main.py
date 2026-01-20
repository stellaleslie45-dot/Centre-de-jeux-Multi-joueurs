"""
Projet : Centre de Jeux Multi-joueurs
Description : Application console permettant de jouer à 3 mini-jeux (Devinette, Calcul, Pendu),
              de gérer des profils utilisateurs et de sauvegarder la progression.
Auteurs : [Ton Prénom] & [Prénom de ta partenaire]
Date : Janvier 2024
"""

# Fichier: main.py
import gestion_profils
import mecaniques
import jeu_devinette
import jeu_calcul
import jeu_pendu

def menu_principal():
    
    """
    Fonction principale : Point d'entrée et chef d'orchestre du programme.

    Cette fonction gère la boucle infinie du menu principal. Elle est responsable de :
    1. Afficher l'interface graphique (textuelle) et le statut du joueur actif.
    2. Recueillir le choix de l'utilisateur.
    3. Diriger l'utilisateur vers les bons modules (gestion_profils, jeux, mecaniques).
    4. Vérifier qu'un profil est bien chargé avant de lancer un jeu.
    5. Quitter proprement l'application.

    Args:
        None

    Returns:
        None
    """
    profil_actuel = None 
    
    profil_actuel = None 

    while True:
        print("\n" + "="*40)
        print("   CENTRE DE JEUX MULTI-JOUEURS   ")
        print("="*40)
        
        if profil_actuel:
            print(f"👤 JOUEUR ACTIF : {profil_actuel['nom']}")
            print(f"🏆 SCORE GLOBAL : {profil_actuel['score_total']} pts")
        else:
            print("👤 Aucun profil chargé")
        
        print("-" * 40)
        print("1. Créer un nouveau profil")
        print("2. Charger un profil existant")
        print("3. Jouer à 'Devine le Nombre'")
        print("4. Jouer au 'Calcul Mental'")
        print("5. Jouer au 'Pendu'")
        print("6. Voir les Classements (Top 10)")
        print("7. Quitter")
        
        choix = input("\n👉 Votre choix : ")

        if choix == "1":
            profil_actuel = gestion_profils.creer_profil()
        elif choix == "2":
            p = gestion_profils.charger_profil()
            if p: profil_actuel = p
        elif choix in ["3", "4", "5"]:
            if profil_actuel is None:
                print("\n⛔ ERREUR : Chargez un profil d'abord !")
                continue
            
            # Note comment on appelle la fonction 'lancer' de chaque fichier
            if choix == "3":
                jeu_devinette.lancer(profil_actuel)
            elif choix == "4":
                jeu_calcul.lancer(profil_actuel)
            elif choix == "5":
                jeu_pendu.lancer(profil_actuel)
                
        elif choix == "6":
            mecaniques.afficher_classements()
        elif choix == "7":
            print("Au revoir !")
            break

if __name__ == "__main__":
    menu_principal()
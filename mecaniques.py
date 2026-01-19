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


import json
import os
import random
import time
from datetime import datetime

DATA_DIR = "data"
PROFILES_PATH = os.path.join(DATA_DIR, "profiles.json")


# ========= Utilitaires Fichiers / JSON =========

def dossier_existe(path):
    return os.path.isdir(path)

def creer_dossier(path):
    os.makedirs(path, exist_ok=True)

def lire_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def ecrire_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# ========= Gestion des profils =========

def creer_profil(nom):
    if not dossier_existe(DATA_DIR):
        creer_dossier(DATA_DIR)

    profiles = lire_json(PROFILES_PATH)

    key = nom.lower()
    if key in profiles:
        return None

    nouveau_profil = {
        "nom": nom,
        "date_creation": datetime.now().isoformat(),
        "parties_jouees": 0,
        "score_total": 0,
        "scores_par_jeu": {
            "devinette": 0,
            "calcul_mental": 0,
            "pendu": 0
        },
        "historique_parties": [],
        "succes": {
            "premiere_victoire": False,
            "10_parties": False,
            "score_parfait": False,
            "maitre_calcul": False,
            "pendu_expert": False,
            "score_500": False,
            "score_1000": False
        }
    }

    profiles[key] = nouveau_profil
    ecrire_json(PROFILES_PATH, profiles)
    print("Profil créé avec succès!")
    return nouveau_profil


def charger_profil(nom):
    try:
        profiles = lire_json(PROFILES_PATH)
        key = nom.lower()
        if key in profiles:
            print("Profil chargé!")
            return profiles[key]
        else:
            print("Profil non trouvé")
            return None
    except Exception as e:
        print("Erreur lors du chargement:", e)
        return None


def sauvegarder_profil(joueur):
    try:
        profiles = lire_json(PROFILES_PATH)
        profiles[joueur["nom"].lower()] = joueur
        ecrire_json(PROFILES_PATH, profiles)

        mettre_a_jour_classements()
        mettre_a_jour_historique(joueur)

        print("Profil sauvegardé")
    except Exception as e:
        print("Erreur sauvegarde:", e)


# ========= Classements / Historique (squelettes) =========

def mettre_a_jour_classements():
    # À implémenter si tu veux un fichier de classement global
    pass

def mettre_a_jour_historique(joueur):
    # À implémenter si tu veux un fichier d’historique global
    pass


# ========= Calcul des points =========

def calculer_points_devinette(tentatives, difficulte):
    base = {"facile": 50, "moyen": 100, "difficile": 150}
    points = base.get(difficulte, 0)
    bonus = max(0, 50 - (tentatives * 5))
    return points + bonus

def calculer_points_calcul(reussis, temps_restant, difficulte):
    points = reussis * 10
    bonus = int(temps_restant * 2)
    return points + bonus

def calculer_points_pendu(erreurs, difficulte):
    if erreurs >= 7:
        return 0
    return 100 - (erreurs * 10)


# ========= Succès =========

def verifier_succes(joueur):
    # 1. Première victoire
    if joueur["parties_jouees"] >= 1 and not joueur["succes"].get("premiere_victoire", False):
        joueur["succes"]["premiere_victoire"] = True
        print("Succès débloqué: Première victoire!")

    # 2. 10 parties jouées
    if joueur["parties_jouees"] >= 10 and not joueur["succes"].get("10_parties", False):
        joueur["succes"]["10_parties"] = True
        print("Succès: 10 parties jouées!")

    # 3. Score parfait devinette (<3 tentatives)
    if not joueur["succes"].get("score_parfait", False):
        for partie in joueur["historique_parties"]:
            if partie.get("jeu") == "devinette" and partie.get("tentatives", 999) < 3:
                joueur["succes"]["score_parfait"] = True
                print("Succès: Score parfait!")
                break

    # 4. Maître du calcul (20 réussis)
    if not joueur["succes"].get("maitre_calcul", False):
        total_reussis = 0
        for partie in joueur["historique_parties"]:
            if partie.get("jeu") == "calcul_mental":
                total_reussis += partie.get("reussis", 0)
        if total_reussis >= 20:
            joueur["succes"]["maitre_calcul"] = True
            print("Succès: Maître du calcul!")

    # 5. Expert pendu (0 erreur)
    if not joueur["succes"].get("pendu_expert", False):
        for partie in joueur["historique_parties"]:
            if (
                partie.get("jeu") == "pendu"
                and partie.get("reussi") is True
                and partie.get("erreurs", 1) == 0
            ):
                joueur["succes"]["pendu_expert"] = True
                print("Succès: Expert Pendu!")
                break

    # 6. 500 points
    if joueur["score_total"] >= 500 and not joueur["succes"].get("score_500", False):
        joueur["succes"]["score_500"] = True
        print("🏆 Succès: 500 points atteints!")

    # 7. 1000 points
    if joueur["score_total"] >= 1000 and not joueur["succes"].get("score_1000", False):
        joueur["succes"]["score_1000"] = True
        print("🏆 Succès: 1000 points atteints!")

    return joueur


# ========= Jeux =========

def jouer_devinette(joueur):
    print("=== JEU DE DEVINETTE ===")
    print("1. Facile (1-50)")
    print("2. Moyen (1-100)")
    print("3. Difficile (1-200)")
    difficulte = input("Choix: ")

    if difficulte == "1":
        max_nombre = 50
        niveau = "facile"
    elif difficulte == "2":
        max_nombre = 100
        niveau = "moyen"
    elif difficulte == "3":
        max_nombre = 200
        niveau = "difficile"
    else:
        print("Choix invalide")
        return None

    nombre_secret = random.randint(1, max_nombre)
    tentatives = 0
    MAX_TENTATIVES = 10
    devine = False

    print(f"Je pense à un nombre entre 1 et {max_nombre}")
    print(f"Tu as {MAX_TENTATIVES} tentatives")

    while not devine and tentatives < MAX_TENTATIVES:
        try:
            guess = input("Ta devinette (ou 'q' pour quitter): ")
            if guess == "q":
                print(f"Partie abandonnée. Le nombre était: {nombre_secret}")
                return {
                    "points": 0,
                    "reussi": False,
                    "difficulte": niveau,
                    "jeu": "devinette"
                }
            guess = int(guess)
            tentatives += 1

            if guess < nombre_secret:
                print(f"C'est plus grand! ({MAX_TENTATIVES - tentatives} restantes)")
            elif guess > nombre_secret:
                print(f"C'est plus petit! ({MAX_TENTATIVES - tentatives} restantes)")
            else:
                print(f"Bravo! Tu as trouvé en {tentatives} tentatives!")
                devine = True
        except ValueError:
            print("Erreur: entrez un nombre valide!")

    if devine:
        points = calculer_points_devinette(tentatives, niveau)
        print(f"Tu gagnes {points} points!")
        return {
            "points": points,
            "reussi": True,
            "difficulte": niveau,
            "tentatives": tentatives,
            "jeu": "devinette"
        }
    else:
        print(f"Dommage! Le nombre était: {nombre_secret}")
        return {
            "points": 0,
            "reussi": False,
            "difficulte": niveau,
            "jeu": "devinette"
        }


def jouer_calcul_mental(joueur):
    print("=== CALCUL MENTAL ===")
    print("Tu as 30 secondes pour résoudre des calculs!")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    difficulte = input("Choix: ")

    if difficulte == "1":
        niveau = "facile"
        max_nombre = 20
        operations = ["+", "-"]
    elif difficulte == "2":
        niveau = "moyen"
        max_nombre = 50
        operations = ["+", "-", "*"]
    elif difficulte == "3":
        niveau = "difficile"
        max_nombre = 100
        operations = ["+", "-", "*"]
    else:
        return None

    temps_total = 30
    temps_restant = 30
    reussis = 0
    echoues = 0
    heure_debut = time.time()

    input("C'est parti! Appuie sur ENTRER pour commencer...")

    while temps_restant > 0:
        num1 = random.randint(1, max_nombre)
        num2 = random.randint(1, max_nombre)
        operation = random.choice(operations)

        if operation == "+":
            reponse_attendue = num1 + num2
        elif operation == "-":
            reponse_attendue = num1 - num2
        else:
            reponse_attendue = num1 * num2

        temps_restant = temps_total - int(time.time() - heure_debut)
        if temps_restant <= 0:
            break

        print(f"{num1} {operation} {num2} = ? ({temps_restant}s)")
        try:
            reponse = input("Réponse: ")
            reponse = int(reponse)
            if reponse == reponse_attendue:
                print("Correct!")
                reussis += 1
            else:
                print(f"Mauvais! C'était {reponse_attendue}")
                echoues += 1
        except ValueError:
            print("Entrée invalide!")
            echoues += 1

        temps_restant = temps_total - int(time.time() - heure_debut)

    print("Temps écoulé!")
    print(f"Réussis: {reussis} | Échoués: {echoues}")

    points = calculer_points_calcul(reussis, max(0, temps_restant), niveau)
    return {
        "points": points,
        "reussi": True,
        "difficulte": niveau,
        "reussis": reussis,
        "echoues": echoues,
        "jeu": "calcul_mental"
    }


# ========= Pendu =========

def dessiner_pendu(erreurs):
    etapes = [
        "",
        " O",
        " O\n |",
        " O\n/|",
        " O\n/|\\",
        " O\n/|\\\n |",
        " O\n/|\\\n |\n/",
        " O\n/|\\\n |\n/ \\",
    ]
    return etapes[min(erreurs, len(etapes) - 1)]


def jouer_pendu(joueur):
    print("=== JEU DU PENDU ===")
    print("1. Facile (mots courts)")
    print("2. Moyen (mots moyens)")
    print("3. Difficile (mots longs)")
    difficulte = input("Choix: ")

    if difficulte == "1":
        mots = ["chat", "chien", "maison", "soleil", "lune", "arbre", "fleur", "école"]
        niveau = "facile"
    elif difficulte == "2":
        mots = ["ordinateur", "bibliothèque", "température", "automobile", "electricité"]
        niveau = "moyen"
    elif difficulte == "3":
        mots = ["programmation", "développement", "architecture", "documentation", "implémentation"]
        niveau = "difficile"
    else:
        return None

    mot_secret = random.choice(mots)
    mot_affiche = "_" * len(mot_secret)

    erreurs = 0
    MAX_ERREURS = 7
    lettres_trouvees = set()
    lettres_essayees = set()
    partie_gagnee = False

    while erreurs < MAX_ERREURS and not partie_gagnee:
        print(dessiner_pendu(erreurs))
        print("Mot:", " ".join(mot_affiche))
        print("Lettres essayées:", " ".join(sorted(lettres_essayees)))
        print(f"Erreurs: {erreurs}/{MAX_ERREURS}")

        try:
            lettre = input("Propose une lettre (ou 'q' pour quitter): ").lower()
            if lettre == "q":
                print("Abandon. Le mot était:", mot_secret)
                return {
                    "points": 0,
                    "reussi": False,
                    "difficulte": niveau,
                    "jeu": "pendu"
                }

            if len(lettre) != 1:
                print("Une seule lettre svp!")
                continue

            if lettre in lettres_essayees:
                print("Déjà proposée!")
                continue

            lettres_essayees.add(lettre)

            if lettre in mot_secret:
                print("Lettre trouvée!")
                lettres_trouvees.add(lettre)

                mot_affiche_temp = ""
                for ch in mot_secret:
                    if ch in lettres_trouvees:
                        mot_affiche_temp += ch
                    else:
                        mot_affiche_temp += "_"
                mot_affiche = mot_affiche_temp

                if mot_affiche == mot_secret:
                    print("Gagné! Mot:", mot_secret)
                    partie_gagnee = True
            else:
                print("Pas dans le mot")
                erreurs += 1

        except Exception:
            print("Entrée invalide!")

    if partie_gagnee:
        points = 100 - (erreurs * 10)
        return {
            "points": points,
            "reussi": True,
            "difficulte": niveau,
            "erreurs": erreurs,
            "jeu": "pendu"
        }
    else:
        print("Pendu! Mot:", mot_secret)
        return {
            "points": 0,
            "reussi": False,
            "difficulte": niveau,
            "jeu": "pendu"
        }


# ========= Mise à jour profil après partie =========

def mettre_a_jour_profil(joueur, resultat):
    if resultat is None:
        return joueur

    joueur["parties_jouees"] += 1
    points = resultat.get("points", 0)
    joueur["score_total"] += points

    jeu = resultat.get("jeu")
    if jeu in joueur["scores_par_jeu"]:
        joueur["scores_par_jeu"][jeu] += points

    joueur["historique_parties"].append(resultat)

    joueur = verifier_succes(joueur)
    return joueur


def afficher_classements():
    print("=== Classements ===")
    print("(Classements non implémentés)")

def afficher_succes(joueur):
    print("=== Succès ===")
    for nom_succes, obtenu in joueur["succes"].items():
        statut = "oui" if obtenu else "non"
        print(f"{statut} {nom_succes}")


# ========= Menu Principal (après connexion) =========

def menu_principal(joueur):
    while True:
        print("=========================================")
        print(f"Bienvenue {joueur['nom']}")
        print(f"Score total: {joueur['score_total']} pts")
        print(f"Parties jouées: {joueur['parties_jouees']}")
        print("=========================================")
        print("1. Jouer à la Devinette")
        print("2. Jouer au Calcul Mental")
        print("3. Jouer au Pendu")
        print("4. Consulter Classements")
        print("5. Consulter Succès")
        print("6. Quitter")

        choix = input("Ton choix: ")

        if choix == "1":
            resultat = jouer_devinette(joueur)
            joueur = mettre_a_jour_profil(joueur, resultat)
            sauvegarder_profil(joueur)

        elif choix == "2":
            resultat = jouer_calcul_mental(joueur)
            joueur = mettre_a_jour_profil(joueur, resultat)
            sauvegarder_profil(joueur)

        elif choix == "3":
            resultat = jouer_pendu(joueur)
            joueur = mettre_a_jour_profil(joueur, resultat)
            sauvegarder_profil(joueur)

        elif choix == "4":
            afficher_classements()

        elif choix == "5":
            afficher_succes(joueur)

        elif choix == "6":
            print(f"À bientôt {joueur['nom']} !")
            return


# ========= Programme principal =========

def main():
    while True:
        print("=== CENTRE DE JEUX MULTI-JOUEURS ===")
        print("1. Créer profil")
        print("2. Charger profil")
        print("3. Quitter")

        choix = input("Ton choix: ")

        if choix == "1":
            nom = input("Nom du joueur: ")
            joueur = creer_profil(nom)
            if joueur is not None:
                menu_principal(joueur)
            else:
                print("Profil existe déjà!")

        elif choix == "2":
            nom = input("Nom du joueur: ")
            joueur = charger_profil(nom)
            if joueur is not None:
                menu_principal(joueur)
            else:
                print("Profil non trouvé!")

        elif choix == "3":
            print("Au revoir!")
            break

if __name__ == "__main__":
    main()

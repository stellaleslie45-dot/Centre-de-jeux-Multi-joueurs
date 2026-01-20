# 🎮 Centre de Jeux Multi-joueurs

    Projet Python Fondamental | École IT - Bachelor 1 (Module 1PRJ1)

Le Centre de Jeux Multi-joueurs est une plateforme interactive en console conçue pour offrir une expérience de jeu complète. Créez votre profil, affrontez des défis intellectuels, débloquez des succès et grimpez dans le classement mondial.
### 🚀 Aperçu des Fonctionnalités
### 🕹️ Les Mini-Jeux

    Devinette 🔍 : Trouvez le nombre secret avec trois niveaux de difficulté (1-50, 1-100, 1-200).

    Calcul Mental ⚡ : Un sprint de 30 secondes pour résoudre des opérations (+, -, *).

    Le Pendu 😵 : Devinez le mot caché parmi des listes thématiques avec affichage ASCII dynamique.

### 👤 Gestion des Joueurs

    Profils Persistants : Création et chargement via des fichiers JSON individuels.

    Tableau de Bord : Suivi du score total, du nombre de parties et de la date de création.

    Succès (Achievements) : Plus de 8 succès à débloquer, tels que Première victoire, 10 parties jouées, ou Score parfait.

### 📊 Compétition

    Classements : Top 10 global et Top 5 spécifique par jeu.

    Historique : Suivi des 20 dernières sessions pour analyser vos performances.

### 🏗️ Architecture du Code

Le projet suit une structure modulaire pour une maintenance facilitée :

    main.py : Point d'entrée, gestion du menu principal et de la boucle système.

    profils.py : Logique de création, chargement et sauvegarde des données JSON.

    jeux.py : Moteur logique pour la Devinette, le Calcul mental et le Pendu.

    scores.py : Algorithmes de calcul des points selon la difficulté et la performance.

    succes.py : Système de vérification des conditions d'attribution des trophées. 

⚙️ Installation et Lancement
Prérequis

    Python 3.8 ou plus récent.

    Aucune bibliothèque tierce requise (uniquement les modules standards : json, random, time, os, datetime).

Installation
Bash

### Cloner le dépôt
git clone https://github.com/votre-organisation/centre-jeux-multijoueurs.git

### Accéder au dossier
cd centre-jeux-multijoueurs

### Lancer le programme
python main.py

💾 Structure des Données (JSON)

Les profils sont stockés dans le dossier data/ avec la structure suivante :
<img width="1022" height="480" alt="image" src="https://github.com/user-attachments/assets/6d2c19eb-d6c6-44ff-9b0f-ba620f684ccd" />



### 👥L'Équipe du Projet
Membre	Rôles & Responsabilités
Leslie	Introduction, contexte, gestion de projet, Git (Readme, commits) et conclusion.
Cecilia	Architecture logicielle, développement de la logique des jeux, gestion JSON et démonstration.
🛠️ Gestion des Erreurs

Le système intègre une gestion robuste des exceptions (try/except) pour :

    Prévenir la corruption des fichiers JSON.

    Gérer les entrées utilisateur invalides (lettres au lieu de chiffres, etc.).

    Assurer la continuité du programme même en cas de fichier manquant.

Souhaitez-vous que je génère un exemple de fichier de classements global pour compléter votre dossier data/ ?

### 🧪Tests et exemples d’exécution
Profil du jouer 
<img width="817" height="480" alt="image" src="https://github.com/user-attachments/assets/abebc680-afec-4f58-a53b-6323b1de3d8f" />
Jeux du pendu
<img width="571" height="624" alt="image" src="https://github.com/user-attachments/assets/1c86a81d-b552-49b1-9e10-907e35ddbfcf" />
Jeux calcul mental
<img width="666" height="400" alt="image" src="https://github.com/user-attachments/assets/6ab5d5ff-8c42-46a0-b3ab-317688fbd2d2" />
Jeux du pendu 
<img width="453" height="698" alt="image" src="https://github.com/user-attachments/assets/859cec0b-f38d-470e-aa5f-a5fa6396cf35" />
<img width="415" height="724" alt="image" src="https://github.com/user-attachments/assets/c0642c83-9465-41a2-9a0d-396f7c277181" />

<img width="459" height="693" alt="image" src="https://github.com/user-attachments/assets/902c1fd5-147f-4bf8-bb1e-e081c083e60c" />



### 👥Contributions et organisation de l’équipe

Leslie : Introducrion et contexe (presentation du sujet, objectifs)
          Gestion de projet et git (Historique, commits, Readme, contraintes)

Cecilia : Architecture et code (Structure des fichers, logique des jeux ,json)\
          Conclusion , démonstration 

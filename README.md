# monitoring-basics

Ce script permet de surveiller l'état des services en vérifiant leur disponibilité.

## Prérequis

- Python 3 installé sur la machine
- Flask package installé (`pip install flask`)

## Utilisation
python monitoring.py

1. Définir les services à surveiller en modifiant la liste `services` dans le script `monitoring.py`. Chaque service doit avoir un nom et une adresse (IP ou URL) associés.

2. Exécuter le script `monitoring.py` :

3. Ouvrir un navigateur web et accéder à l'adresse `http://localhost:8000` pour afficher le tableau de monitoring des services.

4. Les états des services seront mis à jour automatiquement en fonction de leur disponibilité.

5. Arrêter le script en appuyant sur `Ctrl + C`.

## Personnalisation

- Vous pouvez personnaliser le template HTML dans le fichier `templates/index.html` pour adapter l'apparence du tableau de monitoring selon vos besoins.

- Vous pouvez également ajouter d'autres services à surveiller en ajoutant des entrées à la liste `services` dans le script `monitoring.py`.

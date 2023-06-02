# Monitoring Service

Ce projet est un système de surveillance simple qui vérifie l'état de différents services en ligne. Il envoie des alertes par e-mail lorsque les services sont indisponibles.

## Prérequis

Avant d'exécuter l'application, assurez-vous d'avoir les éléments suivants installés :

- Python 3.x : https://www.python.org/downloads/
- Flask : Exécutez la commande suivante pour installer Flask : `pip install flask`

## Configuration

Avant de lancer l'application, vous devez configurer les paramètres de messagerie électronique pour l'envoi d'alertes par e-mail. Ouvrez le fichier `monitoring.py` et modifiez les variables suivantes en fonction de vos informations :

- `smtp_server` : l'adresse du serveur SMTP
- `smtp_port` : le port SMTP
- `smtp_username` : le nom d'utilisateur SMTP
- `smtp_password` : le mot de passe SMTP
- `email_from` : l'adresse e-mail de l'expéditeur
- `email_to` : l'adresse e-mail du destinataire des alertes

## Utilisation

1. Clonez le dépôt Git : `git clone https://github.com/m-kis/monitoring-basics.git`
2. Accédez au répertoire du projet : `cd monitoring-basics`
3. Lancez l'application : `python monitoring.py`
4. Ouvrez votre navigateur et accédez à l'URL suivante : `http://localhost:8000`

L'application affichera l'état des services surveillés et enverra des alertes par e-mail lorsque des services sont indisponibles. Vous pouvez ajouter de nouveaux services en utilisant le formulaire sur la page principale.

## Personnalisation

- Pour ajouter ou supprimer des services à surveiller,Vous pouvez simplement le faire depuis l'interface web
- Pour personnaliser l'apparence de l'application, modifiez le fichier `style.css` dans le répertoire `static`.

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet ou signaler des problèmes, n'hésitez pas à ouvrir une issue ou à proposer une pull request.

## Licence

Ce projet est sous licence [MIT](LICENSE).

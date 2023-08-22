# P9-LITRevu-Trissi-MohammadSaleh
Développez une application Web en utilisant Django

LITRevu,

Est une application dédiée aux amateurs de lecture , aux chercheurs, aux critiques littéraires et à tous ceux qui s'intéressent à la littérature et à la recherche académique. Cette plateforme offre une communauté en ligne où les utilisateurs peuvent partager leurs opinions sur des livres et des articles, demander des critiques et découvrir de nouvelles lectures en se basant sur les recommandations d'autres utilisateurs.
Il s'agit d'une application web réalisée avec Django.

## Caractéristiques

1. Inscription / Connexion : 
    - Les utilisateurs peuvent créer un compte en toute simplicité grâce à l'inscription, et se connecter rapidement pour accéder à toutes les fonctionnalités de LITRevu.
1. Flux Personnalisé :
    - Les utilisateurs ont la possibilité de consulter un flux personnalisé qui présente les critiques, les demandes et les activités de leurs abonnements ou lui même. Cela leur permet de suivre les publications de leurs amis.
1. Tri automatique par date :
    - LITRevu propose également un tri automatique par date. Cette fonctionnalité permet aux utilisateurs de visualiser les demandes et les critiques dans l'ordre chronologique, en mettant en avant les publications les plus récentes en premier. 
1. Publier des demandes de critique:
    - Les utilisateurs peuvent créer des demandes de critiques pour des livres ou des articles spécifiques qu'ils souhaitent explorer. Cela permet d'obtenir des recommandations et des avis de la communauté.
1. Publier des critiques:
    - Les critiques peuvent être publiées en réponse à une demande de critique ou indépendamment. Les utilisateurs sont encouragés à partager leurs opinions détaillées sur les œuvres littéraires qu'ils ont lues.
1. Gestion des Publications :
    - Les utilisateurs ont le contrôle total sur leurs demandes et critiques. Ils peuvent les modifier ou les supprimer à tout moment pour refléter leurs évolutions d'opinions ou de besoins.
1. Abonnement et Désabonnement : 
    -  L'application permet aux utilisateurs de s'abonner aux comptes d'autres utilisateurs dont ils apprécient les critiques et le contenu. Ils peuvent également se désabonner à tout moment.
1. Recherche d'Utilisateurs :
    - Une fonction de recherche d'utilisateurs est disponible pour faciliter la recherche et la connexion avec d'autres membres de la communauté.

## Installation & lancement
Commencez tout d'abord par installer Python.  

Lancez la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/SalehTrissi/P9-LITRevu-Trissi-MohammadSaleh.git
```
Placez vous dans le dossier P9-LITRevu-Trissi-MohammadSaleh, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Installez ensuite les packages requis:
```
pip install -r requirements.txt
```
Ensuite, placez vous à la racine du projet (là ou se trouve le fichier manage.py), puis effectuez les migrations:
```
python manage.py makemigrations
```
Puis: 
```
python manage.py migrate
```
Il ne vous reste plus qu'à lancer le serveur: 
```
python manage.py runserver
```
Vous pouvez ensuite utiliser l'applicaton à l'adresse suivante:
```
http://127.0.0.1:8000
```

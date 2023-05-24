# Projet OpenClassrooms "Catégorisez automatiquement des questions"
### Sana TAYS

Le but de ce projet est de créer un algorithme capable de prendre des données textuelles en entrée, en l'occurrence il s'agira de questions issues du forum StackOverflow, et de prédire en sortie quel tag serait le plus pertinent à proposer, afin d'automatiser et faciliter le référencement des questions sur le site.

L'algorithme utilisé ici est une pipeline contenant une étape de feature extraction par le USE (Universal Sentence Encoder) de Tensorflow, ainsi qu'une étape de classification par Régression Logistique. Le modèle pré-entraîné est disponible dans le fichier trained_use_logreg.joblib.

Le modèle est déployé sur une application web via l'outil Streamlit.

Ce répertoire contient notamment :

- un fichier app.py qui est notre API
- un fichier use.py qui contient toutes les fonctions liées à l'utilisation du modèle
- un fichier sttest.py qui contient les informations de l'interface de la web app

___

Afin de pouvoir utiliser l'algorithme, voici la marche à suivre :

- Téléchargez le code de ce répertoire (soit via une commande `git clone` soit en téléchargement direct)
- Ouvrez une ligne de commande et naviguez jusqu'au dossier créé
- Tapez la commande `python app.py` et patientez, cela sert à lancer le serveur
- Dans un nouvel onglet, toujours dans le dossier du répertoire, tapez la commande `streamlit run sttest.py` et une fenêtre devrait s'ouvrir dans votre navigateur.

Si tout fonctionne, vous voyez s'afficher une barre de saisie et l'on vous demande d'entrer du texte.
Si vous saisissez une question sur le thème de l'informatique, vous devriez voir s'afficher un tag recommandé selon le sujet que vous abordez. Si l'algorithme ne sait pas quoi vous recommander, il vous le dira.

Bonne utilisation !
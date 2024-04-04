# projet-developpement

# Installation

## PyCharm

Pour l'utilisation de PyCharm, vous pouvez ouvrir le dossier contenant le projet avec PyCharm, il devrait proposer un
profil d'exécution automatique avec Django. Vous pouvez voir le bouton d'exécution en haut à droite.

![exemple_execution_projet_pycharm.png](documentation%2Fimages%2Fexemple_execution_projet_pycharm.png)

Dans le cas où l'exécution ne fonctionne pas. Il est possible dans un premier temps que vous n'ayez pas le bon
environment de développement. Pour ce faire, vous pouvez cliquer en bas à droite sur la version de Python.

![bouton_interpreteur_python_pycharm.png](documentation%2Fimages%2Fbouton_interpreteur_python_pycharm.png)

Ensuite, cliquez sur "Ajouter un nouvel interpréteur" puis "Ajouter un interpréteur local". Ensuite, vous pouvez cliquer
sur Ok sans rien modifier.

## VSCode 

> Note : il est possible que la commande `python` ne fonctionne pas, dans ce cas, essayez avec `python3`. D'une autre
> part, pour toutes les commandes ci-dessous, vous devrez vous placer dans le dossier du projet.

Pour exécuter le projet avec VSCode, il n'existe pas de bouton d'exécution directe. Dans un premier temps, ouvrez un
terminal (il faut que Python3 soit installé) et créez un environnement virtuel avec la commande `python -m venv venv`.
Cette commande devrait créer un dossier `venv` qui est en fait une version locale et virtualisée de Python.

Lorsque vous aurez créé votre environnement virtuel python, vous devrez (*à chaque fois que vous rouvrirez votre
terminal pour travailler sur ce projet*) exécuter la commande `source venv/bin/activate` sur MacOS et
`./venv/Scripts/Activate.ps1` sur Windows (cette commande a pour objectif de mettre votre terminal dans environment python et de 
pouvoir faire fonctionner le projet).

> Note 2 : Il est aussi possible que lorsque essayiez d'exécuter la commande `./venv/Scripts/Activate.ps1`, vous aillez
> une erreur de permissions, dans ce cas, exécuter la commande : 
> `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force `

Il faut ensuite (une seule fois suffira) exécuter la commande `python -m pip install -r requirements.txt`. Dans le 
dossier `requirements.txt` est stocké ligne par ligne les modules et libraries nécessaires à l'exécution du projet.
Cette commande permet l'installation de ces libraires.

Enfin pour exécuter le projet, il suffit d'exécuter la commande `python manage.py runserver`.

> Note 1 : Si l'erreur : `Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH 
> environment variable? Did you forget to activate a virtual environment?` s'affiche, c'est probablement que vous avez
> oubliés une étape :)
 
# Utilisation de Git 

> Attention : la méthode de travail utilisée ci-dessous est une simplification et une adaptation pour le projet à
> l'ESAIP, certains concepts se retrouvent en entreprise, mais ils sont un peu plus compliqués.

Ce projet est supporté par Git, afin de rester organisés et d'éviter les *conflits*, nous travaillerons avec la méthode
**GitFlow** bien que nous n'utiliserons pas les outils proposés par cette méthode, nous nous en inspirerons grandement.

Cette méthode repose sur l'utilisation des branches avec Git ainsi que l'utilisation de "Pull Requests". Deux branches
principales seront créées : la branche `main` et la branche `dev`. La branche `main` à la branche en production (en
entreprise), il faut à tout prix éviter qu'il y ait des bugs sur cette version, car c'est celle-ci qui est hébergée et
accessible au grand publique. La branche `dev` a pour objectif de réunir les modifications de tout le monde et de corriger
les bugs liés à aggregation des fonctionnalités créées. Lorsqu'une version de la branche `dev` ne contient aucun bug,
cette branche est `merge` avec la branch `main` pour rendre ces modifications publiques.

Lorsque vous travaillerez sur une fonctionnalité, il vous faudra dans un premier temps créer une branche (avec un nom
explicite si possible). Ensuite, vous pourrez travailler tranquillement sur votre fonctionnalité, faire vos commits (
n'oubliez pas de push vos commits)... Lorsque vous pensez avoir fini de travailler sur cette fonctionnalité, vous
pourrez faire ce que l'ont appel une "Pull Request" en vous rendant sur le site de repository du projet sur Github. Vous
aurez sur la page d'accueil quelque chose comme ceci : 

![exemple_accueil_repo_gh.png](documentation%2Fimages%2Fexemple_accueil_repo_gh.png)

Afin de me signaler que vous avez terminés votre travail sur la fonctionnalité sur laquelle vous travaillez, vous pouvez
cliquer sur le bouton "Compare & pull request" associé au nom de la branche sur laquelle vous travaillez. Ensuite, une
interface vous sera proposée, c'est l'interface d'ouverture d'une "Pull Request" :

![exemple_interface_creation_pull_request.png](documentation%2Fimages%2Fexemple_interface_creation_pull_request.png)

Vous pouvez entrer le titre de votre "Pull Request" ainsi qu'une petite description, en bas de la page, vous pourrez
voir la liste des commits que vous avez faits dans la branche ainsi que les modifications faites aux fichiers :

![exemple_interface_creation_pull_request1.png](documentation%2Fimages%2Fexemple_interface_creation_pull_request1.png)

Enfin, vous n'avez plus qu'à cliquer sur le bouton "Create pull request". Je m'occuperai du reste. Dans le cas où il y a
un problème avec votre travail (erreur dans le code, incompréhensions...), l'interface de "Pull Request" permet 
d'envoyer des messages, j'enverrai donc un message *ici*.

## PyCharm

Sur PyCharm, vous pouvez voir le nom de la branche sur laquelle vous êtes actuellement en haut à droite :

![bouton_branche_pycharm.png](documentation%2Fimages%2Fbouton_branche_pycharm.png)

En cliquant sur ce bouton, une interface s'ouvrira, elle vous permet de : créer une branche, changer de branche et push
vos commits. Lorsque vous avez fait vos modifications et voulez "push" celles-ci, vous pouvez ouvrir l'onglet "Commit"
en haut à gauche, juste en dessous de l'onglet "Projet" :

![interface_commit_pycharm.png](documentation%2Fimages%2Finterface_commit_pycharm.png)

Dans le cadre 1, vous pouvez sélectionner les fichiers que vous voulez ajouter dans votre commit. Dans le cadre 2, vous
pouvez entrer le message de description de votre "commit" et le cadre 3 est le bouton de validation du commit. Lorsque
vous avez fait quelques commits (où à chaque commit si vous le souhaitez), vous pouvez "push" vos commits, cet à dire
les envoyer sur le serveur de Github (et donc les rendre accessibles pour tout le monde et les sauvegarder). Pour ce
faire, vous pouvez cliquer sur le bouton dans l'interface suivante : 

![bouton_push_commit.png](documentation%2Fimages%2Fbouton_push_commit.png)

## VSCode

Pour utiliser Git avec une interface, il vous faut premièrement installer l'extension [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens).

![git_lenses_vscode.png](documentation%2Fimages%2Fgit_lenses_vscode.png)

Dans un premier temps, après avoir installé l'extension GitLens, vous pourrez accéder à l'interface de gestion de Git
en cliquant sur le bouton suivant :

![git_lenses_tab_vscode.png](documentation%2Fimages%2Fgit_lenses_tab_vscode.png)

Ensuite, pour créer une branche, vous pouvez suivre les étapes suivantes. La dernière étape permet de sélectionner la
manière dont la branche va être "ouverte", si vous sélectionnez la première option, la branche va simplement être créée
et si vous sélectionnez la seconde option, la branche va être créée et git va vous "mettre directement dans cette
branche", ce qui signifie que lorsque vous ferez des commits, ils se feront dans cette branche.

![ui_creation_branche_vscode.png](documentation%2Fimages%2Fui_creation_branche_vscode.png)
![ui_creation_branche_nom_vscode.png](documentation%2Fimages%2Fui_creation_branche_nom_vscode.png)
![ui_creation_branche_validation_vscode.png](documentation%2Fimages%2Fui_creation_branche_validation_vscode.png)

Pour changer de branche, vous pouvez cliquer sur le bouton suivant : 

![ui_switch_branche_vscode.png](documentation%2Fimages%2Fui_switch_branche_vscode.png)

Lorsque vous aurez fait vos modifications, vous pourrez effectuer votre commit comme vu ci-dessous. Dans un premier
temps, le bouton plus avec marqué "Stage Changes" permet d'ajouter les fichiers au commit (les fichiers que vous
n'ajoutez pas ne seront pas ajouté aux modifications du commit). Ensuite, vous pouvez cliquer sur le bouton "Commit" qui 
permet de valider le commit.

![commits_ui_vscode.png](documentation%2Fimages%2Fcommits_ui_vscode.png)

Enfin, vous pouvez "Push" le commit comme vu ci-dessous avec le bouton "Sync changes" (le nombre affiché correspond au
nombre de commits que vous avez fait) :

![push_ui_vsdode.png](documentation%2Fimages%2Fpush_ui_vsdode.png)
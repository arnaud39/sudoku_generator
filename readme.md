# SUDOKU GENERATOR
Auteur : Arnaud Petit


Ce programme genère aléatoirement n sudoku et les exporte dans un fichier texte. 
La génération se fait de la manière suivante :
- On code une fonction qui permet, suivant un sudoku sous forme d'un array numpy de le résoudre. Cette fonction utilise les principes de la programmation dynamique et du parcours en profondeur de l'arbre des posssibilités. Ce parcours se fait de manière aléatoire.

- On résout n sudokus vierges, le parcours du graph se faisant aléatoirement les solutions sont différentes

- On ajoute une probabilité de disparitition pour chaque chiffre d'une solution complète ce qui permet de rendre la grille incomplète : on a obtenu notre sudoku et on a la garantie qu'une solution non forcément unique existe.





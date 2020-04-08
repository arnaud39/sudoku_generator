# SUDOKU GENERATOR
Auteur : Arnaud Petit


Ce programme genère aléatoirement n sudokus et les exporte dans un fichier texte. 
La génération se fait de la manière suivante :
- On code une fonction qui permet, suivant un sudoku sous forme d'un array numpy de le résoudre. Cette fonction utilise les principes de la programmation dynamique et du parcours en profondeur de l'arbre des posssibilités. Ce parcours se fait de manière aléatoire.

- On résout n sudokus vierges, le parcours du graph se faisant aléatoirement les solutions sont différentes

- On ajoute une probabilité de disparitition pour chaque chiffre d'une solution complète ce qui permet de rendre la grille incomplète : on a obtenu notre sudoku et on a la garantie qu'une solution non forcément unique existe.

Exemple d'output :
```text

   8     |           |           
         |           |         
         |           |         
      9  |  6        |     8     
         |           |         
         |           |         
   2     |  5  8  7  |  3        
         |           |         
-------------------------------
   5  3  |     9     |           
         |           |         
         |           |         
7  9     |     4     |     5  3  
         |           |         
         |           |         
2        |  8  5     |           
         |           |         
-------------------------------
   7     |     3     |           
         |           |         
         |           |         
   3     |  4  6  2  |        5  
         |           |         
         |           |         
4  6     |     7     |     3     
         |           |         




	      ====



5     7  |  3  1     |  6     4  
         |           |         
         |           |         
         |  6        |        7  
         |           |         
         |           |         
6        |           |  3        
         |           |         
-------------------------------
         |     9     |        6  
         |           |         
         |           |         
         |     4     |  8        
         |           |         
         |           |         
2     6  |     5     |  7        
         |           |         
-------------------------------
      5  |  9  3     |           
         |           |         
         |           |         
         |        2  |        5  
         |           |         
         |           |         
      2  |  1  7     |  9  3     
         |           |         

```



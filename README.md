# LINFO1112 - Projet de multiplication de matrices

Ce projet implémente une fonction pour multiplier deux matrices.

## Fonction de multiplication

La fonction `multiply(A, B)` prend deux matrices `A` et `B` en tant que paramètres et retourne leur produit. Voici comment elle fonctionne :

1. Vérifie la compatibilité des dimensions des matrices. Si le nombre de colonnes de la matrice `A` est différent du nombre de lignes de la matrice `B`, une exception de type `DimensionMismatchError` est levée.

2. Crée une matrice vide appelée `multiplied` qui contiendra le résultat final de la multiplication.

3. Itère sur les lignes de la matrice `A`. Pour chaque ligne, itère également sur les colonnes de la matrice `B`.

4. Calcule le produit scalaire entre la ligne courante de `A` et la colonne courante de `B`. Pour ce faire, multiplie chaque élément de la ligne de `A` par l'élément correspondant de la colonne de `B` et ajoute ces produits pour obtenir la somme.

5. Ajoute la somme calculée à la ligne en cours de construction dans la matrice `multiplied`.

6. Une fois que toutes les lignes ont été traitées, la matrice `multiplied` contient le résultat de la multiplication des matrices `A` et `B`. Elle est renvoyée en tant que résultat de la fonction.

## Utilisation

Voici un exemple d'utilisation de la fonction `multiply` :

```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = multiply(A, B)
print(result)

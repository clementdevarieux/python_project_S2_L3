# python_project_S2_L3

# MyBear
MyBear est une librairie Python qui vise à reproduire certaines fonctionnalités de la bibliothèque Pandas. Elle fournit des structures de données flexibles pour la manipulation et l'analyse de données tabulaires.

## Installation
Pour installer MyBear, vous pouvez utiliser pip :

> pip setup.py bdist_wheel sdist
> 
> pip install
> 
> pip freeze (pour s'assurer de la bonne installation)

## Utilisation
Pour commencer, importez les classes et les fonctions nécessaires depuis la librairie :

>from MyBear.dataframe import DataFrame, read_csv, read_json
> 
>from MyBear.dataframe import Series

## Séries
Créez des objets Series en spécifiant un nom et une liste de valeurs :

>serie_test_1 = Series("Test 1", ["1", 2, 3, 4, 5])
>
>serie_test_2 = Series("Test 2", [4, 2, "hello", 4, 18])
> 
>serie_test_3 = Series("Test 3", [14, 12, 19, 14, "118.927"])
> 
>serie_test_4 = Series("Test 4", [1, None, 7, 8])

Vous pouvez accéder aux éléments d'une série en utilisant les propriétés iloc[n] et iloc[a:b] :

>value_1 = serie_test_1.iloc[1]
>
>value_2 = serie_test_3.iloc[2:4]

Pour afficher le contenu d'une série, utilisez la méthode print_series() :

>serie_test_1.print_series()

## DataFrames
Créez un DataFrame à partir de colonnes et de valeurs :


>df_columns_values = DataFrame(
>    column_names=["test_1", "test2"],
>    values=[[11, 21, 3, 4], [3, -4, 1, 9]]
>)

Créez un DataFrame à partir d'une liste de séries :

>df_series = DataFrame(serie_list=[serie_test_1, serie_test_2, serie_test_3])

Vous pouvez afficher le contenu d'un DataFrame en utilisant la méthode print_df() :

>df_columns_values.print_df()

Vous pouvez accéder aux éléments d'un DataFrame en utilisant la méthode iloc[n, n] pour un élément spécifique, ou iloc[a:b, n], iloc[n, a:b], iloc[a:b, x:y] pour des tranches d'éléments :

>df_iloc_n_n = df_series.iloc[2, 1]
> 
>df_iloc_a_b_n = df_series.iloc[1:3, 1]
> 
>df_iloc_n_a_b = df_series.iloc[4, 1:2]
> 
>df_iloc_a_b_x_y = df_series.iloc[1:3, 0:2]

### Lecture de données
Vous pouvez lire des données à partir d'un fichier CSV en utilisant la fonction read_csv() :

>df_csv = read_csv("chemin/vers/le/fichier.csv")

Vous pouvez lire des données à partir d'un fichier JSON en utilisant la fonction read_json() :

> df_json = read_json("chemin/vers/le/fichier.json")

## Jointure de DataFrames
La méthode join() permet de fusionner deux DataFrames :

>left = read_csv("fichier_gauche.csv")
> 
>right = read_csv("fichier_droit.csv")
> 
>result = left.join(other=right, left_on="colonne_gauche", right_on="colonne_droite", how="inner")

Vous pouvez spécifier le type de jointure en utilisant le paramètre how avec les valeurs "inner", "left", "right" ou "outer".

## Groupement de données
La méthode groupby() permet de regrouper les données d'un DataFrame et d'appliquer des fonctions d'agrégation :

>result = df.groupby(by=["colonne_1", "colonne_2"], agg={"colonne_aggregee": fonction_aggregation})

Vous pouvez spécifier une ou plusieurs colonnes pour le regroupement en utilisant le paramètre by, et spécifier les fonctions d'agrégation pour les autres colonnes en utilisant le paramètre agg.

### Exemples supplémentaires
Le fichier d'exemples example.py contient des exemples d'utilisation de la librairie MyBear, y compris la création de séries, de DataFrames, les opérations d'indexation, la lecture de fichiers CSV et JSON, les jointures et les groupements de données.

### Contribuer
Les contributions à MyBear sont les bienvenues ! Si vous avez des suggestions d'amélioration, des rapports de bugs ou si vous souhaitez ajouter de nouvelles fonctionnalités, n'hésitez pas à ouvrir une issue ou à envoyer une pull request.

### Auteurs
Badr Bouaissa
Gabriel Bonjour
Clément Devarieux

### Licence
Ce projet est sous licence privée. Toute utilisation non authorisée sera fortement puni par les trois auteurs magnianimes de cette splendide librairie
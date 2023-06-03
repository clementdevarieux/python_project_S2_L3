from .series import Series
from typing import List, Any, Dict, Callable
import csv
import json


class DataFrame:
    def __init__(
        self,
        column_names: List[str] = None,
        values: List[List[Any]] = None,
        serie_list: List[Series] = None,
    ):
        """
        Initialise une instance de la classe DataFrame.
        Possibilité d'initialiser avec une combinaison nom de colonnes / valeurs associées, ou en entrant une liste de séries.

        Args:
            column_names: Liste des noms de colonnes du DataFrame.
            values: Liste de liste de valeurs des colonnes nommées précédemment
            serie_list: Liste de séries
        """
        self.series = []
        if serie_list is not None:
            self.series = serie_list
        elif column_names is not None and values is not None:
            if len(column_names) != len(values):
                raise ValueError("Size of columns and values not the same")
            for i in range(len(column_names)):
                try:
                    self.series.append(Series(column_names[i], values[i]))
                except IndexError:
                    self.series.append(Series(column_names[i], None))
        else:
            raise ValueError("invalid")

    def _max(self):
        """
        Calcule et retourne la valeur maximale de chaque série du Dataframe.

        Returns:
            Nouveau Dataframe contenant le max de chacune de ses séries.
        """
        name_list = []
        value_list = []
        for serie in self.series:
            name_list.append(serie.name)
            value_list.append([serie._max()])
        max_df = DataFrame(name_list, value_list)
        return max_df

    def print_as_table(self) -> None:
        """
        Affiche le contenu du DataFrame sous forme de tableau.
        """
        if not self.series:
            return
        line = ""
        for serie in self.series:
            line += str(serie.name).ljust(20, " ")
        print(line)
        for line_number in range(len(self.series[0].values)):
            line = ""
            for serie in self.series:
                line += str(serie.values[line_number]).ljust(20, " ")
            print(line)

    def print_df(self) -> None:
        """
        Affiche le contenu du DataFrame sous forme de séries, en donnant les détails de chaque séries.
        """
        for serie in self.series:
            serie.print_series()

    def print_df_values(self) -> None:
        """
        Affiche les valeurs des séries contenues dans le dataframe.
        """
        for serie in self.series:
            print(serie.values)

    def _min(self):
        """
        Calcule et retourne la valeur minimale de chaque série du Dataframe.

        Returns:
            Nouveau Dataframe contenant le min de chacune de ses séries.
        """
        name_list = []
        value_list = []
        for serie in self.series:
            name_list.append(serie.name)
            value_list.append([serie._min()])
        min_df = DataFrame(name_list, value_list)
        return min_df

    def _mean(self):
        name_list = []
        value_list = []
        for serie in self.series:
            name_list.append(serie.name)
            value_list.append([serie._mean()])
        mean_df = DataFrame(name_list, value_list)
        return mean_df

    def _std(self):
        """
        Calcule et retourne l'écart-type de chaque série du Dataframe.

        Returns:
            Nouveau Dataframe contenant l'écart-type de chacune de ses séries.
        """
        name_list = []
        value_list = []
        for serie in self.series:
            name_list.append(serie.name)
            value_list.append([serie._std()])
        std_df = DataFrame(name_list, value_list)
        return std_df

    def _count(self):
        """
        Calcule et retourne le nombre d'éléments de chaque série du Dataframe.

        Returns:
            Nouveau Dataframe contenant le nombre d'éléments de chacune de ses séries.
        """
        name_list = []
        value_list = []
        for serie in self.series:
            name_list.append(serie.name)
            value_list.append([serie._count()])
        count_df = DataFrame(name_list, value_list)
        return count_df

    @property
    def iloc(self):
        """
        Accès aux valeurs d'un dataframe selon différents critères.

        Args:
            index: Position ou plage de positions des valeurs à accéder.

        Returns:
            cas de figure iloc[n, m] : retourne un seul élément, de la ligne n et colonne m
            cas de figure iloc[a:b, n] : retourne une serie contenant les valeurs mentionnées
            cas de figure iloc[n, a:b] : retourne un dataframe qui contient une seule ligne et les valeurs mentionnées
            cas de figure iloc[x:y, a:b] : retourne un dataframe avec les lignes et les colonnes mentionnées


        Raises:
            - TypeError si le format d'entrée d'iloc n'est pas bon.

        Notes:
            - iloc[a, b] --> a sont les lignes, b les colonnes
        """

        class IlocAccessor:
            def __init__(self, dataframe):
                self.dataframe = dataframe

            def __getitem__(self, item):
                if isinstance(item, tuple):
                    ligne, colonne = item

                    if isinstance(ligne, int) and isinstance(colonne, int):
                        serie = self.dataframe.series[colonne]
                        return serie.iloc[ligne]

                    elif isinstance(ligne, slice) and isinstance(colonne, int):
                        serie = self.dataframe.series[colonne]
                        name = serie.name
                        values = serie.iloc[ligne]

                        new_serie = Series(name, values)

                        return new_serie

                    elif isinstance(ligne, int) and isinstance(colonne, slice):
                        name = []
                        values = []
                        start, stop, step = colonne.start, colonne.stop, colonne.step
                        count = 0
                        for serie in self.dataframe.series:
                            if count >= start and count <= stop:
                                name.append(serie.name)
                                values.append([serie.iloc[ligne]])
                            count += 1
                        df = DataFrame(column_names=name, values=values)
                        return df

                    elif isinstance(ligne, slice) and isinstance(colonne, slice):
                        name = []
                        values = []
                        start_col, stop_col, step_col = (
                            colonne.start,
                            colonne.stop,
                            colonne.step,
                        )
                        count = 0
                        for serie in self.dataframe.series:
                            if count >= start_col and count <= stop_col:
                                name.append(serie.name)
                                values.append(serie.iloc[ligne])
                            count += 1
                        df = DataFrame(column_names=name, values=values)
                        return df
                    else:
                        raise TypeError

        return IlocAccessor(self)

    def join(
        self,
        other: "DataFrame",
        left_on: List[str] | str,
        right_on: List[str] | str,
        how: str = "left",
    ) -> "DataFrame":
        """
        Effectue une jointure entre deux DataFrames.

        Args:
            left_df: DataFrame de gauche.
            right_df: DataFrame de droite.
            left_on: Nom de la colonne ou liste de noms de colonnes à utiliser pour la jointure du DataFrame de gauche (par défaut: None).
            right_on: Nom de la colonne ou liste de noms de colonnes à utiliser pour la jointure du DataFrame de droite (par défaut: None).
            how: Type de jointure à effectuer. Les valeurs possibles sont 'inner' (par défaut), 'outer', 'left' et 'right'.

        Returns:
            DataFrame résultant de la jointure.

        Raises:
            ValueError: Si les colonnes spécifiées pour la jointure ne sont pas présentes dans les DataFrames.

        Notes:
            - Si les arguments `left_on` et `right_on` ne sont pas spécifiés, la jointure sera effectuée en utilisant toutes les colonnes avec des noms identiques dans les DataFrames de gauche et de droite.
            - Les types de jointures disponibles sont les suivants:
                - 'inner': Retourne uniquement les enregistrements ayant des correspondances dans les deux DataFrames.
                - 'outer': Retourne tous les enregistrements de chaque DataFrame, combinés là où il y a une correspondance et avec des valeurs manquantes (NaN) là où il n'y a pas de correspondance.
                - 'left': Retourne tous les enregistrements du DataFrame de gauche et les enregistrements correspondants du DataFrame de droite, avec des valeurs manquantes (NaN) là où il n'y a pas de correspondance.
                - 'right': Retourne tous les enregistrements du DataFrame de droite et les enregistrements correspondants du DataFrame de gauche, avec des valeurs manquantes (NaN) là où il n'y a pas de correspondance.
        """
        if how not in ["left", "outer", "right", "inner"]:
            raise ValueError
        outer_on_left = how in ["left", "outer"]
        outer_on_right = how in ["right", "outer"]
        if isinstance(left_on, List) ^ isinstance(right_on, List):
            raise TypeError
        if not isinstance(left_on, List):
            left_on = [left_on]
            right_on = [right_on]
        if len(left_on) == 0 or len(right_on) == 0 or len(left_on) != len(right_on):
            raise ValueError
        left_column_names = [syrie.name for syrie in self.series]
        right_column_names = [syrie.name for syrie in other.series]
        for column_name in left_on:
            if column_name not in left_column_names:
                raise ValueError
        for column_name in right_on:
            if column_name not in right_column_names:
                raise ValueError
        list_of_names = []
        list_of_series = []
        for column_name in left_column_names:
            column_to_append_name = (
                column_name
                if column_name not in left_on
                or column_name == right_on[left_on.index(column_name)]
                else column_name + "|" + right_on[left_on.index(column_name)]
            )
            list_of_names.append(column_to_append_name)
            list_of_series.append(Series(name=column_to_append_name, values=[]))
        for column_name in right_column_names:
            if column_name not in right_on:
                list_of_names.append(column_name)
                list_of_series.append(Series(name=column_name, values=[]))

        for left_line_number in range(len(self.series[0].values)):
            left_part = []
            is_there_a_match_in_right = False
            for column in self.series:
                left_part.append(column.values[left_line_number])
            for right_line_number in range(len(other.series[0].values)):
                check = True in [
                    self.series[left_column_names.index(left_on[i])].values[
                        left_line_number
                    ]
                    == other.series[right_column_names.index(right_on[i])].values[
                        right_line_number
                    ]
                    for i in range(len(left_on))
                ]
                if check:
                    is_there_a_match_in_right = True
                    right_part = []
                    for column in other.series:
                        if column.name not in right_on:
                            right_part.append(column.values[right_line_number])
                    whole_part = left_part + right_part
                    for index in range(len(whole_part)):
                        list_of_series[index].values.append(whole_part[index])
            if outer_on_left and not is_there_a_match_in_right:
                whole_part = left_part + [None] * (
                    len(right_column_names) - len(right_on)
                )
                for index in range(len(whole_part)):
                    list_of_series[index].values.append(whole_part[index])
        if outer_on_right:
            for right_line_number in range(len(other.series[0].values)):
                is_there_a_match_in_left = False
                for left_line_number in range(len(self.series[0].values)):
                    check = True in [
                        self.series[left_column_names.index(left_on[i])].values[
                            left_line_number
                        ]
                        == other.series[right_column_names.index(right_on[i])].values[
                            right_line_number
                        ]
                        for i in range(len(left_on))
                    ]
                    if check:
                        is_there_a_match_in_left = True
                if not is_there_a_match_in_left:
                    whole_part = [None] * (len(left_column_names) - len(right_on))
                    for column in other.series:
                        whole_part.append(column.values[right_line_number])
                    for index in range(len(whole_part)):
                        list_of_series[index].values.append(whole_part[index])
        return DataFrame(serie_list=list_of_series)

    def groupby(self,
                by: List[str] | str,
                agg: Dict[str, Callable[[List[Any]], Any]]
                ) -> "DataFrame":
        """
        Regroupe les données du DataFrame en fonction des colonnes spécifiées et applique des fonctions d'agrégation.

        Args:
            by: Liste des colonnes à utiliser pour le regroupement.
            agg: Dictionnaire des fonctions d'agrégation à appliquer aux autres colonnes.

        Returns:
            DataFrame contenant les résultats du regroupement et de l'agrégation.
        """
        if by == [] :
            raise ValueError
        if isinstance(by, str) :
            by = [by]
        if not isinstance(by, List) :
            raise TypeError
        if not isinstance(agg, Dict) :
            raise TypeError
        for key, value in agg.items() :
            if not isinstance(key, str) or not isinstance(value, Callable) :
                raise TypeError
        column_names = []
        agg_columns_names = []
        for serie in self.series :
            column_names.append(serie.name)
            if serie.name in agg.keys() :
                agg_columns_names.append(serie.name)
        if len(agg.keys()) != len (agg_columns_names) :
            raise ValueError
        for column in by :
            if column not in column_names :
                raise ValueError
            if column in agg.keys() :
                raise ValueError
        for column in agg.values() :
            if not isinstance(column, Callable) :
                raise TypeError
        keys = []
        related_values_lists = []
        for line_number in range(len(self.series[0].values)) :
            by_columns_values = []
            agg_columns_values = []
            for serie in self.series :
                if serie.name in by :
                    by_columns_values.append(serie.values[line_number])
                elif serie.name in agg.keys() :
                    agg_columns_values.append(serie.values[line_number])
            if by_columns_values in keys :
                related_values_lists[keys.index(by_columns_values)].append(agg_columns_values)
            else :
                keys.append(by_columns_values)
                related_values_lists.append([agg_columns_values])
        all_columns = []
        for column_index in range(len(by)) :
            column_values = []
            for key_values in keys :
                column_values.append(key_values[column_index])
            all_columns.append(column_values)
        for column_index in range(len(agg_columns_names)) :
            column_values = []
            for related_values_list in related_values_lists :
                column_values_to_aggregate_into_one = []
                for line in related_values_list :
                    column_values_to_aggregate_into_one.append(line[column_index])
                column_values.append(agg[agg_columns_names[column_index]](column_values_to_aggregate_into_one))
            all_columns.append(column_values)
        return DataFrame(by + agg_columns_names, all_columns)
            

def read_csv(path: str, delimiter: str = ","):
    """
    Charge les données d'un fichier CSV dans un DataFrame.

    Args:
        path: Chemin du fichier CSV à charger.
        delimiter: Délimiteur utilisé dans le fichier CSV (par défaut: ',').

    Returns:
        DataFrame contenant les données du fichier CSV.
    """
    with open(path, newline="") as csvfile:
        value_list = []
        spamreader = csv.reader(csvfile, delimiter=delimiter)
        row = next(spamreader, None)
        name_list = row
        while row is not None:
            row = next(spamreader, None)
            if row is not None:
                for i in range(len(row)):
                    if len(value_list) < len(row):
                        try:
                            value_list.append([int(row[i])])
                        except ValueError:
                            value_list.append([row[i]])
                    else:
                        try:
                            value_list[i].append(int(row[i]))
                        except ValueError:
                            value_list[i].append(row[i])

    return DataFrame(column_names=name_list, values=value_list)


def read_json(path: str):
    """
    Charge les données d'un fichier JSON dans un DataFrame.

    Args:
        file_path: Chemin du fichier JSON à charger.

    Returns:
        DataFrame contenant les données du fichier JSON.
    """
    name_list = []
    value_list = []
    with open(path, encoding="utf-8") as f:
        file = json.load(f)
        for my_dict in file:
            for k, v in my_dict.items():
                if k not in name_list:
                    name_list.append(k)
                    try:
                        value_list.append([int(v)])
                    except ValueError:
                        value_list.append([v])
                elif k in name_list:
                    index = name_list.index(k)
                    try:
                        value_list[index].append(int(v))
                    except ValueError:
                        value_list[index].append(v)
    return DataFrame(column_names=name_list, values=value_list)

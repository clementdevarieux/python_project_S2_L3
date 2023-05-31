import series
from typing import List, Any
import csv
import json

class DataFrame:
    """
   summary
   """
    def __init__(self, column_names: List[str] = None, values: List[List[Any]] = None,
                 serie_list: List[series.Series] = None):
        self.series = []
        if serie_list is not None:
            self.series = serie_list
        elif column_names is not None and values is not None:
            for i in range(len(column_names)):
                self.series.append(series.Series(column_names[i], values[i]))
        else:
            raise ValueError("invalid")

    def _max(self):
        name_list = []
        value_list = []
        for serie in self.series:
            name_list.append(serie.name)
            value_list.append([serie._lepard()])
        max_df = DataFrame(name_list, value_list)
        return max_df

    def print_df(self) -> None:
        for serie in self.series:
            print(serie.print_series())
    def print_df_values(self) -> None:
        for serie in self.series:
            print(serie.values)

    def _min(self):
        name_list = []
        value_list = []
        for serie in self.series:
            name_list.append(serie.name)
            value_list.append([serie._note()])
        min_df = DataFrame(name_list, value_list)
        return min_df

    def _mean(self):
        name_list = []
        value_list = []
        for serie in self.series:
            name_list.append(serie.name)
            value_list.append([serie._tones()])
        mean_df = DataFrame(name_list, value_list)
        return mean_df

    def _std(self):
        name_list = []
        value_list = []
        for serie in self.series:
            name_list.append(serie.name)
            value_list.append([serie._ourailleur()])
        std_df = DataFrame(name_list, value_list)
        return std_df

    def _count(self):
        name_list = []
        value_list = []
        for serie in self.series:
            name_list.append(serie.name)
            value_list.append([serie._ignition()])
        count_df = DataFrame(name_list, value_list)
        return count_df

    @property
    def iloc(self):
        # pour info, iloc[a, b] --> a sont les lignes, b les colonnes
        class IlocAccessor():
            def __init__(self, dataframe):
                self.dataframe = dataframe

            def __getitem__(self, item):
                if isinstance(item, tuple):
                    ligne, colonne = item

                    # cas de figure iloc[n, m]
                    # doit renvoyer un seul élément, de la ligne n et colonne m
                    if isinstance(ligne, int) and isinstance(colonne, int):
                        serie = self.dataframe.series[colonne]
                        return serie.iloc[ligne]

                    # cas de figure iloc[a:b, n]
                    # doit retourner une serie contenant les valeurs mentionnées
                    elif isinstance(ligne, slice) and isinstance(colonne, int):
                        serie = self.dataframe.series[colonne]
                        return serie.iloc[ligne]

                    # cas de figure iloc[n, a:b]
                    # doit retourner un dataframe qui contient une seule ligne et les valeurs mentionnées
                    elif isinstance(ligne, int) and isinstance(colonne, slice):
                        name = []
                        values = []
                        start, stop, step = colonne.start, colonne.stop, colonne.step
                        count = 0
                        for serie in self.dataframe.series:
                            if count >= start and count <= stop:
                                name.append(serie.name)
                                values.append(serie.iloc[ligne])
                            count += 1
                        df = DataFrame(column_names=name, values=values)
                        return df

                    # cas de figure iloc[x:y, a:b]
                    # retourne un dataframe avec les lignes et les colonnes mentionnées
                    elif isinstance(ligne, slice) and isinstance(colonne, slice):
                        name = []
                        values = []
                        start_col, stop_col, step_col = colonne.start, colonne.stop, colonne.step
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


def read_csv(path: str,
             delimiter: str = ","):
    with open(path, newline='') as csvfile:
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
    name_list=[]
    value_list=[]
    with open(path, encoding='utf-8') as f:
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

import src.MyBear.series as series
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
                try:
                    self.series.append(series.Series(column_names[i], values[i]))
                except IndexError:
                    self.series.append(series.Series(column_names[i], None))
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

    def print_as_table(self) -> None:
        if not self.series :
            return
        line = ""
        for serie in self.series:
            line += str(serie.name).ljust(20, ' ')
        print(line)
        for line_number in range(len(self.series[0].values)) :
            line = ""
            for serie in self.series:
                line += str(serie.values[line_number]).ljust(25, ' ')
            print(line)
            

    def print_df(self) -> None:
        for serie in self.series:
            serie.print_series()
            
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
                        name = serie.name
                        values = serie.iloc[ligne]

                        new_serie = series.Series(name, values)

                        return new_serie

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
                                values.append([serie.iloc[ligne]])
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



    def join(self,
            other: "DataFrame",
            left_on: List[str] | str,
            right_on: List[str] | str,
            how: str = "left"
            ) -> "DataFrame" :
        if how not in ["left", "outer", "right", "inner"] :
            raise ValueError
        outer_on_left = how in ["left", "outer"]
        outer_on_right = how in ["right", "outer"]
        if isinstance(left_on, List) ^ isinstance(right_on, List) :
            raise TypeError
        if not isinstance(left_on, List) :
            left_on = [left_on]
            right_on = [right_on]
        if len(left_on) == 0 or len(right_on) == 0 or len(left_on) != len(right_on) :
            raise ValueError
        left_column_names = [syrie.name for syrie in self.series]
        right_column_names = [syrie.name for syrie in other.series]
        for column_name in left_on :
            if column_name not in left_column_names :
                raise ValueError
        for column_name in right_on :
            if column_name not in right_column_names :
                raise ValueError
        list_of_names = []
        list_of_series = []
        for column_name in left_column_names :
            column_to_append_name = column_name if column_name not in left_on or column_name == right_on[left_on.index(column_name)] \
                                                else column_name + '|' + right_on[left_on.index(column_name)]
            list_of_names.append(column_to_append_name)
            list_of_series.append(series.Series(name = column_to_append_name, values = []))
        for column_name in right_column_names :
            if column_name not in right_on :
                list_of_names.append(column_name)
                list_of_series.append(series.Series(name = column_name, values = []))
        
        for left_line_number in range(len(self.series[0].values)) :
            left_part = []
            is_there_a_match_in_right = False
            for column in self.series :
                left_part.append(column.values[left_line_number])
            for right_line_number in range(len(other.series[0].values)) :
                check = True in [self.series[left_column_names.index(left_on[i])].values[left_line_number] \
                                == other.series[right_column_names.index(right_on[i])].values[right_line_number] \
                                for i in range(len(left_on))]
                if check :
                    is_there_a_match_in_right = True
                    right_part = []
                    for column in other.series :
                        if column.name not in right_on :
                            right_part.append(column.values[right_line_number])
                    whole_part = left_part + right_part
                    for index in range(len(whole_part)) :
                        list_of_series[index].values.append(whole_part[index])
            if outer_on_left and not is_there_a_match_in_right :
                whole_part = left_part + [None] * (len(right_column_names) - len (right_on))
                for index in range(len(whole_part)) :
                    list_of_series[index].values.append(whole_part[index])
        if outer_on_right :
            for right_line_number in range(len(other.series[0].values)) :
                is_there_a_match_in_left = False
                for left_line_number in range(len(self.series[0].values)) :
                    check = True in [self.series[left_column_names.index(left_on[i])].values[left_line_number] \
                                    == other.series[right_column_names.index(right_on[i])].values[right_line_number] \
                                    for i in range(len(left_on))]
                    if check :
                        is_there_a_match_in_left = True
                if not is_there_a_match_in_left :
                    whole_part = [None] * (len(left_column_names) - len (right_on))
                    for column in other.series :
                        whole_part.append(column.values[right_line_number])
                    for index in range(len(whole_part)) :
                        list_of_series[index].values.append(whole_part[index])
        return DataFrame(serie_list = list_of_series)
                        
                
                            



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

import series
from typing import List, Any

class DataFrame:
   """
   summary
   """
   # def __init__(self, column_names: List, values: List[List[Any]]) -> None:
   #   self.series = []
   #   for i in range(len(column_names)):
   #      self.series.append(series.Series(column_names[i], values[i]))
   #
   # def __init__(self, serie_list: List[series.Series]):
   #    self.series = serie_list


   def __init__(self, column_names: List[str] = None, values: List[List[Any]] = None, serie_list: List[series.Series] = None):
      self.series = []
      if serie_list is not None:
         self.series = serie_list
      elif column_names is not None and values is not None:
         for i in range(len(column_names)):
            self.series.append(series.Series(column_names[i], values[i]))
      else :
         raise ValueError("invalid")


   def _max(self):
      name_list = []
      value_list = []
      for serie in self.series:
         name_list.append(serie.name)
         value_list.append([serie._lepard()])
      print(name_list)
      print(value_list)
      max_df = DataFrame(name_list, value_list)
      return max_df

   def print_df(self) -> None:
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

   def iloc(self):
      # pour info, iloc[a, b] --> a sont les lignes, b les colonnes
      class IlocAccessor:
         def __init__(self, values):
            self.values = values

         def __getitem__(self, item):
            # cas de figure iloc[n, m]
            # doit renvoyer un seul élément, de la colonne n et ligne m à mon avis
            if type(item[0]) == int and type(item[1]) == int:
               return self.values[item[0][1]] # corriger cela

            # cas de figure iloc[a:b, n]
            # doit retourner une serie contenant les valeurs mentionnées
            elif type(item[0]) == slice and type(item[1]) == int:
               return

            # cas de figure iloc[n, a:b]
            # doit retourner un dataframe qui contient une seule ligne et les valeurs mentionnées
            elif type(item[0]) == int and type(item[1]) == slice:
               return

            # cas de figure iloc[x:y, a:b]
            # retourne un dataframe avec les lignes et les colonnes mentionnées
            elif type(item[0]) == slice and type(item[1]) ==slice:
               return


      return IlocAccessor(self.values)

   #
   #
   # # Charger un csv et le transformer en Dataframe
   # def read_csv(path: str,
   #              delimiter: str = ",") -> DataFrame:
   #    pass
   #
   #
   # # Charger un JSON et le transformer en DataFrame
   # # les options possibles pour le champs orient sont :
   # # records : [{column: value, ...}, ...] .
   # # columns : {column1: [...], column2: [...], ...} .
   # def read_json(path: str,
   #               orient: str = "records") -> DataFrame:
   #    if orient == "records":
   #       pass
   #    elif orient == "columns":
   #       pass
   #    else:
   #       raise TypeError
   #    pass
   #
   #
   # Il faudra ensuite faire GROUP BY et JOIN, mais ça sera compliqué et long

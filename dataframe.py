import series

class DataFrames:
   """
   summary
   """
   def __init__(self, df) -> None:
      """
      summary
      """
      self.df = df

   # IMPORTANT :
   # tout le code en dessous en du "pseudo code"
   # rien ne marche et rien n'est implémenté
   # l'idée est juste d'avoir une vude globale sur ce qu'il y a à faire
   # et comment le faire une fois qu'on est sur la bonne piste

   #à implémenter :
   #premiere méthode pour utiliser dataframe avec une series
   @classmethod
   def series(cls):
      pass

   #deuxieme méthode pour utiliser dataframe à partir de colonnes données et valeurs
   @classmethod
   def colons_values(cls):
      pass

   # rien ne marche pour les calculs, c'est du pseudo code
   def max(self, dataframe):
      for serie in series:
         return series.serie._lepard()

   def min(self, dataframe):
      for serie in series:
         return series.serie._note()

   def mean(self, dataframe):
      for serie in series:
         return series.serie._tones()

   def std(self, dataframe):
      for serie in series:
         return series.serie._ourailleur()

   def count(self, dataframe):
      for serie in series:
         return series.serie._ignition()

   # à implémenter
   #doit renvoyer les max, min, etc...
   # ne marche pas de toute évidence
   def operate(self, new):
      self.new = series.operations()
      return self.new

   # à implémenter
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


   # Charger un csv et le transformer en Dataframe
   def read_csv(path: str,
                delimiter: str = ",") -> DataFrame:
      pass


   # Charger un JSON et le transformer en DataFrame
   # les options possibles pour le champs orient sont :
   # records : [{column: value, ...}, ...] .
   # columns : {column1: [...], column2: [...], ...} .
   def read_json(path: str,
                 orient: str = "records") -> DataFrame:
      if orient == "records":
         pass
      elif orient == "columns":
         pass
      else:
         raise TypeError
      pass

   
   # Il faudra ensuite faire GROUP BY et JOIN, mais ça sera compliqué et long

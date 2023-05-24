import numpy as np

class Series:
   """_summary_
   """
   # Created by Clément and Gabriel
   
   
   def __init__(self, name: str, values: list) -> None:
      """_summary_

      Args:
          name (str): _description_
          values (list): _description_
      """
      # Created by Clément and Gabriel
      if values == []:
         return
      self.name = name
      self.values = values
      self.max = self._lepard()
      self.min = self._note()
      self.mean = self._tones()
      self.std = self._ourailleur()
      self.count = self._ignition()
      #max, min, mean, std (ecart-type) et count
      
   def _lepard (self) -> None:
      """Defines the maximum of this series.
      """
      max = self.values[0]
      for value in self.values :
         if value > max :
            max = value
      return max

   def _note (self) -> None:
      """Defines the minimum of this series.
      """
      min = self.values[0]
      for value in self.values:
         if value < min:
            min = value
      return min

   def _tones (self) -> None:
      """Defines the mean of this series.
      """
      somme = 0
      for value in self.values:
         somme += value
      mean = round((somme / len(self.values)), 2)
      return mean

   def _ourailleur (self) -> None:
      """Defines the standard deviation of this series.
      """
      return np.std(self.values)

   def _ignition (self) -> None:
      """Defines the number of values of this series.
      """
      return len(self.values)

   def print_series(self) -> None:
      print(f'self.name = {self.name}')
      print(f'self.values = {self.values}')
      print(f'self.max = {self._lepard()}')
      print(f'self.min = {self._note()}')
      print(f'self.mean = {self._tones()}')
      print(f'self.std = {self._ourailleur()}')
      print(f'self.count = {self._ignition()}')

   @property
   def iloc(self) :
      class IlocAccessor :
         def __init__(self, values):
            self.values = values

         def __getitem__(self, item):
            if isinstance(item, int):
               return self.values[item]
            elif type(item) == slice:
               start, stop, step = item.indices(len(self.values))
               print(f"start = {start}")
               print(f"stop = {stop}")
               print(f"step = {step}")
               if stop == len(self.values):
                  return [self.values[i] for i in range(start, stop, step)]
               else :
                  return [self.values[i] for i in range(start, stop + 1, step)]
            else :
               raise TypeError("Mauvais format dans iloc")

      return IlocAccessor(self.values)




class DataFrame:
   """The Dashboard receives data from a :ref:`Link`, and prints it on a new
   popped window.

   It can only display data coming from one block.
   """

   def __init__(self,
                verbose: bool = False,
                freq: float = 30) -> None:
      """Sets the args and initializes parent class.

      Args:
         labels (:obj:`list`): Values to plot on the output window.
         nb_digits (:obj:`int`, optional): Number of decimals to show.
         verbose (:obj:`bool`, optional): Display loop frequency ?
         freq (:obj:`float`, optional): If set, the block will loop at this
            frequency.
      """
      super().__init__()
      self.verbose = verbose
      self.freq = freq

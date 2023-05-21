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
      for value in values :
         if value > max :
            max = value
      return max

   def _note (self) -> None:
      """Defines the minimum of this series.
      """
      min = self.values[0]
      for value in values:
         if value < min:
            min = value
      return min

   def _tones (self) -> None:
      """Defines the mean of this series.
      """
      somme = 0
      for value in values:
         somme += value
      mean = round((somme / len(values)), 2)
      return mean

   def _ourailleur (self) -> None:
      """Defines the standard deviation of this series.
      """
      return np.std(values)

   def _ignition (self) -> None:
      """Defines the number of values of this series.
      """
      return len(values)
   
   @property
   def iloc(self) -> Any | Series:
      return self._iloc

   @iloc.setter
   def iloc(self, *args):
      if type(args[0]) == 'int':
         return self.Series(args[0])
      else :
         #mettre en forme pour retourner les lignes voulues
         pass



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

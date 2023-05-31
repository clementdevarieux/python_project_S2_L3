import numpy as np
import statistics

def list_to_int_or_float(list):
    if list is not None:
        my_list= []
        for value in list:
            try:
                my_list.append(int(value))
            except:
                try:
                    my_list.append(float(value))
                except:
                    my_list.append(value)
        return my_list
class Series:
    """_summary_
   """

    # Created by Clément and Gabriel

    def __init__(self, name: str, values:list=[]) -> None:
        """_summary_

      Args:
          name (str): _description_
          values (list): _description_
      """
        self.name = name

        # Created by Clément and Gabriel
        if not values:
            self.values = None
            self.max = None
            self.min = None
            self.mean = None
            self.std = None
            self.count = None

        self.values = list_to_int_or_float(values)
        self.max = self._lepard()
        self.min = self._note()
        self.mean = self._tones()
        self.std = self._ourailleur()
        self.count = self._ignition()
        # max, min, mean, std (ecart-type) et count

    def _lepard(self) -> None:
        """Defines the maximum of this series.
      """
        if self.values is not None:
            try:
                max = self.values[0]
                for value in self.values:
                    if value > max:
                        max = value
            except:
                return None

            return max

    def _note(self) -> None:
        """Defines the minimum of this series.
      """
        if self.values is not None:
            try:
                min = self.values[0]
                for value in self.values:
                    if value < min:
                        min = value
            except:
                return None
            return min

    def _tones(self) -> None:
        """Defines the mean of this series.
      """
        if self.values is not None:
            try:
                somme = 0
                for value in self.values:
                    somme += value
                mean = round((somme / len(self.values)), 2)
            except:
                return None
            return mean

    def _ourailleur(self) -> None:
        """Defines the standard deviation of this series.
      """
        if self.values is not None:
            try:
                return round(np.std(int(self.values)), 4)
            except:
                return None

    def _ignition(self) -> None:
        """Defines the number of values of this series.
      """
        try:
            return len(self.values)
        except:
            return None

    def print_series(self) -> None:
        print(f'Nom = {self.name}')
        print(f'Values = {self.values}')
        print(f'Max = {self._lepard()}')
        print(f'Min = {self._note()}')
        print(f'Mean = {self._tones()}')
        print(f'Ecart-type = {self._ourailleur()}')
        print(f'Nombre = {self._ignition()}')


    @property
    def iloc(self):
        class IlocAccessor:
            def __init__(self, series):
                self.series = series

            def __getitem__(self, item):
                if isinstance(item, int):
                    return self.series.values[item]
                elif isinstance(item, slice):
                    start, stop, step = item.indices(len(self.series.values))
                    if stop >= start:
                        if stop == len(self.series.values):
                            return [self.series.values[i] for i in range(start, stop, step)]
                        else:
                            return [self.series.values[i] for i in range(start, stop + 1, step)]
                    else:
                        if stop < 0:
                            return [self.series.values[i] for i in range(start)]
                        else:
                            return [self.series.values[i] for i in range(stop, start + 1, step)]
                else:
                    raise TypeError("Mauvais format dans iloc")

        return IlocAccessor(self)

import numpy as np
import statistics


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
        # Created by Clément and Gabriel
        if not values:
            return
        self.name = name
        self.values = values
        self.max = self._lepard()
        self.min = self._note()
        self.mean = self._tones()
        self.std = self._ourailleur()
        self.count = self._ignition()
        # max, min, mean, std (ecart-type) et count

    def _lepard(self) -> None:
        """Defines the maximum of this series.
      """
        max = self.values[0]
        for value in self.values:
            if value > max:
                max = value
        return max

    def _note(self) -> None:
        """Defines the minimum of this series.
      """
        min = self.values[0]
        for value in self.values:
            if value < min:
                min = value
        return min

    def _tones(self) -> None:
        """Defines the mean of this series.
      """
        somme = 0
        for value in self.values:
            somme += value
        mean = round((somme / len(self.values)), 2)
        return mean

    def _ourailleur(self) -> None:
        """Defines the standard deviation of this series.
      """
        return np.std(self.values)

    def _ignition(self) -> None:
        """Defines the number of values of this series.
      """
        return len(self.values)

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

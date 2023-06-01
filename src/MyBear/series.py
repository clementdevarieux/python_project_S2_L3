import numpy as np


class Series:
    """_summary_"""

    # Created by Clément and Gabriel

    def list_to_int_or_float(self, list):
        if list is not None:
            my_list = []
            for value in list:
                try:
                    my_list.append(int(value))
                except:
                    try:
                        my_list.append(float(value))
                    except:
                        my_list.append(value)
            return my_list

    def __init__(self, name: str, values: list = []) -> None:
        """_summary_

        Args:
            name (str): _description_
            values (list): _description_
        """
        self.name = name

        # Created by Clément and Gabriel

        self.values = self.list_to_int_or_float(values)
        self.max = self._max()
        self.min = self._min()
        self.mean = self._mean()
        self.std = self._std()
        self.count = self._count()
        self.missing = self._missing()
        self.type = self._type()
        # max, min, mean, std (ecart-type) et count

    def _missing(self) -> None:
        count = 0
        try:
            for value in self.values:
                if value == '' or value is None:
                    count += 1
            return count
        except:
            return None

    def _type(self) -> None:
        type_list = []
        if self.values is not None:
            try:
                for value in self.values:
                    if type(value) not in type_list:
                        type_list.append(type(value))
                if len(type_list) == 1:
                    return type_list[0]
                else:
                    raise TypeError
            except:
                return None

    def _max(self) -> None:
        """Defines the maximum of this series."""
        if self.values is not None:
            try:
                max = self.values[0]
                for value in self.values:
                    if value > max:
                        max = value
            except:
                return None

            return max

    def _min(self) -> None:
        """Defines the minimum of this series."""
        if self.values is not None:
            try:
                min = self.values[0]
                for value in self.values:
                    if value < min:
                        min = value
            except:
                return None
            return min

    def _mean(self) -> None:
        """Defines the mean of this series."""
        if self.values is not None:
            try:
                somme = 0
                for value in self.values:
                    somme += value
                mean = round((somme / len(self.values)), 2)
            except:
                return None
            return mean

    def _std(self) -> None:
        """Defines the standard deviation of this series."""
        if self.values is not None:
            try:
                if len(self.values) != 0:
                    return round(np.std(self.values), 4)
            except:
                return None

    def _count(self) -> None:
        """Defines the number of values of this series."""
        try:
            return len(self.values)
        except:
            return None

    def print_series(self) -> None:
        print(f"Nom = {self.name}")
        print(f"Values = {self.values}")
        print(f"Max = {self._max()}")
        print(f"Min = {self._min()}")
        print(f"Mean = {self._mean()}")
        print(f"Ecart-type = {self._std()}")
        print(f"Nombre = {self._count()}")
        print(f"Nombre de valeurs manquantes = {self._missing()}")
        print(f"Type = {self._type()}")

    @property
    def iloc(self):
        class IlocAccessor:
            def __init__(self, series):
                self.series = series

            def __getitem__(self, item):
                if isinstance(item, int):
                    return self.series.values[item]
                elif isinstance(item, slice):
                    start, stop = item.start, item.stop
                    new_serie = []
                    if stop >= start:
                        if stop == len(self.series.values):
                            for i in range(start, stop):
                                new_serie.append(self.series.values[i])
                            return new_serie
                        elif stop > len(self.series.values):
                            for i in range(start, len(self.series.values)):
                                new_serie.append(self.series.values[i])
                            return new_serie
                        else :
                            for i in range(start, stop + 1):
                                new_serie.append(self.series.values[i])
                            return new_serie
                    else:
                        raise ValueError("mauvais ordre")
                else:
                    raise TypeError("Mauvais format dans iloc")

        return IlocAccessor(self)

import numpy as np


class Series:
    def list_to_int_or_float(self, list) -> list:
        """
        Convertit les éléments d'une liste en entiers ou en flottants.

        Args:
            data_list: Liste contenant les données à convertir.

        Returns:
            Liste contenant les éléments convertis en entiers ou en flottants.

        """
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
        """
        Initialise une instance de la classe Series avec les données spécifiées.

        Args:
            data: Nom de la série, et liste des valeurs de la série.
        """
        self.name = name

        self.values = self.list_to_int_or_float(values)
        self.max = self._max()
        self.min = self._min()
        self.mean = self._mean()
        self.std = self._std()
        self.count = self._count()
        self.missing = self._missing()
        self.type = self._type()
        # max, min, mean, std (ecart-type) et count

    def _missing(self) -> int:
        """
        Indique le nombre de valeurs manquantes dans la série

        Return:
            Nombre de valeur vides de la série.

        """
        count = 0
        try:
            for value in self.values:
                if value == "" or value is None:
                    count += 1
            return count
        except:
            return None

    def _type(self) -> type:
        """
        Indique le type des données présentes dans la série, si elles sont toutes de même nature.
        Au cas contraire, raise un TypeError

        Returns:
            Type des valeurs de la série
        """
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

    def _max(self) -> int | float:
        """
        Calcule et retourne la valeur maximale de la série.

        Returns:
            Valeur maximale de la série.
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

    def _min(self) -> int | float:
        """
        Calcule et retourne la valeur minimale de la série.

        Returns:
            Valeur minimale de la série.
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

    def _mean(self) -> int | float:
        """
        Calcule et retourne la moyenne des valeurs de la série.

        Returns:
            Moyenne des valeurs de la série.
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

    def _std(self) -> int | float:
        """
        Calcule et retourne l'écart-type des valeurs de la série.

        Returns:
            Écart-type des valeurs de la série.
        """
        if self.values is not None:
            try:
                if len(self.values) != 0:
                    return round(np.std(self.values), 4)
            except:
                return None

    def _count(self) -> int:
        """
        Calcule et retourne le nombre total de valeurs dans la série.

        Returns:
            Nombre total de valeurs dans la série.
        """
        try:
            return len(self.values)
        except:
            return None

    def print_series(self) -> None:
        """
        Affiche les informations de la série, y compris les valeurs et le nombre de valeurs manquantes.
        """
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
        """
        Accès aux valeurs d'une série par position.

        Args:
            index: Position ou plage de positions des valeurs à accéder.

        Returns:
            - Si l'index est un entier, retourne la valeur correspondante à cette position.
            - Si l'index est une plage de positions (slice), retourne une nouvelle série contenant les valeurs incluses dans cette plage.

        Raises:
            - TypeError si le format d'entrée d'iloc n'est pas bon.

        Notes:
            - Les positions des valeurs dans une série commencent à zéro.
            - L'index peut être un entier ou une plage de positions.
            - Si l'index spécifié est en dehors de la plage valide des positions lors d'un slice, cela retournera le slice entre le start, et le dernier élément de la série.
            - Si l'index spécifié est en dehors de la plage valide des positions lors d'un slice, cela retournera le slice entre le start, et le dernier élément de la série.
            - La méthode iloc ne modifie pas la série d'origine.
        """

        class IlocAccessor:
            def __init__(self, series):
                self.series = series

            def __getitem__(self, item):
                if isinstance(item, int):
                    if item > len(self.series.values):
                        return self.series.values[len(self.series.values) - 1]
                    elif item < 0:
                        return self.series.values[0]
                    else:
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
                        else:
                            for i in range(start, stop + 1):
                                new_serie.append(self.series.values[i])
                            return new_serie
                    else:
                        raise ValueError("mauvais ordre")
                else:
                    raise TypeError("Mauvais format dans iloc")

        return IlocAccessor(self)

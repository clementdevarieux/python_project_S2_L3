

#  .'"'.        ___,,,___        .'``.
# : (\  `."'"```         ```"'"-'  /) ;
#  :  \                         `./  .'
#   `.                            :.'
#     /        _         _        \
#    |         0}       {0         |
#    |         /         \         |
#    |        /           \        |
#    |       /             \       |
#     \     |      .-.      |     /
#      `.   | . . /   \ . . |   .'
#  jgs   `-._\.'.(     ).'./_.-'
#            `\'  `._.'  '/'
#              `. --'-- .'
#                `-...-'


import numpy as np
import test
import series

def main():
    serie_test = series.Series("Test", [1, 2, 3, 4, 5])
    serie_test.print_series()
    value_1 = serie_test.iloc[1]
    serie_1 = serie_test.iloc[2:7]
    serie_2 = serie_test.iloc[1:3]
    print(f'iloc[3] vaut {value_1}')
    print(f'iloc[2:7] vaut {serie_1}')
    print(f'iloc[1:3] vaut {serie_2}')

if __name__ == "__main__" :
    main()



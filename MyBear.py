

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
import dataframe

def main():
    serie_test = series.Series("Test", [1, 2, 3, 4, 5])
    value_1 = serie_test.iloc[1]
    serie_test.operations()
    print(f"iloc[1]= {value_1}")
    #dataframe(serie_test).operate(serie_test)

if __name__ == "__main__" :
    main()



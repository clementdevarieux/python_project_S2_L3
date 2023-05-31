

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
    serie_test_1 = series.Series("Test 1", [1, 2, 3, 4, 5])
    serie_test_2 = series.Series("Test 2", [4, 2, 9, 4, 18])
    serie_test_3 = series.Series("Test 3", [14, 12, 19, 14, 118])

    serie_list = [serie_test_1, serie_test_2, serie_test_3]
    #
    # # value_1 = serie_test.iloc[1]
    # # serie_test.print_series()
    # # print(f"iloc[1]= {value_1}")
    # df_test = dataframe.DataFrame(column_names=["test_1", "test2"], values=[[1,2],[3,4]])
    #
    df_test_series = dataframe.DataFrame(serie_list=serie_list)
    df_iloc = df_test_series.iloc[2:4, 1:2]
    df_iloc.print_df()
    #df = df_test._count()
    # df = df_test._max()
    # df_2 = df_test_series._std()
    # df_2.print_df()
    # df.print_df()
    # df_csv = dataframe.read_csv("test_csv.csv")
    # df_json = dataframe.read_json("test_json.json")
    # print(df)
    # df = dataframe.read_csv("test_csv.csv")
    # df_csv.print_df()
    # print("json")
    # df_json.print_df_values()



if __name__ == "__main__" :
    main()



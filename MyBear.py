

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
    # serie_test_1 = series.Series("Test 1", ["hellof"])
    # serie_test_2 = series.Series("Test 2", ["1.5"])
    # serie_list = [serie_test_1, serie_test_2]
    #
    # # value_1 = serie_test.iloc[1]
    # # serie_test.print_series()
    # # print(f"iloc[1]= {value_1}")
    # df_test = dataframe.DataFrame(column_names=["test_1", "test2"], values=[[1,2],[3,4]])
    #
    # df_test_series = dataframe.DataFrame(serie_list=serie_list)
    # df_test_series.print_df()
    # #df = df_test._count()
    # df = df_test._max()
    # df_2 = df_test_series._std()
    # df_2.print_df()
    # df.print_df()
    # df_csv = dataframe.read_csv("test_csv.csv")
    # df_json = dataframe.read_json("test_json.json")
    # # print(df)
    # # df = dataframe.read_csv("test_csv.csv")
    # df_csv.print_df()
    # print("json")
    # df_json.print_df_values()

    left = dataframe.read_csv("join_test_left.csv")
    right = dataframe.read_csv("join_test_right.csv")
    left.print_as_table()
    print("------")
    right.print_as_table()
    print("------")
    patate = left.join(other = right, left_on = "EMPDEPT", right_on = "DEPTNAME", how = "inner")
    patate.print_as_table()
    print("------")
    patate = left.join(other = right, left_on = "EMPDEPT", right_on = "DEPTNAME", how = "left")
    patate.print_as_table()
    print("------")
    patate = left.join(other = right, left_on = "EMPDEPT", right_on = "DEPTNAME", how = "right")
    patate.print_as_table()
    print("------")
    patate = left.join(other = right, left_on = "EMPDEPT", right_on = "DEPTNAME", how = "outer")
    patate.print_as_table()
    


if __name__ == "__main__" :
    main()



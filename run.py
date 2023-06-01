from MyBear.dataframe import DataFrame

serie = DataFrame(
    column_names=["test_1", "test2"], values=[[11, 21, 3, 4], [3, 4, 1, 9]]
)

serie.print_df()
# MyBear.print_df(serie)

from MyBear.dataframe import DataFrame, read_csv, read_json
from MyBear.dataframe import Series


# SERIES:
# Création de 3 séries pour effectuer des tests dessus
serie_test_1 = Series("Test 1", ["1", 2, 3, 4, 5])
serie_test_2 = Series("Test 2", [4, 2, "hello", 4, 18])
serie_test_3 = Series("Test 3", [14, 12, 19, 14, "118.927"])
serie_test_4 = Series("Test 4", [1, None, 7, 8])

# Vérification de la propriété iloc[n]
value_1 = serie_test_1.iloc[1]
print(f"iloc[n] = {value_1}\n")

# Vérification de la propriété iloc[a:b]
value_2 = serie_test_3.iloc[2:4]
print(f"iloc[a:b] = {value_2}\n")

# Print de la serie
print("serie test 1")
serie_test_1.print_series()
print("\n")

# Verification de propriété valeur manquante pour série
print("serie test 4")
serie_test_4.print_series()
print("\n")

# DATAFRAMES:
# Création d'un dataframe à partir de colonnes et valeurs
df_columns_values = DataFrame(
    column_names=["test_1", "test2"], values=[[11, 21, 3, 4], [3, -4, 1, 9]]
)

# Création d'une liste de séries
serie_list = [serie_test_1, serie_test_2, serie_test_3]

# Création d'un dataframe à partir d'une liste de series
df_series = DataFrame(serie_list=serie_list)

# Print des deux dataframes
print("_____")
print(f"df_columns_values to print = {df_columns_values.print_df()}\n")
print("_____")
print(f"df_series = {df_series.print_df()}\n")
print("_____")
# Verifications pour iloc[n, n]
df_iloc_n_n = df_series.iloc[2, 1]
print(df_iloc_n_n)
print("\n")

# Verifications pour iloc[a:b, n]

df_iloc_a_b_n = df_series.iloc[1:3, 1]
df_iloc_a_b_n.print_series()
print("\n")

# Verifications pour iloc[n, a:b]
df_iloc_n_a_b = df_series.iloc[4, 1:2]
df_iloc_n_a_b.print_as_table()
print("\n")

# Verifications pour iloc[a:b, x:y]
df_iloc_a_b_x_y = df_series.iloc[1:3, 0:2]
print(type(df_iloc_a_b_x_y))
df_iloc_a_b_x_y.print_as_table()
print("\n")

# Verification du CSV
df_csv = read_csv("files/test_csv.csv")
df_csv.print_df()
print("\n")

# Verification du JSON
df_json = read_json("files/test_json.json")
df_json.print_df()
print("\n")

df_json_records = read_json("files/test_json_records.json", orient="records")
df_json_records.print_df()

# Vérification de la méthode join
left = read_csv("files/join_test_left.csv")
right = read_csv("files/join_test_right.csv")
left.print_as_table()
print("------")
right.print_as_table()
print("------")
patate = left.join(other=right, left_on="EMPDEPT", right_on="DEPTNAME", how="inner")
patate.print_as_table()
print("------")
patate = left.join(other=right, left_on="EMPDEPT", right_on="DEPTNAME", how="left")
patate.print_as_table()
print("------")
patate = left.join(other=right, left_on="EMPDEPT", right_on="DEPTNAME", how="right")
patate.print_as_table()
print("------")
patate = left.join(other=right, left_on="EMPDEPT", right_on="DEPTNAME", how="outer")
patate.print_as_table()

# Vérification de la méthode groupby
right = read_csv("files/group_by_test.csv")
right.print_as_table()
print("-----")
# agg : TypeError
# right.groupby(by="fhk", agg={"gfbb", print})
# # agg.keys() : TypeError
# right.groupby(by="fhk", agg={3: print})
# # agg.keys() : ValueError
# right.groupby(by="fhk", agg={"gfbb": print})
# # by : TypeError
# right.groupby(by=3, agg={"DEPTNAME": print})
# # by : ValueError
# right.groupby(by="fdhkvbfdkb", agg={"DEPTNAME": print})
# # groupby OK for a single column
right.groupby(by="DEPTNAME", agg={"DEPTID": max}).print_as_table()
# # groupby OK for multiple columns
right.groupby(by=["DEPTNAME", "LOCATION"], agg={"DEPTID": max}).print_as_table()

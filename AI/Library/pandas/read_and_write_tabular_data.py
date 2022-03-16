import pandas as pd 

filename = "student_marks.csv"

"""read_csv() function to read data from the csv
 file """
 
titanic = pd.read_csv(filename)
# display whole data
# print(titanic)

# display first 8 dataframe
print(titanic.head(8))

# check pandas dataframe column datatypes ot dtypes
# dtypes of each column will be listed
print(titanic.dtypes)

# converting to spreadsheet or excel
titanic.to_excel('titanic.xlsx', sheet_name="passengers", index=False)
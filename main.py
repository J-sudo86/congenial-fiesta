import pandas

titanic = pandas.read_csv("titanic.csv")

print(titanic.iloc[10:20, 1:5])

#changing the values of a dataset for some row and a certain amount of columns
titanic.iloc[2:5, 2] = "Ronald McDonald"

print(titanic["Name"])

#saving a dataframe as a csv file
#titanic.to_csv("revised_titanic.txt")

#adding a new column
titanic["NewColumn"] = titanic["Fare"] * 2
print(titanic)

#we want to make a pair of columns
titanic["Alive Money Index"] = titanic["Fare"] * titanic["Survived"]
print(titanic)

#renaming a column
renamedcolumn = titanic.rename(columns={"Siblings/Spouses Aboard": ";("})
print(renamedcolumn.info())
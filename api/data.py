from Database import Database
import pandas as pd

def initDataInDB(db: Database) -> None:
    createCategoryTable(db)
    if len(db.all("SELECT * FROM category", [])) < 1:
        msg, category = readDataCSV("data.csv")
        for i in range(len(msg)):
            db.run("INSERT INTO category (msg, category) VALUES(?,?)", (str(msg[i]), str(category[i])))
    return SplitSQLiteData(db.all("SELECT * FROM category", []))

def createCategoryTable(db: Database) -> None:
    db.run("""CREATE TABLE IF NOT EXISTS category (
           msg TEXT NOT NULL,
           category TEXT NOT NULL
    )""", [])

def readDataCSV(file: str):
    data = pd.read_csv(file, sep=';')
    msg_column = data["msg"]
    category_column = data["category"]
    return list(msg_column), list(category_column)

def SplitSQLiteData(result: list):
    msg_list = [row[0] for row in result]
    category_list = [row[1] for row in result]
    return msg_list, category_list

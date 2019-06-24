import mysql.connector
from mysql.connector import Error
from db_config_data import read_db_config


TABLENAME   = "123TESTS"

data =  {
            "TABLENAME" :   None,
            "VALUES"    :   None,
            "data"      :   None,
            "commands"  :
            {
                "MySQL" :
                {
                    "mydb"       :   None,
                    "cursor"     :   None
                },
                "cursor":
                {
                    "createTable":   "CREATE TABLE " + TABLENAME + " (%(values)s)",
                    "insertInto" :   "INSERT INTO "  + TABLENAME + " (firstName, secondName, age, lol) VALUES (%s, %s, %s, %s)",
                    "selectFrom" :   "SELECT * FROM " + TABLENAME
                }
            }
        }



mydb        = data["commands"]["MySQL"]["mydb"]
cursor      = data["commands"]["MySQL"]["cursor"]
createTable_= data["commands"]["cursor"]["createTable"]
insertInto  = data["commands"]["cursor"]["insertInto"]
selectFrom  = data["commands"]["cursor"]["selectFrom"]

TABLENAME   = data["TABLENAME"]
VALUES      = data['VALUES']
push_data   = data['data']
def connect():
    """ Connect to MySQL database """
    db_data = read_db_config()
    try:
        mydb    =   mysql.connector.connect(**db_data)
        cursor  =   mydb.cursor()
        if mydb.is_connected(): print('Connected Done!')
        else:                   print("Connected Denied!")
    except Error as e:          print('Connected Access')
    else:                       return mydb,cursor

def createTable(command):
    try:
        cursor.execute(command)
        print("Created table!")
        return True
    except Error as e:
        print(e)
        return False

def pushData(sqlFormula, data):
    try:
        typeOfData = type(data)
        if typeOfData == list:
            cursor.executemany(sqlFormula, data)
        elif typeOfData == tuple:
            cursor.execute(sqlFormula,data)
        mydb.commit()
        print("Data was pushed!")
    except Error as e:
        print(e)

def seeData():
    cursor.execute(selectFrom)
    myresult = cursor.fetchall()
    return [row for row in myresult]


def main(data):
    createTable(command = createTable_ % VALUES)
    pushData(data=data, sqlFormula = insertInto)
    print(seeData())
if __name__ == '__main__':
    CONNECTtoDB = connect()
    mydb        = CONNECTtoDB[0]
    cursor      = CONNECTtoDB[1]
    VALUES      =   {
                        "values":   "firstName VARCHAR(255) , secondName VARCHAR(255), age VARCHAR(255), lol VARCHAR(255)"
                    }
    push_data       =   [
                            ("Я"     , "Ебал"   , "Эту" ,   "Хуйню")
                        ]
    main(data = push_data)
    mydb.close()

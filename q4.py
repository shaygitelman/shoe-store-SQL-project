import mysql.connector

if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port="3307"
    )
    cursor = mydb.cursor()

    #ALTER TABLE = ADD/DROP COL/ CHANGE THE TABLE
    cursor.execute("""
    ALTER TABLE size
    ADD COLUMN uk_number TINYINT DEFAULT 0;
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("UK column added successfully to size table.")

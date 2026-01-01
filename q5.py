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
    ALTER TABLE upcoming
    ADD COLUMN pre_order_available BIT DEFAULT 0;
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("pre_order_available column added successfully.")


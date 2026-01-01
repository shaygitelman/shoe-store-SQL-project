import mysql.connector

if __name__ == "__main__":
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port="3307"
    )
    cursor = mydb.cursor()

    # Select all data from the view created earlier
    # SELECT does not modify the DB, so no commit
    cursor.execute("SELECT * FROM total_sales_per_shoe;")

    # Print all rows returned by the view
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()

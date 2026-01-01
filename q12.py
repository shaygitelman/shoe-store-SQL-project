import mysql.connector

if __name__ == "__main__":
    # Connect to the BIU Shoes database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port="3307"
    )
    cursor = mydb.cursor()

    # Query to find all shoes that have never been ordered
    query = """
    SELECT DISTINCT s.shoe_name
    FROM shoe s
    WHERE s.shoe_id NOT IN (
        SELECT os.shoe_id
        FROM order_shoe os
    );
    """

    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()

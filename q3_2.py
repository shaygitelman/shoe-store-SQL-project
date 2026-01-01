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

    cursor.execute("""
    INSERT INTO size (size_id, european_number, us_number) VALUES
    (1, 35, 5),
    (2, 36, 5),
    (3, 37, 6),
    (4, 38, 7),
    (5, 39, 8),
    (6, 40, 9),
    (7, 41, 9),
    (8, 42, 10),
    (9, 43, 10),
    (10, 44, 11),
    (11, 45, 12),
    (12, 46, 13),
    (13, 47, 14),
    (14, 48, 15),
    (15, 49, 16);
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Inserted sizes successfully.")

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
    INSERT INTO order_shoe (order_id, shoe_id) VALUES
    (1, 3),
    (1, 5),
    (2, 7),
    (2, 1),
    (3, 10),
    (4, 12),
    (4, 3),
    (5, 8),
    (6, 2),
    (6, 7),
    (7, 14),
    (8, 1),
    (9, 9),
    (9, 4),
    (10, 6),
    (10, 11),
    (11, 15),
    (12, 10),
    (13, 13),
    (14, 20),
    (15, 19),
    (15, 18);
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Inserted order_shoe records successfully.")

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
    INSERT INTO shoe_size (shoe_id, size_id) VALUES
    (1, 4), (1, 5), (1, 6),
    (2, 7), (2, 8), (2, 9),
    (3, 1), (3, 2), (3, 3),
    (4, 4), (4, 5), (4, 6), (4, 7),
    (5, 3), (5, 4), (5, 5),
    (6, 10), (6, 11), (6, 12),
    (7, 8), (7, 9), (7, 10), (7, 11),
    (8, 5), (8, 6), (8, 7),
    (9, 12), (9, 13), (9, 14),
    (10, 4), (10, 5), (10, 6),
    (11, 6), (11, 7), (11, 8),
    (12, 9), (12, 10), (12, 11),
    (13, 7), (13, 8), (13, 9),
    (14, 3), (14, 4), (14, 5),
    (15, 11), (15, 12), (15, 13),
    (16, 8), (16, 9), (16, 10),
    (17, 5), (17, 6), (17, 7),
    (18, 4), (18, 5), (18, 6),
    (19, 12), (19, 13), (19, 14),
    (20, 7), (20, 8), (20, 9);
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Inserted shoe_size mappings successfully.")

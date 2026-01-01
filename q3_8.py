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
    INSERT INTO company_order (order_id, order_date) VALUES
    (1, '2025-01-05 10:00:00'),
    (2, '2025-01-10 12:30:00'),
    (3, '2025-01-15 16:45:00'),
    (4, '2025-02-01 09:20:00'),
    (5, '2025-02-10 18:10:00'),
    (6, '2025-02-18 11:40:00'),
    (7, '2025-03-02 14:00:00'),
    (8, '2025-03-10 17:55:00'),
    (9, '2025-03-21 08:10:00'),
    (10, '2025-04-05 19:30:00'),
    (11, '2025-04-18 13:25:00'),
    (12, '2025-05-01 09:45:00'),
    (13, '2025-05-11 15:30:00'),
    (14, '2025-05-20 20:00:00'),
    (15, '2025-06-02 10:10:00');
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Inserted company orders successfully.")

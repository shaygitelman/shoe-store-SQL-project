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
    INSERT INTO order_customer (order_id, customer_id) VALUES
    (1, '123456789'),
    (2, '987654321'),
    (3, '555222111'),
    (4, '444333222'),
    (5, '111222333'),
    (6, '222333444'),
    (7, '333444555'),
    (8, '666777888'),
    (9, '777888999'),
    (10, '999888777'),
    (11, '123456789'),
    (12, '987654321'),
    (13, '555222111'),
    (14, '444333222'),
    (15, '111222333');
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Inserted order_customer records successfully.")

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
    INSERT INTO customer (customer_id, first_name, last_name, email, city_id) VALUES
    ('123456789', 'Daniel', 'Cohen', 'daniel.cohen@example.com', 1),
    ('987654321', 'Shira', 'Levi', 'shira.levi@example.com', 2),
    ('555222111', 'John', 'Smith', 'john.smith@example.com', 3),
    ('444333222', 'Emily', 'Brown', 'emily.brown@example.com', 4),
    ('111222333', 'Michael', 'Johnson', 'michael.johnson@example.com', 5),
    ('222333444', 'Sarah', 'Williams', 'sarah.williams@example.com', 6),
    ('333444555', 'David', 'Miller', 'david.miller@example.com', 7),
    ('666777888', 'Laura', 'Wilson', 'laura.wilson@example.com', 8),
    ('777888999', 'Adam', 'Taylor', 'adam.taylor@example.com', 9),
    ('999888777', 'Emma', 'Anderson', 'emma.anderson@example.com', 10);
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Inserted customers successfully.")

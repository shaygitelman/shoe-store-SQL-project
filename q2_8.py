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
    CREATE TABLE company_order (
        order_id INT,
        order_date DATETIME NOT NULL,
        PRIMARY KEY (order_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Table 'company_order' created successfully.")

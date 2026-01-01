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
    CREATE TABLE order_customer (
        order_id INT,
        customer_id VARCHAR(15),
        FOREIGN KEY (order_id) REFERENCES company_order(order_id),
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Table 'order_customer' created successfully.")

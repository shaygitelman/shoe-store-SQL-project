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
    CREATE TABLE customer (
        customer_id VARCHAR(15),
        first_name VARCHAR(31) NOT NULL,
        last_name VARCHAR(31) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        city_id INT NOT NULL,
        CHECK (LENGTH(customer_id) = 9),
        PRIMARY KEY (customer_id),
        FOREIGN KEY (city_id) REFERENCES city(city_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Table 'customer' created successfully.")

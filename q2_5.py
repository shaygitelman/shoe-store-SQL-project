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
    CREATE TABLE country (
        country_id INT,
        country_name VARCHAR(63) NOT NULL,
        PRIMARY KEY (country_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Table 'country' created successfully.")

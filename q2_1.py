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
    CREATE TABLE shoe (
        shoe_id INT,
        shoe_name VARCHAR(31) NOT NULL,
        price SMALLINT NOT NULL,
        PRIMARY KEY (shoe_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Table 'shoe' created successfully.")

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
    CREATE TABLE size (
        size_id INT,
        european_number TINYINT NOT NULL,
        us_number TINYINT,
        PRIMARY KEY (size_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Table 'size' created successfully.")

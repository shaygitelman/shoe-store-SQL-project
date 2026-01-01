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
    CREATE TABLE upcoming (
        special_id INT,
        shoe_id INT NOT NULL,
        collection_name VARCHAR(31),
        release_date DATETIME,
        PRIMARY KEY (special_id),
        FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Table 'upcoming' created successfully.")

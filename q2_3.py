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
    CREATE TABLE shoe_size (
        shoe_id INT,
        size_id INT,
        FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id),
        FOREIGN KEY (size_id) REFERENCES size(size_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Table 'shoe_size' created successfully.")

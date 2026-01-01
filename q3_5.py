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
    INSERT INTO country (country_id, country_name) VALUES
    (1, 'Israel'),
    (2, 'United States'),
    (3, 'Canada'),
    (4, 'United Kingdom'),
    (5, 'France'),
    (6, 'Germany'),
    (7, 'Italy'),
    (8, 'Spain'),
    (9, 'Japan'),
    (10, 'Australia');
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Inserted countries successfully.")

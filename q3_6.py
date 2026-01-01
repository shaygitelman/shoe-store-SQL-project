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
    INSERT INTO city (city_id, city_name, country_id) VALUES
    (1, 'Tel Aviv', 1),
    (2, 'Jerusalem', 1),
    (3, 'New York', 2),
    (4, 'Los Angeles', 2),
    (5, 'Toronto', 3),
    (6, 'Vancouver', 3),
    (7, 'London', 4),
    (8, 'Manchester', 4),
    (9, 'Paris', 5),
    (10, 'Lyon', 5);
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Inserted cities successfully.")

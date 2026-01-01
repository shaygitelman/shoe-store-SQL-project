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
    INSERT INTO upcoming (special_id, shoe_id, collection_name, release_date) VALUES
    (1, 1, 'CS Special Edition', '2025-01-15 10:00:00'),
    (2, 3, 'Retro Classics', '2025-02-01 09:00:00'),
    (3, 5, 'Superstar Gold', '2025-03:10 12:00:00'),
    (4, 7, 'HyperFlux Neon', '2025-04-20 18:00:00'),
    (5, 10, 'Echo Limited', '2025-05-05 11:30:00'),
    (6, 12, 'Apex Ultra', '2025-06-01 08:00:00'),
    (7, 14, 'Stride Blackout', '2025-07-17 14:00:00'),
    (8, 16, 'Infinity Prime', '2025-08-09 16:00:00'),
    (9, 18, 'Pace Elite', '2025-09-03 10:00:00'),
    (10, 19, 'Canyon Limited', '2025-10-21 19:30:00'),
    (11, 20, 'Sky High Night Edition', '2025-11-11 21:00:00'),
    (12, 8, 'Nebula Rare Drop', '2025-12-01 13:00:00');
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

    print("Inserted upcoming special releases successfully.")

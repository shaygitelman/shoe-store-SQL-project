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
    SELECT 
        s.shoe_name,
        COUNT(ss.size_id) AS sizes_available
    FROM shoe s
    LEFT JOIN shoe_size ss 
        ON s.shoe_id = ss.shoe_id
    GROUP BY s.shoe_id, s.shoe_name
    ORDER BY sizes_available DESC;
    """)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    mydb.close()

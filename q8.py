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
        s.european_number,
        s.us_number,
        AVG(sh.price) AS avg_price
    FROM size s, shoe_size ss, shoe sh
    WHERE s.size_id = ss.size_id
      AND ss.shoe_id = sh.shoe_id
    GROUP BY s.european_number, s.us_number
    ORDER BY avg_price DESC;
    """)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    mydb.close()

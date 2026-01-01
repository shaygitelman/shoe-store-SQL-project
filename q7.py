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
        c.first_name,
        c.last_name,
        SUM(s.price) AS total_amount
    FROM customer c, order_customer oc, order_shoe os, shoe s
    WHERE c.customer_id = oc.customer_id
      AND oc.order_id = os.order_id
      AND os.shoe_id = s.shoe_id
    GROUP BY c.customer_id
    ORDER BY total_amount DESC;
    """)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    mydb.close()

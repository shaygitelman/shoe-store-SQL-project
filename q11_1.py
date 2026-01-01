import mysql.connector

if __name__ == "__main__":
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port="3307"
    )
    cursor = mydb.cursor()

    # Create a view summarizing total revenue per shoe
    # Using the OLD JOIN STYLE (FROM a, b WHERE ...)
    cursor.execute("""
    CREATE VIEW total_sales_per_shoe AS
    SELECT 
        s.shoe_id,                     -- The unique identifier of the shoe
        s.shoe_name,                   -- The name of the shoe
        SUM(s.price) AS total_revenue  -- Total revenue = price * number of times sold
    FROM shoe s, order_shoe os
    WHERE s.shoe_id = os.shoe_id       -- OLD JOIN condition: match shoes with their orders
    GROUP BY s.shoe_id, s.shoe_name;   -- One row per shoe, aggregating the revenue
    """)

    # Commit because this VIEW creation modifies the database
    mydb.commit()

    cursor.close()
    mydb.close()

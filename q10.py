import mysql.connector

if __name__ == "__main__":
    # Establish connection to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port="3307"
    )
    
    cursor = mydb.cursor()

    # SQL query combining inventory shoes and upcoming releases
    # Using UNION ALL because we do not need to remove duplicates
    # and performance is better.
    query = """
    -- Step 1: Get all shoe names from the inventory with a fixed label 'Inventory'
    SELECT 
        shoe_name AS name,
        'Inventory' AS source
    FROM shoe

    UNION ALL

    -- Step 2: Get all upcoming collection names with the label 'Upcoming Release'
    SELECT 
        collection_name AS name,
        'Upcoming Release' AS source
    FROM upcoming

    -- Sort everything alphabetically by name
    ORDER BY name;
    """

    # Execute the query
    cursor.execute(query)

    # Fetch and print results
    results = cursor.fetchall()
    for row in results:
        print(row)   # Each row will be (name, source)

    # Clean up
    cursor.close()
    mydb.close()

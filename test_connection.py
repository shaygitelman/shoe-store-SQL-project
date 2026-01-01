import mysql.connector

if __name__ == "__main__":
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            port="3307"
        )
        print("Connected successfully!")
        mydb.close()
    except Exception as e:
        print("Connection failed:", e)

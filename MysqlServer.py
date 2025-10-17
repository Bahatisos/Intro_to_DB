from mysql.connector import connect, Error


def create_database():
    try:
        # Establish connection to MySQL Server
        connection = connect(
            host="localhost",
            user=input("Enter MySQL username: "),
            password=input("Enter MySQL password: ")
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Properly close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")


# Run the function
if __name__ == "__main__":
    create_database()

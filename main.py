import pymysql

# Replace these values with your actual database configuration
host = 'localhost'
user = 'root'
password = 'Surya@123'
database = 'lung_cancer'

try:
    # Establish the connection
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=database
    )

    print(connection)
    # Create a cursor
    cursor = connection.cursor()

    # Execute a SELECT query
    # sql_query = ""
    # cursor.execute(sql_query)
    #
    # # Fetch and print the results
    # results = cursor.fetchall()
    # for row in results:
    #     print(row)

except pymysql.Error as e:
    print(f"Error: {e}")

finally:
    cursor.close()
    connection.close()

import psycopg2

# Lambda function to connect to the database
connect_to_database = lambda: psycopg2.connect(
    host="localhost",
    user="juliousername",
    password="juliopassword",
    database="juliodatabase"
)

create_cursor = lambda connection: connection.cursor()

execute_query = lambda cursor, query: cursor.execute(query)

connection = connect_to_database()

try:
    # Call the lambda function to create a cursor
    cursor = create_cursor(connection)

    # Call the lambda function to execute a query
    execute_query(cursor, "SELECT * FROM users")

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error occurred while connecting to PostgreSQL:", error)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
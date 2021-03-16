import csv
import mysql.connector

def check_id_exist(id):
    query = f"SELECT * FROM customer WHERE customerid = {id};"
    mycursor.execute(query)
    row_count = mycursor.rowcount
    if row_count == 0:
        return False
    return True

if __name__ == '__main__':
    training_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="dev_training_1"
    )

    mycursor = training_db.cursor(buffered=True)

    with open('customer.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        table_name = "customer"

        mycursor.execute("SHOW TABLES LIKE 'customer'")
        check = mycursor.fetchone()
        for row in csv_reader:
            first_row = row
            break
        if not check:

            query_create_table = f"CREATE TABLE {table_name} ({row[0]} int PRIMARY KEY"

            for column in first_row[1:]:
                query_create_table += f", {column} VARCHAR(50)"
            query_create_table += ")"
            
            mycursor.execute(query_create_table)

        column_name = ", ".join(first_row)

        for row in csv_reader:
            id = int(row[0])
            if not check_id_exist(id):
                insert_query = f"INSERT INTO customer({column_name}) values({id}"
                for ele in row[1:]:
                    insert_query += ", '" + ele + "'"
                insert_query += ")"
                mycursor.execute(insert_query)
                training_db.commit()
        
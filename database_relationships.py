import sqlite3

# with DatabaseContextManager("relationships") as db:
#     db.execute(query, parameters)

# "Foreign key table"
# Table = "Customers"
# Fields = [customer_id,first_name, last_name, age, Foreign Key (company_id) References Companies(company_id)]

# Table = "Companies"
# Fields = [company_id, company_name, employee_count]

# JOIN OUTPUT: 1,John,johnathan, 30, 2 , 2 , Google, 500


class DatabaseContextManager(object):

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

#------------------------Customer and Company Tables----------------------

def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first name TEXT,
    last_name TEXT,
    age INTEGER,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES Companies(company_id))"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)


def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    employee_count TEXT)"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)

# ------------------------Customer CRUD------------------------
# CRUD stands for Create, Read, Update, Delete

# Create function Customer
def create_customers(first_name: str, last_name: str, age: int, company_id: int):
    query = """INSERT INTO Customers(first_name, last_name, age, company_id) VALUES(?,?,?,?)"""
    parameters = [first_name, last_name, age, company_id]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


# Read function Customer
def get_customers(first_name):
    query = """SELECT * FROM Customer
               WHERE first_name = ?"""
    parameters = [first_name]
    with DatabaseContextManager("relationships") as cursor:
        cursor.execute(query, parameters)
        for record in cursor.fetchall():
            print(record)
    print("------------------------------------------------------")
    # print for convenience in terminal


# Update function Customer
def update_customers_first_name(db, old_first_name: str, new_first_name: str):
    query = """UPDATE Customers
                SET first_name = ?, 
                WHERE first_name = ?"""
    parameters = [db, new_first_name, old_first_name]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


# Delete function Customer
def delete_customers(first_name: str):
    query = """DELETE FROM Customers
                WHERE first_name = ?"""
    parameters = [first_name]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


# ------------------------Companies CRUD------------------------
def create_companies(company_name: str, employee_count: str):
    query = """INSERT INTO Companies(company_name, employee_count) VALUES(?, ?)"""
    parameters = [company_name, employee_count]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("relationhips") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_companies_name(old_employee_count: str, new_employee_count: str):
    query = """UPDATE Companies
                SET employee_count = ?
                WHERE employee_count = ?"""
    parameters = [new_employee_count, old_employee_count]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


def delete_companies(employee_name: str):
    query = """DELETE FROM Companies
                WHERE employee_name = ?"""
    parameters = [employee_name]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


def get_customers_companies():
    query = """SELECT * FROM Customers
                JOIN Companies
                    ON Customers.company_id = Companies.company_id"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


def drop_table():
    query = """DROP TABLE Company
    with DatabaseContextManager("relationships") as db:
        db.execute(query)


create_table_customer()
create_table_company()
create_customer("Jonas", "Jonis", 30)
create_customer("Briana", "Winkle", 34)
create_company("Derbies", 341)
create_cpmpany("Gilda", 498)
get_customers()
get_companies()

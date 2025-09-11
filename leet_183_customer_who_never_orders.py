import sqlite3

def run_query(sql_query, customers, orders):
    # connect to an in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    # create tables
    cur.execute("""
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            customerId INTEGER
        )
    """)

    # insert test data
    cur.executemany("INSERT INTO customers (id, name) VALUES (?, ?)", customers)
    cur.executemany("INSERT INTO orders (id, customerId) VALUES (?, ?)", orders)

    # run your SQL query
    cur.execute(sql_query)
    rows = cur.fetchall()

    conn.close()
    return rows


if __name__ == "__main__":
    # put your query here (needs to alias the output column as 'Customers')
    sql = """
    SELECT name AS Customers
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customerId
    WHERE o.id IS NULL;
    """

    # Example test cases
    test1_customers = [(1,"Joe"),(2,"Henry"),(3,"Sam"),(4,"Max")]
    test1_orders    = [(1,3),(2,1)]
    print("Test1:", run_query(sql, test1_customers, test1_orders))  
    # expected ['Henry','Max']

    test2_customers = [(1,"A"),(2,"B")]
    test2_orders    = [(10,1),(11,2)]
    print("Test2:", run_query(sql, test2_customers, test2_orders))  
    # expected []

    test3_customers = [(1,"A"),(2,"B"),(3,"C")]
    test3_orders    = []
    print("Test3:", run_query(sql, test3_customers, test3_orders))  
    # expected ['A','B','C']

    test4_customers = [(1,"A"),(2,"B"),(3,"C")]
    test4_orders    = [(10,1),(11,1),(12,1)]
    print("Test4:", run_query(sql, test4_customers, test4_orders))  
    # expected ['B','C']

    test5_customers = [(1,"Alex"),(2,"Alex"),(3,"Bob")]
    test5_orders    = [(10,1)]
    print("Test5:", run_query(sql, test5_customers, test5_orders))  
    # expected ['Alex','Bob']


"""
Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
 

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
"""
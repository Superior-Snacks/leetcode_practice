import sqlite3
def run_query(sql_query, data):
    # connect to an in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    # create table
    cur.execute("""
        CREATE TABLE Employee (
            id INTEGER PRIMARY KEY,
            name TEXT,
            salary INTEGER,
            managerId INTEGER
        )
    """)

    # insert test data
    cur.executemany("INSERT INTO Employee (id, name, salary, managerId) VALUES (?, ?, ?, ?)", data)

    # run your SQL query
    cur.execute(sql_query)
    rows = cur.fetchall()

    conn.close()
    return rows


# Example usage:
if __name__ == "__main__":
    sql = """
    -- paste your solution here
    SELECT E.name AS Employee
    FROM Employee E
    JOIN Employee M
      ON E.managerId = M.id
    WHERE E.salary > M.salary;
    """

    test1 = [
        (1, "Joe", 70000, 3),
        (2, "Henry", 80000, 4),
        (3, "Sam", 60000, None),
        (4, "Max", 90000, None)
    ]
    print("Test1:", run_query(sql, test1))   # expected [('Joe',)]

    test2 = [
        (1, "Alice", 50000, 2),
        (2, "Bob", 60000, None)
    ]
    print("Test2:", run_query(sql, test2))   # expected []

    test3 = [
        (1, "Tom", 100000, 2),
        (2, "Jerry", 90000, None)
    ]
    print("Test3:", run_query(sql, test3))   # expected [('Tom',)]
"""
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
"""
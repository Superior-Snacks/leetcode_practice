import sqlite3
def run_query(sql_query, data):
    # connect to an in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    # create table
    cur.execute("""
        CREATE TABLE person (
            id INTEGER PRIMARY KEY,
            email TEXT
        )
    """)

    # insert test data
    cur.executemany("INSERT INTO person (id, email) VALUES (?, ?)", data)

    # run your SQL query
    cur.execute(sql_query)
    rows = cur.fetchall()

    conn.close()
    return rows

# Example usage:
if __name__ == "__main__":
    sql = """
    -- paste your solution here
    """
    test1 = [
        [[1, "a@b.com"], [2, "c@d.com"], [3, "a@b.com"]]
    ]
    print("Test1:", run_query(sql, test1))   # expected ['a@b.com']

    test2 = [
        [[1, "x@y.com"], [2, "z@y.com"], [3, "x@y.com"], [4, "z@y.com"], [5, "w@y.com"]]
    ]
    print("Test2:", run_query(sql, test2))   # expected ['x@y.com','z@y.com']

    test3 = [
        [[1, "only@one.com"]]
    ]
    print("Test3:", run_query(sql, test3))   # "expected []"

    """
    Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.
    """
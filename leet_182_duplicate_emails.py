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
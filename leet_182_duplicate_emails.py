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
    print(sol.findDuplicateEmails(
        [[1, "a@b.com"], [2, "c@d.com"], [3, "a@b.com"]]
    ), "expected ['a@b.com']")

    print(sol.findDuplicateEmails(
        [[1, "x@y.com"], [2, "z@y.com"], [3, "x@y.com"], [4, "z@y.com"], [5, "w@y.com"]]
    ), "expected ['x@y.com','z@y.com']")

    print(sol.findDuplicateEmails(
        [[1, "only@one.com"]]
    ), "expected []")
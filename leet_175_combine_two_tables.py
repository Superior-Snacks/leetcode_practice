# Write your MySQL query statement below
import sqlite3
def personAddress():
    # 1) connect (use ':memory:' for an in-memory DB)
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()

    # 2) create tables
    cur.execute("""
    CREATE TABLE Person (
    personId   INTEGER PRIMARY KEY,
    lastName   TEXT,
    firstName  TEXT
    )
    """)
    cur.execute("""
    CREATE TABLE Address (
    addressId  INTEGER PRIMARY KEY,
    personId   INTEGER,
    city       TEXT,
    state      TEXT
    )
    """)

    # 3) insert data (ALWAYS parameterize!)
    cur.executemany(
        "INSERT INTO Person (personId, lastName, firstName) VALUES (?, ?, ?)",
        [(1, 'Wang', 'Allen'), (2, 'Alice', 'Bob')]
    )
    cur.executemany(
        "INSERT INTO Address (addressId, personId, city, state) VALUES (?, ?, ?, ?)",
        [(1, 2, 'New York City', 'New York'), (2, 3, 'Leetcode', 'California')]
    )
    conn.commit()
    """
    Output: 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
    """
    # 4) run SQL (example LEFT JOIN)
    cur.execute("""
    SELECT
    """)
    rows = cur.fetchall()

    # 5) use results in Python
    for r in rows:
        print(r)

    cur.close()
    conn.close()


personAddress()
"""print(sol.personAddress(
    person=[{"personId": 1, "lastName": "Wang", "firstName": "Allen"},
            {"personId": 2, "lastName": "Alice", "firstName": "Bob"}],
    address=[{"addressId": 1, "personId": 2, "city": "New York City", "state": "New York"},
             {"addressId": 2, "personId": 3, "city": "Leetcode", "state": "California"}]
), "expected: [[Allen, Wang, Null, Null], [Bob, Alice, New York City, New York]]")

print(sol.personAddress(
    person=[{"personId": 10, "lastName": "Smith", "firstName": "John"}],
    address=[]
), "expected: [[John, Smith, Null, Null]]")

print(sol.personAddress(
    person=[{"personId": 1, "lastName": "Doe", "firstName": "Jane"},
            {"personId": 2, "lastName": "Roe", "firstName": "Richard"}],
    address=[{"addressId": 5, "personId": 1, "city": "Chicago", "state": "Illinois"}]
), "expected: [[Jane, Doe, Chicago, Illinois], [Richard, Roe, Null, Null]]")"""
"""
SQL Schema
Pandas Schema
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key (column with unique values) for this table.
This table contains information about the ID of some persons and their first and last names.
 
Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key (column with unique values) for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.
 
Write a solution to report the first name, last name, city, and state of each person in the Person table. 
If the address of a personId is not present in the Address table, report null instead.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input: 
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output: 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
Explanation: 
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.s
"""
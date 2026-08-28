# Easy SQL

Working with a database often means managing connections, cursors, and repeated
SQL statements. The `easy_sql` module provides beginner-friendly helpers around
Python's built-in `sqlite3` module so common database tasks are easier to read.

## A small real-world example

Imagine you're planning a trip and want to keep a wishlist of destinations with
an estimated budget for each one. You can save the destinations, then find the
trips that fit within the amount you have available.

```python
from py_simple import open_db, run_insert, conditional_run_select

connection, cursor = open_db(":memory:")

cursor.execute("""
    CREATE TABLE destinations (
        city TEXT,
        country TEXT,
        estimated_budget INTEGER
    )
""")

destinations = [
    ["Lisbon", "Portugal", 1500],
    ["Kyoto", "Japan", 1800],
    ["Reykjavik", "Iceland", 2600],
]

for destination in destinations:
    run_insert(
        connection,
        cursor,
        destination,
        "destinations",
        ["city", "country", "estimated_budget"],
    )

budget_limit = 2000
affordable_trips = conditional_run_select(
    connection,
    cursor,
    "destinations",
    "city, country, estimated_budget",
    "estimated_budget <= ?",
    (budget_limit,),
)

print(f"Trips within ${budget_limit:,}:")
for city, country, budget in affordable_trips:
    print(f"{city}, {country}: ${budget:,}")

connection.close()
```

Example output:

```text
Trips within $2,000:
Lisbon, Portugal: $1,500
Kyoto, Japan: $1,800
```

## What happened?

`open_db()` opened an in-memory SQLite database and returned the connection and
cursor needed for the other helpers. Using `:memory:` keeps the example
temporary, so no database file is created on your computer.

`run_insert()` added each destination to the `destinations` table. It matched
the values in each list to the `city`, `country`, and `estimated_budget`
columns and saved the changes.

`conditional_run_select()` selected only destinations whose estimated budget
was at or below the limit. The `?` placeholder kept the budget value separate
from the SQL condition, and `(budget_limit,)` supplied the value for that
placeholder.

If you want every destination instead, use `run_select()`. The module also
includes `run_delete()` for removing rows that match a condition and
`delete_all_from_table()` for emptying a table while keeping the table itself.

## Why use these helpers?

Without `easy_sql`, you would need to build and execute each SQLite statement
yourself, fetch the results, and remember when to commit changes. These helpers
keep common database operations short and readable while still using familiar
SQL concepts such as tables, columns, conditions, and parameter placeholders.

## SQL / Relational Databases

#### CRUD:

- create
- read
- update
- delete

CREATE TABLE table (column type, ...)

#### Data types:

- BLOB
- INTEGER 
    - smallint
    - integer - 32 bits
    - bigint - 64 bits
- NUMERIC
    - boolean
    - date
    - datetime
    - numeric (scale, precision)
    - time
    - timestamp
- REAL
    - real - 32 bits
    - double precision - 64 bits
- TEXT
    - char(n)
    - varchar(n)
    - text

#### Commands:

- insert into table (column, ...) values(value, ...);
- select columns from table;
- select columns from table where condition;
- update table set column=value where condition;
- delete from table where condition;
- functions:
    - avg
    - count
    - distinct
    - max
    - min
    - where
    - limit
    - like
    - group by
    - order by
    - join

#### Special types of columns

- primary key - value for unique identification - used as the primary identifier for a row
- foreign key - the same value in another table - which points to a row in another table
- unique - which means it has to be unique in this table
- index - which asks our database to create an index to more quickly query based on this column. An index is a B-tree data structure, which helps us search for values.

#### Race conditions

- being transaction
- commit 
- rollback

#### SQL injection attack

```
# escapes user input
rows = db.execute("select * from users where username = ? and password = ?", username, password)

if len(rows) == 1:
    # Logged in!
```

```
# does not escape user input
rows = db.execute("select * from users where username = '{username}' and password = '{password}'")

if len(rows) == 1:
    # Logged in!

# using for example someone@mail.com'-- would change everything after the -- in an sql comment in the query
```
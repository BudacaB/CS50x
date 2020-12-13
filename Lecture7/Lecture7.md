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
---
---

#### SQL

- often times, in order to build the most functional website possible, we depend on a database to store info
- each column of an SQL table is capable of holding data of a particular data type: INT, SMALLINT, TINYINT, MEDIUMINT, BIGINT, DECIMAL, FLOAT, BIT, DATE, TIME, DATETIME, TIMESTAMP, CHAR, VARCHAR, BINARY, BLOB, TEXT, ENUM, GEOMETRY, LINESTRING etc.
- geometry and linestring - hold GIS (geographic information system) data
- CHAR - fixed length string, e.g. CHAR(10)
- VARCHAR - variable-length string - specifying the max possible length, e.g. VARCHAR(99)
- for example SQLite has these data types as well, but affiliates each with a "type affinity" to simplify things: NULL, INTEGER, REAL, TEXT, BLOB
- one other important consideration when constructing a table in SQL is to choose one column to be your **primary key**
- primary keys enable rows of a table to be uniquely and quickly identified
    - choosing your primary key appropiately can make subsequent operations on the table much easier
- it is also possible to establish a joint primary key - a combination of two columns that is always guaranteed to be unique
- we primarily consider just four operations that one may perform on a table - CRUD (Create / Read / Update / Delete - Insert / Select / Update / Delete)

#### INSERT

- INSERT INTO \<table> (\<columns>) VALUES (\<values>)
- when defining the column that ultimately ends up being your table's primary key, it's usually a good idea to have that column be an integer
- moreover, so as to eliminate the situation where you may accidentaly forget to specify a real value for the primary key column, you can configure that column to **autoincrement**, so it will pre-populate that column for you automatically when rows are added to the table

#### SELECT

- SELECT \<columns> FROM \<table> WHERE \<condition> ORDER BY \<column>

- databases empower us to organize information into tables efficiently
    - we don't always need to store every possible relevant piece of info in the same table, but can use relationships across the tables to let us pull information from where we need it

#### SELECT (JOIN)

- SELECT \<columns> FROM \<table1> JOIN \<table2> ON \<predicate>

#### UPDATE

- UPDATE \<table> SET \<column> = \<value> WHERE \<predicate> 

#### DELETE

- DELETE FROM \<table> WHERE \<predicate>
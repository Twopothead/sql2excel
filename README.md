# sql2excel
Python script to convert SQL(create table) to an Excel Spreadsheet or the system clipboard.You can paste the result anywhere you like.
## Notes
- This script is used to convert `create table` SQL statement  (sybase IQ) to csv, clipboard and markdown.
- Furthermore,The output can be easily converted to [Gbase database](https://dbdb.io/db/gbase) SQL.GBase is a distributed column store DBMS from China and supports SQL data types like VarChar,Decimal,SmallInt,BigInt and Int.It's a bit different from sybase.
## Dependencies
sqlparse is a non\-validating SQL parser module for Python. It provides support for parsing, splitting and formatting SQL statements.
If  you upgrade your pandas to version above 1.0.0, Converting to Markdown is also supported, see [pandas1.0.0-Converting to Markdown](https://pandas.pydata.org/docs/whatsnew/v1.0.0.html#converting-to-markdown).
- sqlparse
    - `pip install sqlparse`
- pandas (version aboove 1.0.0 is recommended )
 ```bash
pip install --upgrade pandas
pip install tabulate
pip install sqlparse
 ```
### example input
- (sybase IQ) SQL
- only 'create table' is supported.

You can paste your `create table` SQL statement to sql.txt and run `python sql2excel.py`
```sql
CREATE TABLE dbo.my_table_test  ( 
    myfield01	char(2) NOT NULL,
    myfield02	char(15) NOT NULL,
    myfield03	char(8) NOT NULL,
    myfield04	bigint NOT NULL,
    myfield05	bigint NOT NULL,
    myfield06	char(4) NULL,
    myfield07	char(19) NULL,
    myfield08	char(12) NULL,
    myfield09	char(6) NULL,
    myfield10	char(8) NULL,
    myfield11	char(2) NULL,
    myfield12	char(4) NULL,
    myfield13	char(8) NULL,
    myfield14	decimal(18,2) NULL,
    myfield15	char(1) NULL,
    myfield16	char(1) NULL,
    myfield17	decimal(18,2) NULL,
    myfield18	char(8) NULL,
    myfield19	bigint NULL,
    myfield20	char(2) NULL,
    myfield21	char(2) NULL,
    myfield22	bigint NULL,
    myfield23	char(2) NULL,
    myfield24	char(15) NULL,
    myfield25	char(10) NULL,
    myfield26	char(30) NULL,
    myfield27	char(4) NULL,
    myfield28	char(10) NULL,
    myfield29	char(30) NULL,
    myfield30	char(1) NULL,
    myfield31	char(1) NULL,
    myfield32	char(4) NULL,
    myfield33	char(4) NULL,
    myfield34	char(32) NULL,
    myfield35	char(70) NULL,
    myfield36	char(80) NULL,
    myfield37	char(80) NULL,
    myfield38	char(5) NULL,
    myfield39	char(16) NULL,
    myfield40	decimal(19,2) NULL,
    myfield41	decimal(19,2) NULL,
    myfield42	char(4) NULL,
    myfield43	char(1) NULL,
    myfield44	decimal(8,5) NULL,
    myfield45	decimal(8,5) NULL,
    myfield46	decimal(19,5) NULL,
    myfield47	decimal(19,5) NULL,
    myfield48	char(1) NULL,
    myfield49	decimal(19,2) NULL,
    myfield50	char(30) NULL,
    myfield51	char(4) NULL,
    myfield52	char(1) NULL,
    myfield53	char(40) NULL,
    myfield54	char(20) NULL,
    myfield55	varchar(30) NULL,
    myfield56	varchar(60) NULL,
    myfield57	varchar(30) NULL,
    myfield58	varchar(100) NULL,
    myfield59	varchar(30) NULL,
    myfield60	varchar(100) NULL,
    myfield61	varchar(100) NULL,
    myfield62	varchar(100) NULL,
    myfield63	varchar(80) NULL,
    myfield64	varchar(80) NULL,
    myfield65	varchar(80) NULL,
    myfield66	varchar(80) NULL,
    myfield67	varchar(80) NULL,
    myfield68	varchar(80) NULL,
    myfield69	varchar(80) NULL,
    myfield70	varchar(80) NULL,
    myfield71	varchar(80) NULL,
    myfield72	varchar(80) NULL,
    PRIMARY KEY(myfield01,myfield02,myfield03,myfield04,myfield05)
	WITH max_rows_per_page = 0
    )
GO
```

### Output
#### Supported format:
 - csv
 - the system clipboard
 - markdown

|     | field     | description | datatype | num1 | num2 | key | isnull |
| --: | :-------- | :---------- | :------- | :--- | ---: | :-- | :----- |
|   0 | myfield01 |             | Char     | 2    |    0 | Y   | N      |
|   1 | myfield02 |             | Char     | 15   |    0 | Y   | N      |
|   2 | myfield03 |             | Char     | 8    |    0 | Y   | N      |
|   3 | myfield04 |             | BigInt   | xxx  |    0 | Y   | N      |
|   4 | myfield05 |             | BigInt   | xxx  |    0 | Y   | N      |
|   5 | myfield06 |             | Char     | 4    |    0 | N   | Y      |
|   6 | myfield07 |             | Char     | 19   |    0 | N   | Y      |
|   7 | myfield08 |             | Char     | 12   |    0 | N   | Y      |
|   8 | myfield09 |             | Char     | 6    |    0 | N   | Y      |
|   9 | myfield10 |             | Char     | 8    |    0 | N   | Y      |
|  10 | myfield11 |             | Char     | 2    |    0 | N   | Y      |
|  11 | myfield12 |             | Char     | 4    |    0 | N   | Y      |
|  12 | myfield13 |             | Char     | 8    |    0 | N   | Y      |
|  13 | myfield14 |             | Decimal  | 18   |    2 | N   | Y      |
|  14 | myfield15 |             | Char     | 1    |    0 | N   | Y      |
|  15 | myfield16 |             | Char     | 1    |    0 | N   | Y      |
|  16 | myfield17 |             | Decimal  | 18   |    2 | N   | Y      |
|  17 | myfield18 |             | Char     | 8    |    0 | N   | Y      |
|  18 | myfield19 |             | BigInt   | xxx  |    0 | N   | Y      |
|  19 | myfield20 |             | Char     | 2    |    0 | N   | Y      |
|  20 | myfield21 |             | Char     | 2    |    0 | N   | Y      |
|  21 | myfield22 |             | BigInt   | xxx  |    0 | N   | Y      |
|  22 | myfield23 |             | Char     | 2    |    0 | N   | Y      |
|  23 | myfield24 |             | Char     | 15   |    0 | N   | Y      |
|  24 | myfield25 |             | Char     | 10   |    0 | N   | Y      |
|  25 | myfield26 |             | Char     | 30   |    0 | N   | Y      |
|  26 | myfield27 |             | Char     | 4    |    0 | N   | Y      |
|  27 | myfield28 |             | Char     | 10   |    0 | N   | Y      |
|  28 | myfield29 |             | Char     | 30   |    0 | N   | Y      |
|  29 | myfield30 |             | Char     | 1    |    0 | N   | Y      |
|  30 | myfield31 |             | Char     | 1    |    0 | N   | Y      |
|  31 | myfield32 |             | Char     | 4    |    0 | N   | Y      |
|  32 | myfield33 |             | Char     | 4    |    0 | N   | Y      |
|  33 | myfield34 |             | Char     | 32   |    0 | N   | Y      |
|  34 | myfield35 |             | Char     | 70   |    0 | N   | Y      |
|  35 | myfield36 |             | Char     | 80   |    0 | N   | Y      |
|  36 | myfield37 |             | Char     | 80   |    0 | N   | Y      |
|  37 | myfield38 |             | Char     | 5    |    0 | N   | Y      |
|  38 | myfield39 |             | Char     | 16   |    0 | N   | Y      |
|  39 | myfield40 |             | Decimal  | 19   |    2 | N   | Y      |
|  40 | myfield41 |             | Decimal  | 19   |    2 | N   | Y      |
|  41 | myfield42 |             | Char     | 4    |    0 | N   | Y      |
|  42 | myfield43 |             | Char     | 1    |    0 | N   | Y      |
|  43 | myfield44 |             | Decimal  | 8    |    5 | N   | Y      |
|  44 | myfield45 |             | Decimal  | 8    |    5 | N   | Y      |
|  45 | myfield46 |             | Decimal  | 19   |    5 | N   | Y      |
|  46 | myfield47 |             | Decimal  | 19   |    5 | N   | Y      |
|  47 | myfield48 |             | Char     | 1    |    0 | N   | Y      |
|  48 | myfield49 |             | Decimal  | 19   |    2 | N   | Y      |
|  49 | myfield50 |             | Char     | 30   |    0 | N   | Y      |
|  50 | myfield51 |             | Char     | 4    |    0 | N   | Y      |
|  51 | myfield52 |             | Char     | 1    |    0 | N   | Y      |
|  52 | myfield53 |             | Char     | 40   |    0 | N   | Y      |
|  53 | myfield54 |             | Char     | 20   |    0 | N   | Y      |
|  54 | myfield55 |             | VarChar  | 30   |    0 | N   | Y      |
|  55 | myfield56 |             | VarChar  | 60   |    0 | N   | Y      |
|  56 | myfield57 |             | VarChar  | 30   |    0 | N   | Y      |
|  57 | myfield58 |             | VarChar  | 100  |    0 | N   | Y      |
|  58 | myfield59 |             | VarChar  | 30   |    0 | N   | Y      |
|  59 | myfield60 |             | VarChar  | 100  |    0 | N   | Y      |
|  60 | myfield61 |             | VarChar  | 100  |    0 | N   | Y      |
|  61 | myfield62 |             | VarChar  | 100  |    0 | N   | Y      |
|  62 | myfield63 |             | VarChar  | 80   |    0 | N   | Y      |
|  63 | myfield64 |             | VarChar  | 80   |    0 | N   | Y      |
|  64 | myfield65 |             | VarChar  | 80   |    0 | N   | Y      |
|  65 | myfield66 |             | VarChar  | 80   |    0 | N   | Y      |
|  66 | myfield67 |             | VarChar  | 80   |    0 | N   | Y      |
|  67 | myfield68 |             | VarChar  | 80   |    0 | N   | Y      |
|  68 | myfield69 |             | VarChar  | 80   |    0 | N   | Y      |
|  69 | myfield70 |             | VarChar  | 80   |    0 | N   | Y      |
|  70 | myfield71 |             | VarChar  | 80   |    0 | N   | Y      |
|  71 | myfield72 |             | VarChar  | 80   |    0 | N   | Y      |


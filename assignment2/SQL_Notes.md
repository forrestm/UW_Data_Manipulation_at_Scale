## Relational Algebra

_Five primitive operators: Selection, Projection, Cartesian Product, Set Union, Set Difference_

### Projection $(\Pi)$

Produces from a relation $$R$$ a new relation containing only some of $$R$$ columns

To obtain a relation containing only the columns $$a_1, a_2,…, a_n$$ of $$R$$

$$\Pi_{a_1,…,a_n}(R)​$$

``` sql
SELECT A1,..., An
FROM R;
```

Example:

```sql
Person
| Name   | Age  | Weight |
| ------ | ---- | ------ |
| Harry  | 34   | 180    |
| Sally  | 28   | 164    |
| George | 29   | 170    |
| Helena | 54   | 154    |
| Peter  | 34   | 180    |
```

$$\Pi _{Age, Weight}$$(Person)

```sql
| Age  | Weight |
| ---- | ------ |
| 34   | 180    |
| 28   | 164    |
| 29   | 170    |
| 54   | 154    |
```

_Note: SQL will return a multiset with the projection requiring the use of ```SELECT DISTINCT```_

### Selection $(\sigma)$

When applied to a relation $$R$$ produces a new relation with a subset (contained within the original relation) of $$R$$ tuples (rows).

$$\sigma_{a\theta b} (R)$$ or $$\sigma_{a\theta v}(R)$$

* $$a$$ and $$b$$ are attribute names (column names)
* $$\theta$$ is a binary operation in the set $$\{<, \leq, =, \neq, \geq, >\}$$
* $$v$$ is a value constant
* $$R$$ is a relation

```sql
SELECT *
FROM R
WHERE V;
```

Example:

```sql
Person
| Name   | Age  | Weight |
| ------ | ---- | ------ |
| Harry  | 34   | 180    |
| Sally  | 28   | 164    |
| George | 29   | 170    |
| Helena | 54   | 154    |
| Peter  | 34   | 180    |
```

$$\sigma_{Age\leq 34}$$ (Person)
```sql
| Name   | Age  | Weight |
| ------ | ---- | ------ |
| Harry  | 34   | 180    |
| Helena | 54   | 154    |
| Peter  | 34   | 180    |
```
$$\sigma_{Age=Weight}​$$ (Person)
```sql
| Name   | Age  | Weight |
| ------ | ---- | ------ |
| Helena | 54   | 154    |
```


#### Generalized Selection $\sigma _\varphi(R)$

Where $$\varphi$$ is a propositional formula: $$\and$$ (and) $$\or$$ (or) $$\neg$$ (negation)

```sql
SELECT *
FROM R
WHERE V
```

Example:

```sql
Person
| Name   | Age  | Weight |
| ------ | ---- | ------ |
| Harry  | 34   | 180    |
| Sally  | 28   | 164    |
| George | 29   | 170    |
| Helena | 54   | 154    |
| Peter  | 34   | 180    |
```

$$\sigma_{Age\geq 30 \and Weight\leq60}​$$ (Person)

```sql
Person
| Name   | Age  | Weight |
| ------ | ---- | ------ |
| Helena | 54   | 154    |
```

### Set Union $\cup$





### SQL Commands

```sql
COUNT() --will print the amount of what's inside
SELECT DISTINCT --will eliminate duplicates

GROUP BY --column_names 
HAVING --condition. Used because WHERE could not be used with aggregate functions
```

#### Export to CSV

```sqlite
>sqlite3 c:/sqlite/chinook.db
sqlite> .headers on
sqlite> .mode csv
sqlite> .output data.csv
sqlite> SELECT customerid,
   ...>        firstname,
   ...>        lastname,
   ...>        company
   ...>   FROM customers;
sqlite> .quit
```

### [Matrix Multiplication](https://notes.mindprince.in/2013/06/07/sparse-matrix-multiplication-using-sql.html)

$$[A] = \begin{bmatrix} 0&1&0& 0&9\\ 0 &0&3&0&0\\0&0&0&2&0\\0&0&0&0&0 \end{bmatrix}$$ $$[B] = \begin{bmatrix} 1&0&0\\ 0 &0&0\\0&7&0\\0&0&2\\0&0&0 \end{bmatrix}$$

$$A \times B= \begin{bmatrix} 0&0&0\\ 0 &21&0\\0&0&4\\0&0&0 \end{bmatrix}​$$

```sql
CREATE TABLE a (
row_num INT,
col_num INT,
value INT,
PRIMARY KEY(row_num, col_num)
); 

CREATE TABLE b (
row_num INT,
col_num INT,
value INT,
PRIMARY KEY(row_num, col_num)
); 
```

```sql
INSERT INTO a VALUES
(1, 2, 1),
(1, 5, 9),
(2, 3, 3),
(3, 4, 2);

INSERT INTO b VALUES
(1, 1, 1),
(3, 2, 7),
(4, 3, 2);
```

```sql
SELECT a.row_num, b.col_num, SUM(a.value*b.value)
FROM a, b
WHERE a.col_num = b.row_num
GROUP BY a.row_num, b.col_num;

2|2|21
3|3|4
```

To see how this query works, remember the formula for cell (i,j) of the product. It is the sum of a(i,k)*b(k,j) for all k. The `JOIN` condition `a.col_num = b.row_num` makes sure that both `a.value` and `b.value` has the same k. The `GROUP BY` clause makes sure that we sum over all k’s.
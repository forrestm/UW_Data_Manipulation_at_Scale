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


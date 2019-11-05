SELECT *
FROM order
WHERE shipped_date IS NULL

-- IN / NOT OPEARTOR
SELECT *
FROM customers
WHERE state IN ('VA', 'FL', 'GA')
WHERE customer_id NOT IN (2, 4)

-- LIKE
SELECT *
FROM customers
WHERE last_name LIKE '%johnson%'
last_name LIKE '____son'

-- %x% indicate strictly equal before and/or after
-- '__x__' indicate 2 char before and/or after

-- REGEXP
SELECT *
FROM customers
WHERE last_name regexp 'b[ru]'

-- ^x indicate the beginning
-- x$ indicate the end
-- x|y indicate or
-- x[abcd] indicate a possbile combinaison 
-- x[a-z] same as above with an array of possibility

-- JOIN
SELECT order_id,  o.customer_id, first_name, last_name -- o.customer_id : retrieve a column from a specific table
FROM orders o -- abbreviate orders into o
JOIN customers c -- add tables customers to orders
	ON o.customer_id = c.customer_id -- calque le customer_id de la table orders au customer_id de la table customers

-- LEFT JOIN: 
SELECT
	c.customer_id,
    c.first_name,
    o.order_id
FROM customers c
LEFT JOIN orders o -- Add every records from customers even if ON statement is false
	ON c.customer_id = o.customer_id
ORDER BY c.customer_id

-- JOIN MULTIPLE
USE sql_store;
SELECT o.order_id, o.order_date, c.first_name, c.last_name, os.name AS status
FROM orders o
JOIN customers c
	on o.customer_id = c.customer_id
JOIN order_statuses os
	ON o.status = os.order_status_id
-- SQL queries for retrieving insights

-- Retrieve all customers
SELECT * FROM Customers;


-- Retrieve all products
SELECT * FROM Products;


-- Filter products by category (example, "Drinks")
SELECT * FROM Products WHERE category = 'Drinks';


-- List recent orders by date (descending)
SELECT * FROM Orders ORDER BY order_date DESC;



-- Aggregation
-- Find the number of total orders
SELECT COUNT(order_id) AS TotalOrders FROM Orders;


-- Calculate total revenue from all orders (SUM(price × quantity))
SELECT SUM(O.quantity * P.price) AS TotalRevenue
FROM Orders O
JOIN Products P ON O.product_id = P.product_id;


-- Find the average product price
SELECT AVG(price) AS AverageProductPrice FROM Products;


-- Joins
-- INNER JOIN to get detailed order information (with customer and product details)
SELECT
    O.order_id,
    C.name AS CustomerName,
    P.product_name,
    O.quantity,
    P.price AS UnitPrice,
    (O.quantity * P.price) AS LineTotal,
    O.order_date
FROM Orders O
INNER JOIN Customers C ON O.customer_id = C.customer_id
INNER JOIN Products P ON O.product_id = P.product_id;


-- LEFT JOIN to list all customers 
SELECT
    C.name AS CustomerName,
    C.email,
    O.order_id,
    O.order_date,
    P.product_name,
    O.quantity
FROM Customers C
LEFT JOIN Orders O ON C.customer_id = O.customer_id
LEFT JOIN Products P ON O.product_id = P.product_id
ORDER BY C.name, O.order_date;


-- LEFT JOIN to show products even if they haven’t been ordered
SELECT
    P.product_name,
    P.category,
    P.price,
    O.order_id
FROM Products P
LEFT JOIN Orders O ON P.product_id = O.product_id
ORDER BY P.product_name;

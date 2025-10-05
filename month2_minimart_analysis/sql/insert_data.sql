-- SQL script to insert sample data


-- Insert into Customers
INSERT INTO Customers (customer_id, name, email, join_date, phone_number) VALUES
(1, 'Alice Micheaal', 'alice99@gmail.com', '2023-01-15', '555-111-2222'),
(2, 'Bob Stephens', 'bobby05@gmail.com', '2023-02-20', '555-333-4444'),
(3, 'Charlie Brown', 'charlieB@gmail.com', '2023-03-10', '555-555-6666'),
(4, 'Diana Prince', 'diana@gmail.com', '2023-04-05', '555-777-8888'),
(5, 'Eve Adams', 'eve44@gmail.com', '2023-05-22', '555-999-0000');

-- Insert into Products
INSERT INTO Products (product_id, product_name, category, price) VALUES
(101, 'Monster', 'Drinks', 3.50),
(102, 'Groundnuts', 'Pastries', 2.75),
(103, 'Sandwich', 'Meals', 7.00),
(104, 'Orange Juice', 'Drinks', 4.00),
(105, 'Donut', 'Pastries', 3.25),
(106, 'Salad', 'Meals', 8.50);

-- Insert into Orders
INSERT INTO Orders (order_id, customer_id, product_id, quantity, order_date) VALUES
(1, 1, 101, 2, '2023-06-01'),
(2, 2, 103, 1, '2023-06-01'),
(3, 1, 102, 3, '2023-06-02'),
(4, 3, 104, 2, '2023-06-02'),
(5, 4, 101, 1, '2023-06-03'),
(6, 2, 105, 2, '2023-06-03'),
(7, 5, 106, 1, '2023-06-04'),
(8, 1, 104, 1, '2023-06-04'),
(9, 3, 102, 1, '2023-06-05'),
(10, 5, 101, 3, '2023-06-05');

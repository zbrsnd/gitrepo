DROP TABLE IF EXISTS customers;  
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS tbOrders;


CREATE TABLE customers
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_name TEXT,
	address TEXT
);

CREATE TABLE subscriptions
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description	TEXT,
    price_per_month DECIMAL,
	subscription_length TEXT
);

CREATE TABLE tbOrders
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    subscription_id INTEGER,
    purchase_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(id)

);
/*
INSERT INTO tbCustomers(customer_id, customer_name, adress) VALUES (NULL, 'Allie Rahaim', '123 Broadway');
INSERT INTO tbCustomers VALUES (NULL, 'Jacquline Diddle', '456 Park Ave');
INSERT INTO tbSubscriptions(subscription_id, description, price_per_month, subscription_length)
VALUES (NULL, 'Politics Magazine', 10, '12 months' );



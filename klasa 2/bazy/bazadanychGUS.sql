DROP TABLE IF EXISTS miasta;  
DROP TABLE IF EXISTS mieszkancy;
DROP TABLE IF EXISTS powierzchnie;


CREATE TABLE miasta
(
	id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
	nazwa_miasta TEXT(30),
	wojewodztwo TEXT(35)
);

CREATE TABLE mieszkancy
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	liczba_mieszkancow INTEGER,
    liczba_kobiet INTEGER,
	grupa_wiekowa TEXT(20),
    data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
);

CREATE TABLE powierzchnie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    powierzchnia_miasta DECIMAL,
    powierzchnia_zielona INTEGER,
    data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
    FOREIGN KEY (data_aktualizacji) REFERENCES mieszkancy(data_aktualizacji)
    

);
/*
INSERT INTO tbCustomers(customer_id, customer_name, adress) VALUES (NULL, 'Allie Rahaim', '123 Broadway');
INSERT INTO tbCustomers VALUES (NULL, 'Jacquline Diddle', '456 Park Ave');
INSERT INTO tbSubscriptions(subscription_id, description, price_per_month, subscription_length)
VALUES (NULL, 'Politics Magazine', 10, '12 months' );



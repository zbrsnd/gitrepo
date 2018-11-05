DROP TABLE IF EXISTS pracownicy;  
DROP TABLE IF EXISTS kontakty;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS stanowiska;


CREATE TABLE pracownicy
(
    id_pracownika INTEGER PRIMARY KEY AUTOINCREMENT,
	imie TEXT(15),
	nazwisko TEXT(30),
	kod STRING(10),
    miasto_z TEXT(25),
    ulica TEXT(35),
    data_u DATE,
    miasto_u TEXT(30)
);

CREATE TABLE kontakty
(
	id_pracownika INTEGER NOT NULL,
	typ_k BOOLEAN,
    kontakt STRING(15),
    uwagi TEXT(30),
    FOREIGN KEY(id_pracownika) REFERENCES pracownicy(id_pracownika)
);


CREATE TABLE stanowiska 
(
    id_stanowiska INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT(30)
);


CREATE TABLE place
(
    id_p INTEGER NOT NULL,
    id_s INTEGER NOT NULL,
    placa INTEGER,
    data_z DATE,
    FOREIGN KEY (id_p) REFERENCES kontakty(id_pracownika),
    FOREIGN KEY (id_s) REFERENCES stanowiska(id_stanowiska)
    
);


/*
INSERT INTO tbCustomers(customer_id, customer_name, adress) VALUES (NULL, 'Allie Rahaim', '123 Broadway');
INSERT INTO tbCustomers VALUES (NULL, 'Jacquline Diddle', '456 Park Ave');
INSERT INTO tbSubscriptions(subscription_id, description, price_per_month, subscription_length)
VALUES (NULL, 'Politics Magazine', 10, '12 months' );



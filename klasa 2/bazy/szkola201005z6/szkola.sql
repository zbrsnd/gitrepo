DROP TABLE IF EXISTS uczniowie;  
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;


CREATE TABLE uczniowie
(
    IDucznia INTEGER PRIMARY KEY NOT NULL,
	nazwisko TEXT(30),
	ulica TEXT(35),
    dom TEXT(35),
    IDklasy VARCHAR(3) NOT NULL
);

CREATE TABLE przedmioty
(
    IDprzedmiotu INTEGER NOT NULL,
	NazwaPrzedmiotu TEXT(20),
    Nazwisko_naucz TEXT(20), 
	Imie_naucz TEXT(20)
);

CREATE TABLE oceny
(
    IDucznia INTEGER,
    ocena INTEGER,
    Data_ DATE,
    IDprzedmiotu INTEGER NOT NULL,
    FOREIGN KEY (IDucznia) REFERENCES uczniowie(IDucznia)
    FOREIGN KEY (IDprzedmiotu) REFERENCES przedmioty(IDprzedmiotu)
    

);
/*
INSERT INTO tbCustomers(customer_id, customer_name, adress) VALUES (NULL, 'Allie Rahaim', '123 Broadway');
INSERT INTO tbCustomers VALUES (NULL, 'Jacquline Diddle', '456 Park Ave');
INSERT INTO tbSubscriptions(subscription_id, description, price_per_month, subscription_length)
VALUES (NULL, 'Politics Magazine', 10, '12 months' );



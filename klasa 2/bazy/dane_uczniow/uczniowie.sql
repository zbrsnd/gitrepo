DROP TABLE IF EXISTS nazwiska;  
DROP TABLE IF EXISTS dane_osobowe;
DROP TABLE IF EXISTS oceny;


CREATE TABLE nazwiska
(
	nr_ucz INTEGER PRIMARY KEY NOT NULL,
	nazwisko TEXT(30),
	imie1 TEXT(15),
    imie2 TEXT(15)
);

CREATE TABLE dane_osobowe
(
	nr_ucz INTEGER NOT NULL,
	dzien INTEGER,
    miesiac INTEGER,
    rok INTEGER,
    m_urodzenia TEXT(30),
    wojewodztwo TEXT(35),
    FOREIGN KEY (nr_ucz) REFERENCES nazwiska(nr_ucz)
);

CREATE TABLE oceny
(
    nr_ucz INTEGER NOT NULL,
    zach VARCHAR(15),
    rel_ety INTEGER(1),
    jpol INTEGER(1),
    jang INTEGER(1),
    jniem INTEGER(1),
    mat INTEGER(1),
    hist INTEGER(1),
    geog INTEGER(1),
    biol INTEGER(1),
    fiz INTEGER(1),
    che INTEGER(1),
    tech INTEGER(1),
    info INTEGER(1),
    plas INTEGER(1),
    po INTEGER(1),
    wf INTEGER(1),
    FOREIGN KEY (nr_ucz) REFERENCES nazwiska(nr_ucz)
    
);
/*
INSERT INTO tbCustomers(customer_id, customer_name, adress) VALUES (NULL, 'Allie Rahaim', '123 Broadway');
INSERT INTO tbCustomers VALUES (NULL, 'Jacquline Diddle', '456 Park Ave');
INSERT INTO tbSubscriptions(subscription_id, description, price_per_month, subscription_length)
VALUES (NULL, 'Politics Magazine', 10, '12 months' );



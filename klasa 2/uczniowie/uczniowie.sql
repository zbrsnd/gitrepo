DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS klasy;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;

CREATE TABLE uczniowie (
		id INTEGER PRIMARY KEY NOT NULL,
		imie varchar(50),
		nazwisko varchar(50),
		plec INTEGER(1),
		id_klasa INTEGER(1) NOT NULL,
		egz_hum INTEGER(3) NOT NULL,
		egz_mat INTEGER(3) NOT NULL,
		egz_jez INTEGER(3) NOT NULL,
    FOREIGN KEY (id_klasa) REFERENCES klasy(id)
);

CREATE TABLE klasy (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		klasa text(2),
		rok_naboru INTEGER(4),
		rok_matury INTEGER(4)
);
CREATE TABLE przedmioty (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		przedmiot varchar(50),
		imie_naucz varchar(50),
		nazwisko_naucz varchar(50),
		plec_naucz INTEGER(1)
);
CREATE TABLE oceny (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		datad DATE,
		id_uczen INTEGER(1) NOT NULL,
		id_przedmiot INTEGER(1) NOT NULL,
		ocena INTEGER(1),
    FOREIGN KEY (id_uczen) REFERENCES uczniowie(id),
    FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
);
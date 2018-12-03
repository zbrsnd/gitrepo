DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS klasy;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;

CREATE TABLE uczniowie (
		id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
		imie varchar(50),
		nazwisko varchar(50),
		plec BOOLEAN,
		id_klasa INTEGER(1) NOT NULL,
		egz_hum NUMERIC(3) NOT NULL DEFAULT 0,
		egz_mat NUMERIC(3) NOT NULL DEFAULT 0,
		egz_jez NUMERIC(3) NOT NULL DEFAULT 0,
    FOREIGN KEY (id_klasa) REFERENCES klasy(id)
    ON DELETE CASCADE ON UPDATE NO ACTION
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
		plec_naucz BOOLEAN
);
CREATE TABLE oceny (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		datad DATE,
		id_uczen INTEGER(1) NOT NULL,
		id_przedmiot INTEGER(1) NOT NULL,
		ocena DECIMAL(1) NOT NULL,
    FOREIGN KEY (id_uczen) REFERENCES uczniowie(id),
    FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
);
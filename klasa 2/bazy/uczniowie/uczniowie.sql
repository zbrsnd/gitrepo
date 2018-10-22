DROP TABLE IF EXISTS uczniowie;  
DROP TABLE IF EXISTS klasy;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;

CREATE TABLE uczniowie
(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
imie TEXT(20),
nazwisko TEXT(20),
plec BOOLEAN,
id_klasa INTEGER NOT NULL,
egz_hum NUMERIC NOT NULL DEFAULT 0,
egz_mat NUMERIC NOT NULL DEFAULT 0,
egz_jez NUMERIC NOT NULL DEFAULT 0,
FOREIGN KEY (id_klasa) REFERENCES klasy(id)
ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE klasy 
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
klasa TEXT,
rok_naboru INTEGER,
rok_matury INTEGER
);

CREATE TABLE przedmioty 
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
przedmiot TEXT(35),
imie_naucz TEXT(20),
nazwisko_naucz TEXT(25),
plec_naucz BOOLEAN
);


CREATE TABLE oceny
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
datad DATE,
id_uczen INTEGER,
id_przedmiot INTEGER,
ocena INTEGER,
FOREIGN KEY (id_uczen) REFERENCES uczniowie(id),
FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
);

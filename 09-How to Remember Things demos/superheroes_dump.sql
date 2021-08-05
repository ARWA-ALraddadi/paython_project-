/* This SQLite "dump" script recreates the Superheroes database.
After creating a new database in the GUI, execute this script
to both define the tables and populate them with data.  This
script was "exported" from the DB Browser GUI and is not intended
for human consumption, so is not laid out nicely or commented. */

CREATE TABLE vulnerabilities (
  superhero TEXT NOT NULL,
  weakness TEXT NULL, effect TEXT,
  PRIMARY KEY (superhero, weakness) );
INSERT INTO `vulnerabilities` VALUES ('Superman','Green kryptonite','Loss of superpowers');
INSERT INTO `vulnerabilities` VALUES ('Batman','Bullets',NULL);
INSERT INTO `vulnerabilities` VALUES ('Superman','Red-gold kryptonite','Amnesia');
CREATE TABLE powers_and_abilities (
  superhero TEXT NOT NULL,
  power TEXT NOT NULL,
  PRIMARY KEY (superhero, power) );
INSERT INTO `powers_and_abilities` VALUES ('Superman','Faster than a speeding bullet');
INSERT INTO `powers_and_abilities` VALUES ('Superman','More powerful than a locomotive');
INSERT INTO `powers_and_abilities` VALUES ('Superman','Able to leap tall buildings in a single bound');
INSERT INTO `powers_and_abilities` VALUES ('Captain Marvel','The wisdom of Solomon');
INSERT INTO `powers_and_abilities` VALUES ('Captain Marvel','The strength of Hercules');
INSERT INTO `powers_and_abilities` VALUES ('Captain Marvel','The stamina of Atlas');
INSERT INTO `powers_and_abilities` VALUES ('Captain Marvel','The power of Zeus');
INSERT INTO `powers_and_abilities` VALUES ('Captain Marvel','The courage of Achilles');
INSERT INTO `powers_and_abilities` VALUES ('Captain Marvel','The speed of Mercury');
CREATE TABLE nicknames (
  superhero TEXT NOT NULL,
  nickname TEXT NULL,
  PRIMARY KEY (superhero) );
INSERT INTO `nicknames` VALUES ('Superman','The Man of Steel');
INSERT INTO `nicknames` VALUES ('Batman','The Caped Crusader');
INSERT INTO `nicknames` VALUES ('Captain Marvel','The World''s Mightiest Mortal');
CREATE TABLE identities (
  superhero TEXT NOT NULL,
  secret_identity TEXT NULL,
  real_name TEXT NULL, -- If different from the superhero's secret identity
  PRIMARY KEY (superhero) );
INSERT INTO `identities` VALUES ('Superman','Clark Kent','Kal El');
INSERT INTO `identities` VALUES ('Batman','Bruce Wayne',NULL);
INSERT INTO `identities` VALUES ('Captain Marvel','Billy Batson',NULL);
INSERT INTO `identities` VALUES ('Wonder Woman','Diana Prince','Princess Diana');
CREATE TABLE enemies (
  enemy TEXT NOT NULL,
  superhero TEXT NULL,
  PRIMARY KEY (enemy, superhero) );
INSERT INTO `enemies` VALUES ('Lex Luthor','Superman');
INSERT INTO `enemies` VALUES ('Brainiac','Superman');
INSERT INTO `enemies` VALUES ('The Joker','Batman');
INSERT INTO `enemies` VALUES ('The Penguin','Batman');
INSERT INTO `enemies` VALUES ('Catwoman','Batman');
INSERT INTO `enemies` VALUES ('The Riddler','Batman');
INSERT INTO `enemies` VALUES ('Dr. Sivana','Captain Marvel');
INSERT INTO `enemies` VALUES ('Mr. Mind','Captain Marvel');
CREATE TABLE birthdates (
  superhero TEXT NOT NULL,
  birthdate INTEGER NOT NULL,
  PRIMARY KEY (superhero) );
INSERT INTO `birthdates` VALUES ('Batman',1939);
INSERT INTO `birthdates` VALUES ('Captain Marvel',1940);
INSERT INTO `birthdates` VALUES ('Superman',1938);
INSERT INTO `birthdates` VALUES ('Wonder Woman',1941);
CREATE TABLE allies (
  friend TEXT NOT NULL,
  superhero TEXT NULL,
  PRIMARY KEY (friend, superhero) );
INSERT INTO `allies` VALUES ('Lois Lane','Superman');
INSERT INTO `allies` VALUES ('Jimmy Olsen','Superman');
INSERT INTO `allies` VALUES ('Perry White','Superman');
INSERT INTO `allies` VALUES ('Steve Trevor','Wonder Woman');
INSERT INTO `allies` VALUES ('Etta Candy','Wonder Woman');
INSERT INTO `allies` VALUES ('Alfred Pennyworth','Batman');


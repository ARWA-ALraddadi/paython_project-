/* This script contains certain queries on our Superheroes database.
   You should execute only one of these queries at a time. */

/* Query 1: Show everything in the table of enemies */
SELECT * FROM enemies;

/* Query 2: Select just the first column from the table of allies */
SELECT friend FROM allies;

/* Query 3: Find superheroes "born" before 1940 */
SELECT superhero FROM birthdates WHERE birthdate < 1940;

/* Query 4: Find superheroes with the power of super speed */
SELECT * FROM powers_and_abilities WHERE power LIKE '%speed%';

/* Query 5: Sort superheroes by age */
SELECT * FROM birthdates ORDER BY birthdate;

/* Query 6: A naive merger of two tables (producing meaningless rows) */
SELECT * FROM nicknames, vulnerabilities;

/* Query 7: Match superhero's nicknames with their vulnerabilties (for
    heroes who have both attributes) */
SELECT nickname, weakness
FROM nicknames, vulnerabilities
WHERE nicknames.superhero = vulnerabilities.superhero;

/* Query 8: Assuming that friendliness is transitive, find out the
   enemies of some superhero's allies */
SELECT friend, enemy FROM allies, enemies
WHERE allies.superhero = enemies.superhero
ORDER BY friend, enemy;

/* Query 9: Find out the birthdates of some "secret identities",
   assuming they're the same as the corresponding hero */
SELECT secret_identity, birthdate
FROM identities, birthdates
WHERE identities.superhero = birthdates.superhero;


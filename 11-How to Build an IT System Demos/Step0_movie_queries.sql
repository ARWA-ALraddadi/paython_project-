-- These are prototypes of the queries that our program
-- must generate.  This script can be used to demonstrate
-- to the client the kinds of results that will be
-- produced by the final system, to get early feedback on
-- whether or not they're the kind of thing the
-- client wants.
--
-- Before running these queries you'll need to ensure you
-- have a copy of the movie_survey database

-- Get all actors, ordered by productivity:

SELECT actor, number_of_movies FROM actors
ORDER BY number_of_movies DESC, actor ASC;

-- Get all actors, ordered by popularity:

SELECT actor, count(actor) FROM favorite_actors
GROUP BY actor
ORDER BY count(actor) DESC, actor ASC;

-- Find all the actors who starred in a given movie:

SELECT actor FROM actors_movies
WHERE movie = 'Back to the Future'
ORDER BY actor;

-- Find all the movies in which a given actor appeared:

SELECT movie FROM actors_movies
WHERE actor = 'Jodie Foster'
ORDER BY movie;
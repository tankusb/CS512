-- Select the first name, last name and film title of all films an actor with the last name Cage acted in.
-- Order by the film title, descending. There should be one row for every actor/film pair.
SELECT actor.first_name, actor.last_name, film.title 
FROM actor
INNER JOIN film_actor on film_actor.actor_id = actor.actor_id
INNER JOIN film on film.film_id = film_actor.film_id 
WHERE actor.last_name = 'Cage'
ORDER BY title DESC
-- Select from films, the title and description of all films where both a dog and a robot are mentioned
-- in the description but only when the robot is mentioned first. Order by the film title ascending.
-- The robot is considered first if at some point in the string the substring 'dog' shows up after the substring 'robot'
SELECT title, description FROM film where description like "%robot%dog%" ORDER BY title ASC
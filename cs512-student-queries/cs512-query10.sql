-- Update the bsg_people table. Set anyone named Gaius Baltar to be from Caprica. This should use a subquery.
UPDATE bsg_people
set homeworld = (SELECT id FROM bsg_planets WHERE name = "Caprica") 
where fname = 'Gaius' AND lname = 'Baltar'


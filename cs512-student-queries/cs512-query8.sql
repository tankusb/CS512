-- Insert Anastasia Dualla from Sagittaron into the bsg_people table. You should use a subquery to do this.
INSERT INTO bsg_people (id, fname, lname, homeworld, age)
VALUES ('Anastasia', 'Dualla', (SELECT id FROM bsg_planets WHERE name = "Sagittaron"))


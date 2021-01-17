-- List the customer first and last name and address district of all customers from the California district
-- order by their last name descending
SELECT first_name, last_name,  district
FROM customer cust
LEFT OUTER JOIN address addr ON cust.address_id = addr.address_id
WHERE district = 'California'
ORDER BY last_name DESC
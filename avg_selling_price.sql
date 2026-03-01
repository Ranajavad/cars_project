/*What is the average selling price for Automatic vs. Manual cars?*/
SELECT transmission, ROUND(AVG(selling_price), 2) as avg_price
FROM vehicles
GROUP BY transmission;
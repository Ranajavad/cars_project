/* 1. Year-over-Year Depreciation 
How much value does a car lose the moment it turns a year older?*/
SELECT 
    year, 
    ROUND(AVG(selling_price), 0) as avg_price,
    LAG(ROUND(AVG(selling_price), 0)) OVER (ORDER BY year DESC) - ROUND(AVG(selling_price), 0) as price_drop_from_previous_year
FROM vehicles
WHERE year > 2010
GROUP BY year
ORDER BY year DESC;



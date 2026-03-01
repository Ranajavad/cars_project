/*Goal: Show the maximum and minimum price for each Owner category (First Owner, Second Owner, etc.).

Why: This helps see how much value a car loses just by changing hands.*/

SELECT owner, 
       MAX(selling_price) as highest_price, 
       MIN(selling_price) as lowest_price
FROM vehicles
GROUP BY owner
ORDER BY highest_price DESC;
/* Count how many cars are available for each Seller Type (Individual vs. Dealer). */
SELECT seller_type, COUNT(*) as number_of_cars
FROM vehicles
GROUP BY seller_type;
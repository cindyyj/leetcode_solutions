# Write your MySQL query statement below

# https://www.mysqltutorial.org/mysql-delete-duplicate-rows/
DELETE t1 FROM Person t1
INNER JOIN Person t2 
WHERE t1.id > t2.id AND t1.email = t2.email    
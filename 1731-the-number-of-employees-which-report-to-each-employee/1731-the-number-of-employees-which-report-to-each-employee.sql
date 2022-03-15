# Write your MySQL query statement below
# For exact-value numbers, ROUND() uses the “round half up” rule: A value with a fractional part of .5 or greater is rounded up to the next integer if positive or down to the next integer if negative. (In other words, it is rounded away from zero.) A value with a fractional part less than .5 is rounded down to the next integer if positive or up to the next integer if negative. (In other words, it is rounded toward zero.)

SELECT 
    b.employee_id AS employee_id, 
    b.name AS name, 
    COUNT(*) AS reports_count, 
    ROUND(AVG(a.age)) AS average_age
FROM 
    Employees a JOIN Employees b ON a.reports_to = b.employee_id
GROUP BY employee_id
ORDER BY employee_id
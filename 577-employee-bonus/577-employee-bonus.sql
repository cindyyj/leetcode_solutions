# Write your MySQL query statement below
# "Select all employee's name and bonus whose bonus is < 1000. 
# (People have no bonus records are also needed to be considered)"

select name, bonus
from Employee left join Bonus 
on Employee.empId = Bonus.empId
where bonus < 1000 or bonus is null
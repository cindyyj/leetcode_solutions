# Write your MySQL query statement below

# common top n, nth problem
# https://leetcode.com/problems/second-highest-salary/discuss/1168444/Summary-Five-ways-to-solve-the-top-n-nth-problems

# window function!
# common table expression (CTE)
# CTE is a temporary named result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement

with CTE as (
    select salary, rank() over (order by salary desc) as rank_desc
    from Employee
    )

select max(salary) as SecondHighestSalary 
from cte 
where rank_desc = 2
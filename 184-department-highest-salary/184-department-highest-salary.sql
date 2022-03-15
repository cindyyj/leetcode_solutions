# Write your MySQL query statement below

select 
    a.name as Department, 
    b.name as Employee, 
    Salary 
from 
    Employee as a 
    join Department as b 
    on a.DepartmentId = b.id 
where
    (a.DepartmentId, Salary) in 
    (
        select DepartmentId, max(Salary)
        from employee
        group by DepartmentId
    )

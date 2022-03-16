# Write your MySQL query statement below
select DISTINCT title 
from content c 
inner join TVProgram t on c.content_id = t.content_id
where 
    year(t.program_date) = 2020 
    and month(t.program_date) = 6 
    and c.Kids_content = 'Y'
    and c.content_type = 'Movies';
# Write your MySQL query statement below
select customer_name, customer_id, order_id, order_date
from
(
    select  
        name customer_name, 
        c.customer_id, 
        order_id, 
        order_date,
        rank() over(partition by c.customer_id order by order_date desc) ranking
    from customers c
    inner join orders o
    on c.customer_id = o.customer_id
) t
where t.ranking <=3
order by customer_name, customer_id, order_date desc
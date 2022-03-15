# Write your MySQL query statement below

# select customer_number
# from orders
# group by customer_number
# order by count(*) desc
# limit 1

select customer_number
from orders
group by customer_number
having count(*) = (
    select count(*) as cnt
    from orders
    group by customer_number
    order by cnt desc
    limit 1
)

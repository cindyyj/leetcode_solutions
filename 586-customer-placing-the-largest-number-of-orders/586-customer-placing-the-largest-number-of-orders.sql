# Write your MySQL query statement below

# select customer_number
# from orders
# group by customer_number
# order by count(*) desc
# limit 1


# generic version 
# Follow up: What if more than one customer have the largest number of orders, can you find all the customer_number in this case?
# Do not use triangle join, because it is bad scalibility and performance

# Step:
# Find the number of the largest count on order number
# Select the customer who has same number of order as the largest count on order number

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

# Write your MySQL query statement below
# 1.  name of the user who has rated the greatest number of movies. 
# In case of a tie, return the lexicographically smaller user name.

(
    select u.name as results
    from MovieRating r left join Users u
    on r.user_id = u.user_id
    group by r.user_id
    order by count(r.movie_id) desc, u.name
    limit 1
)
union
(
    select m.title as results
    from MovieRating r left join Movies m
    on r.movie_id = m.movie_id
    where r.created_at between '2020-02-01' and '2020-02-29'
    group by r.movie_id
    order by avg(r.rating) desc, m.title
    limit 1
)

# (
#   SELECT u.name AS results
#   FROM Movie_Rating r LEFT JOIN Users u
#   ON (r.user_id = u.user_id)
#   GROUP BY r.user_id
#   ORDER BY COUNT(r.movie_id) DESC, u.name 
#   LIMIT 1
# )
# UNION
# (
#   SELECT m.title AS results
#   FROM Movie_Rating r LEFT JOIN Movies m
#   ON (r.movie_id = m.movie_id)
#   WHERE r.created_at LIKE '2020-02%'
#   GROUP BY r.movie_id
#   ORDER BY AVG(r.rating) DESC, m.title 
#   LIMIT 1
# )
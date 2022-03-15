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
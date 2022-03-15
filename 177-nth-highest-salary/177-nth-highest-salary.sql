CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      
      # # DENSE_RANK vs. RANK
      # select distinct Salary
      # from 
      # (select DENSE_RANK() over (order by Salary desc) as r, Salary
      #   from Employee
      #  ) as t
      # where r = N
      
      
      # 'limit 0,1 ' that means the first row,so does 'limit 1 offset 0.likewise,'limit n,1' means the n+1th row.
      # the m of 'limit m,n' means starting on line m+1，the n of 'limit m,n' means how many rows we want to get.
      SELECT DISTINCT Salary 
      FROM Employee
      ORDER BY Salary DESC
      LIMIT 1 
      OFFSET N
  );
END
SELECT name, SUM(amount) AS balance
FROM Users
JOIN Transactions ON Transactions.account = Users.account
GROUP BY name
HAVING SUM(amount) > 10000;
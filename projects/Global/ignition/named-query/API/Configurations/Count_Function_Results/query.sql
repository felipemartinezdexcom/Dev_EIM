SELECT result, COUNT(*) AS count
FROM [API].TransactionsLog
where [timestamp] between :starttime and :endtime
GROUP BY result;
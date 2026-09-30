SELECT [API].TransactionsLog.function_name,

Count([API].TransactionsLog.function_name) AS Count_function_name

FROM [API].TransactionsLog where [timestamp]
BETWEEN :starttime AND :endtime 


GROUP BY [API].TransactionsLog.function_name
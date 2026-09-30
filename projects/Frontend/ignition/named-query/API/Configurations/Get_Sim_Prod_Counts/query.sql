SELECT 
  CASE WHEN simulator_call = 'YES' THEN 'Simulator'
       WHEN simulator_call = 'NO'  THEN 'Production'
  END AS environment,
  COUNT(*) AS count
FROM [API].TransactionsLog where [timestamp] between :starttime and :endtime
GROUP BY simulator_call;
SELECT 
  CASE WHEN sys_interface = 'Database' THEN 'DB'
       WHEN sys_interface = 'Camstar'  THEN 'MES'
  END AS environment,
  COUNT(*) AS count
FROM [API].TransactionsLog where [timestamp] between :starttime and :endtime
GROUP BY sys_interface;


SELECT 
    name AS 'function_name'
FROM sys.procedures
WHERE SCHEMA_NAME(schema_id) = :schema
ORDER BY name;
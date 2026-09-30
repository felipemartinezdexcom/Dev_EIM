---0 does not exist
---1 exist and is active
---2 exist but not active

SELECT
    CASE
        WHEN EXISTS (
            SELECT 1
            FROM [API].[Equipment]
            WHERE equipment_name = :machine_name
              AND active = 1
        ) THEN 1

        WHEN EXISTS (
            SELECT 1
            FROM [API].[Equipment]
            WHERE equipment_name = :machine_name
        ) THEN 2

        ELSE 0
    END AS Status;
    

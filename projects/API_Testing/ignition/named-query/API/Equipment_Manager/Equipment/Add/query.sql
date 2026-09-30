IF NOT EXISTS
(
    SELECT 1
    FROM [API].[Equipment]
    WHERE equipment_name = :equipment_name
)
BEGIN
    INSERT INTO [API].[Equipment]
    (
        equipment_name,
        date_created,
        description,
        created_by,
        last_date_modified,
        active
    )
    VALUES
    (
        :equipment_name,
        GETDATE(),
        :description,
        :created_by,
        GETDATE(),
        1
    );

    SELECT 1 AS Inserted;
END
ELSE
BEGIN
    SELECT 0 AS Inserted;
END
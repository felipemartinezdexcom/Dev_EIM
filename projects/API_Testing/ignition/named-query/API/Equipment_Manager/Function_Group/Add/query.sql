IF NOT EXISTS
(
    SELECT 1
    FROM [API].[FunctionGroups]
    WHERE function_group_name = :function_group_name
)
BEGIN
    INSERT INTO [API].[FunctionGroups]
    (
        function_group_name,
        date_created,
        created_by,
        last_date_modified,
        active
    )
    VALUES
    (
        :function_group_name,
        GETDATE(),
        :created_by,
        GETDATE(),
        1
    );

    SELECT function_group_id AS result
    FROM [API].[FunctionGroups]
    WHERE function_group_name = :function_group_name;
END
ELSE
BEGIN
    SELECT 0 AS result;
END
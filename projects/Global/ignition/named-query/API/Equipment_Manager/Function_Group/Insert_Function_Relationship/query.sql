

IF NOT EXISTS (
    SELECT 1
    FROM [API].FunctionGroupList
    WHERE function_group_id = :function_group_id
      AND function_id = :function_id
)
BEGIN
    INSERT INTO [API].FunctionGroupList
        (function_group_id, function_id)
    VALUES
        (:function_group_id, :function_id);
END
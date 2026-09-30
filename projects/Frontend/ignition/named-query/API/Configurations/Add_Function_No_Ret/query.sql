IF NOT EXISTS (
    SELECT 1 FROM [API].[FunctionsList]
    WHERE [function_name] = :function_name and  [sys_interface]=:sys_interface 
)
BEGIN
    INSERT INTO [API].[FunctionsList] (
        [function_name],
        [date_created],
        [created_by],
        [sys_interface],
        [database_name],
        [database_schema],
        [custom_function_name]
    )
    VALUES (
        :function_name,
        GETDATE(),
        :username,
        :sys_interface,
        :database_name,
        :database_schema,
        :custom_function_name
    );
END
IF NOT EXISTS (
    SELECT 1 FROM [API].FunctionsList WHERE [function_name] = :function_name  and [database_name]=:database_name and [database_schema]=:database_schema
)
BEGIN
    INSERT INTO [API].FunctionsList (
        [function_name],
        [date_created],
        [created_by],
        [sys_interface],
        [custom_function_name],
        [database_name],
        [database_schema]
    )
    VALUES (
        :function_name,
        GETDATE(),
        :username,
        :sys_interface,
        :custom_function_name,
        :database_name,
        :database_schema
    );
END

SELECT  SCOPE_IDENTITY() AS ID;
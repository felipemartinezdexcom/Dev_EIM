IF NOT EXISTS (
    SELECT 1 FROM [API].[FunctionParameters]
    WHERE [function_id] = :function_id
      AND [param_name] = :param_name
)
BEGIN
    INSERT INTO [API].[FunctionParameters] (
        [param_name],
        [data_type],
        [function_id],
        [date_created],
        [created_by],
        [required_param]
    )
    VALUES (
        :param_name,
        :data_type,
        :function_id,
        GETDATE(),
        :username,
        :required_param
    );
END
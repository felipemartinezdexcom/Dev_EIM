update [API].FunctionsList set database_name=:database_name ,database_schema=:database_schema,
last_date_modified=GETDATE(), last_modified_by=:username
where function_id=:function_id
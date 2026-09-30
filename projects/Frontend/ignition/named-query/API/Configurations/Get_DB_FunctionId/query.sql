select function_id from [API].FunctionsList 
where sys_interface='Database' 
and database_name=:database_name 
and database_schema=:database_schema 
and function_name=:function_name 
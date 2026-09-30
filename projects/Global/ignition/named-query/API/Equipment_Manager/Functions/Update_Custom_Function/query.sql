update [API].FunctionsList set function_name=:function_name , custom_function_name=:custom_function_name ,
last_date_modified=GETDATE(), last_modified_by=:username
where function_id=:function_id
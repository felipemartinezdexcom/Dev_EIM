SELECT FunctionsList.function_id,
	FunctionsList.function_name,
  FunctionsList.sys_interface,
  FunctionsList.custom_function_name,
  FunctionsList.database_name,
  FunctionsList.database_schema,
  FunctionGroupList.function_group_id
FROM [API].FunctionsList
  LEFT OUTER JOIN [API].FunctionGroupList ON FunctionsList.function_id =
    FunctionGroupList.function_id
    where FunctionGroupList.function_group_id=:function_group_id and FunctionsList.function_name=:function_name

   
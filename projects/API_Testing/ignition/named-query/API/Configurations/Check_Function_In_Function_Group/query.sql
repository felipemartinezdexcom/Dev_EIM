SELECT FunctionGroupList.function_group_id,
  FunctionGroupList.function_id,
  FunctionsList.function_name,
  FunctionsList.database_name,
  FunctionsList.database_schema,
  FunctionsList.sys_interface,
  FunctionsList.custom_function_name
FROM [API].FunctionGroupList
  LEFT OUTER JOIN [API].FunctionsList ON FunctionGroupList.function_id =
    FunctionsList.function_id
    where FunctionGroupList.function_group_id=:function_group_id and FunctionsList.function_name=:function_name


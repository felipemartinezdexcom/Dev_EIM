SELECT --FunctionGroupList.function_group_id,
  ---FunctionGroupList.function_id,
  FunctionsList.function_name,
  FunctionsList.sys_interface,
  FunctionsList.custom_function_name,
  FunctionsList.database_name,
  FunctionsList.database_schema,
  FunctionGroups.function_group_name
FROM [API].FunctionGroupList
  LEFT OUTER JOIN [API].FunctionsList ON FunctionGroupList.function_id =
    FunctionsList.function_id
  LEFT OUTER JOIN [API].FunctionGroups ON FunctionGroupList.function_group_id =
    FunctionGroups.function_group_id
    where FunctionGroupList.function_group_id=:function_group_id
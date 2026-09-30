SELECT FunctionGroupList.function_group_id,
  FunctionsList.function_name,
  FunctionsList1.database_name,
  FunctionsList1.database_schema,
  FunctionsList1.sys_interface,
  FunctionsList1.function_id

FROM [API].FunctionGroupList
  RIGHT OUTER JOIN [API].FunctionsList ON FunctionGroupList.function_id =
    FunctionsList.function_id
  LEFT OUTER JOIN [API].FunctionsList FunctionsList1 ON FunctionGroupList.function_id
    = FunctionsList1.function_id
     where FunctionGroupList.function_group_id=:function_group_id
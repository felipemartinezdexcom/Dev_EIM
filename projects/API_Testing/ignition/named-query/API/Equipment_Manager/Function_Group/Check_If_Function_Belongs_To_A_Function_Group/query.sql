SELECT FunctionGroupList.function_group_id,
  FunctionGroupList.function_id,
  FunctionGroups.function_group_name
FROM [API].FunctionGroupList
  LEFT OUTER JOIN [API].FunctionGroups ON FunctionGroupList.function_group_id =
    FunctionGroups.function_group_id
    where FunctionGroupList.function_id=:function_id

    
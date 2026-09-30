SELECT [API].FunctionGroupList.function_group_id,
  [API].FunctionsList.function_name
FROM [API].FunctionGroupList
  RIGHT OUTER JOIN [API].FunctionsList ON [API].FunctionGroupList.function_id =
    [API].FunctionsList.function_id
    where [API].FunctionGroupList.function_group_id=:function_group_id
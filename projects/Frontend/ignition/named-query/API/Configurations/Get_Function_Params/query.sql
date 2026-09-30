SELECT FunctionParameters.*,
  FunctionsList.function_name
FROM [API].FunctionParameters
  INNER JOIN [API].FunctionsList ON FunctionParameters.function_id =
    FunctionsList.function_id
    where  FunctionParameters.function_id=:function_id
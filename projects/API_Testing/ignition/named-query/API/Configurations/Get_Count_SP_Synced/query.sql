SELECT Count([API].FunctionsList.function_name) AS Count_function_name

FROM [API].FunctionsList
where [API].FunctionsList.sys_interface='database'

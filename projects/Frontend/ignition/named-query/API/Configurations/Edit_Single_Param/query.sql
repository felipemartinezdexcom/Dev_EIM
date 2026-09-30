update [API].FunctionParameters set param_name=:param_name, data_type=:data_type, required_param=:required_param,
last_date_modified=GETDATE(), last_modified_by=:username where param_id=:param_id
insert into [API].TransactionsLog ([timestamp],function_name, result,data,message,sys_interface,sql_timing,
exec_timing,simulator_call,simulator_user,input_params,valid_for_prod,gateway_name) 
values (GETDATE(), :function_name,:result,:data,:message,:sys_interface,:sqltiming,
:exectiming,:simulatorcall,:simulatoruser ,:input_params,:valid_for_prod,:gateway_name)
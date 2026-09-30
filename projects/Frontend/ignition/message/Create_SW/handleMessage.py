def handleMessage(payload):
	
	db_connection_name=payload['db_connection_name'] 
	schema =payload['schema'] 
	table_names=payload['table_names'] 
	
	Software_Version_String=API.Build_SQL.Functions.get_mssql_data_export(db_connection_name, schema, table_names)
	API.Build_SQL.Functions.insert_Software_Version(API.Build_SQL.Functions.TARGET_PATH, Software_Version_String)
	
	return "Sofware Revision Created successfully"
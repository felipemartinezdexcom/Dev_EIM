def onTagChange(initialChange, newValue, previousValue, event, executionCount):
	TARGET_PATH = "F:\Ignition\data\projects\API_Testing\ignition\script-python\API\Build_SQL\Functions\code.py"
	# Check if this is a startup/initial subscription event
	if initialChange:
	    # Exit early so the rest of the script doesn't run on save
	    pass 
	else:
		a=API.Build_SQL.Functions.get_mssql_data_export("API_Configurations","API",["FunctionsList","FunctionParameters","dataTypesList"])
		API.Build_SQL.Functions.insert_Software_Version(TARGET_PATH, a)
		
import json
import time
from java.lang import Throwable
import os
from collections import Counter
import API.Function_Calls
#try:
#	from com.inductiveautomation.ignition.gateway import IgnitionGateway
#except:
#	pass


def dataset_to_json(dataset):
    if not dataset or dataset.getRowCount() == 0:
        return []

    headers = list(dataset.getColumnNames())
    rows = []

    for row in dataset:
        rows.append({headers[i]: row[i] for i in range(len(headers))})

    #return json.dumps(rows, indent=4)
    return rows

def trans_sqlite_logger(function_name,result,data,message,sys_interface,input_params,valid_for_prod,gateway_name,sql_timing=None,exec_timing=None, simulator_user=None,simulator_call="NO"):

		
	logParams = {
	    "function_name": function_name,
	    "result": result,
	    "data": data,
	    "message":message,
	    "sqltiming":sql_timing,
	    "exectiming":exec_timing,
	    "simulatoruser":simulator_user,
	    "simulatorcall":simulator_call,
	    "sys_interface":sys_interface,
	    "input_params":input_params,
	    "valid_for_prod":valid_for_prod,
	    "gateway_name":gateway_name
	}	
	
	system.db.runNamedQuery("API/Configurations/Insert_Transaction_Record", logParams)


def check_machine_name_configured_active(machine_name):
	##0 does not exist
	##1 exist and active
	##2 exist not active
	data={
	  "machine_name_status":"",
	  "equipment_id":"",
	  "message":""
	  }
	  
	params={"machine_name":machine_name,
	  		"database": API.Variables.API_CONFIG_DB}
	machine_name_check_call=system.db.execQuery("API/Configurations/Check_Equipment_Valid_Active", params)
	machine_name_check_result=machine_name_check_call[0]['status']
	

	
	if machine_name_check_result==0:
		data['message']="""API EIM -- The provided EQ Number is not configured in the equipment list in EIM."""
		data['machine_name_status']=0
	elif machine_name_check_result==1:
		data['machine_name_status']=1
		data['equipment_id']=machine_name_check_call[0]['equipment_id']
	elif machine_name_check_result==2:
		data['message']="""API EIM -- The provided EQ Number is configured in the equipment list in EIM but it is not active."""
		data['machine_name_status']=2
	
	return data
	
def check_equipment_group(equipment_id):
	
	data={
	  "equipment_group_id":None,
	  "equipment_group_name":"",
	  "message":""
	  }
	  
	params={"equipment_id":equipment_id,
	  		"database": API.Variables.API_CONFIG_DB}
	equipment_group_check_call=system.db.execQuery("API/Configurations/Get_Equipment_Groups_for_Machine_Name", params)
	
	if len(equipment_group_check_call)==0:
		data['message']="""API EIM -- The equipment related to the provided EQ Number is not part of an equipment group.
		Please add the EQ Number into the right equipment group."""
	else:
		##condition for when the query returns data related to the equipment group related to the equipment name
		equipment_group_name=equipment_group_check_call[0]['equipment_group_name']
		equipment_group_id=equipment_group_check_call[0]['equipment_group_id']
		equipment_group_active=equipment_group_check_call[0]['active']
		
		if equipment_group_active==False:
			data['message']="""API EIM -- The equipment group {0} is not active. Please activate the equipment group first and try again""".format(equipment_group_name)
		
		elif equipment_group_active==True:		
			data['equipment_group_id']=equipment_group_id
			data['equipment_group_name']=equipment_group_name
	
	return data

def check_assignment_related(equipment_group_id,equipment_group_name):
	
	data={
	  "function_group_id":None,
	  "function_group_name":None,
	  "assignment_name":None,
	  "message":""
	  }
	params={"equipment_group_id":equipment_group_id,
	  		"database": API.Variables.API_CONFIG_DB}
	assignment_check_call=system.db.execQuery("API/Configurations/Get_Assignments_Retaled_To_Equipment_Group", params)
	
	if len(assignment_check_call)==0:
		data['message']="""API EIM -- There is no assignment related to equipment group: {0}.""".format(equipment_group_name)
	else:
		data['function_group_id']=[]
		data['function_group_name']=[]
		data['assignment_name']=[]
		for index in range(len(assignment_check_call)):

			function_group_name=assignment_check_call[index]['function_group_name']
			function_group_id=assignment_check_call[index]['function_group_id']
			assignment_name=assignment_check_call[index]['assignment_name']
		
			data['function_group_id'].append(function_group_id)
			data['assignment_name'].append(assignment_name)
			data['function_group_name'].append(function_group_name)
	return data
	
def check_function_in_function_group(function_name, function_group_id_list,function_group_name_list,assignment_name_list):
	
	data={
	  "function_id":None,
	  "sys_interface":None,
	  "custom_function_name":None,
	  "database_schema":None,
	  "database_name":None,
	  "message":""}
	
	single_function_instance=None
	##single assignment case
	if len(assignment_name_list)==1:
		params1={"function_name":function_name,
				 "function_group_id":function_group_id_list[0],
	  			 "database": API.Variables.API_CONFIG_DB}
		find_function_in_fg_call=system.db.execQuery("API/Configurations/Find_Function_Name_in_FG", params1)
		
		if len(find_function_in_fg_call)==0:
			data['message']="""API EIM -- The function name: {0} provided in the payload does not \n
							belong to  the function group: {1} related to the assignemt: {2}.""".format(function_name,str(function_group_name_list[0]),str(assignment_name_list[0])) 
		
		elif len(find_function_in_fg_call)==1:
			data['function_id']=find_function_in_fg_call[0]['function_id']
			data['sys_interface']=find_function_in_fg_call[0]['sys_interface']
			data['custom_function_name']=find_function_in_fg_call[0]['custom_function_name']
			data['database_schema']=find_function_in_fg_call[0]['database_schema']
			data['database_name']=find_function_in_fg_call[0]['database_name']

		
	##multi assignment case
	
	elif len(assignment_name_list)>1:
		function_found_count=0
		
		for function_group_id_element in function_group_id_list:
			  
			params2={"function_name":function_name,
					 "function_group_id":function_group_id_element,
	  				 "database": API.Variables.API_CONFIG_DB}
			find_function_in_fg_call=system.db.execQuery("API/Configurations/Find_Function_Name_in_FG", params2)
			if len(find_function_in_fg_call)!=0:
				function_found_count+=1
				single_function_instance=find_function_in_fg_call
				
				
		if function_found_count==0:
			data['message']="""API EIM -- The function name: {0} provided in the payload does not belong to any 
						 function group: {1} related to the assignemt(s): {2}. The function name 
						 must belong to only one of the function groups. Launch the management console and correct the issue.""".format(function_name,str(function_group_name_list),str(assignment_name_list)) 	
		
		elif function_found_count>1:
			data['message']="""API EIM -- The function name: {0} provided in the payload belongs to more than 1
							 function group: {1} related to the assignemt(s): {2}. If the equipment group has
							 multiple assignments, the function can only be in one of the function groups. Launch 
							 the management console and correct the issue.""".format(function_name,str(function_group_name_list),str(assignment_name_list)) 
		
		##desired outcome, only 1 found function instance
		elif function_found_count==1:
			#data['message']="valid"
			system.tag.writeBlocking(['[default]New Tag'],[len(single_function_instance)])
			data['function_id']=single_function_instance[0]['function_id']
			data['sys_interface']=single_function_instance[0]['sys_interface']
			data['custom_function_name']=single_function_instance[0]['custom_function_name']
			data['database_schema']=single_function_instance[0]['database_schema']
			data['database_name']=single_function_instance[0]['database_name']
	
	return data
	
def check_sp_configured(function_name):
		
	data={
		  "configured_Store_Procs":[],
		  "storeproc_Exist":False,
		  "sp_id": "",
		  "message":"",
		  "validated_for_prod":""
		  }
	
	#Check [API].FunctionsList
	storeprocs_call=system.db.execQuery("API/Configurations/Get_Functions")

	configured_Store_Procs_list=[]
	for sp in range(storeprocs_call.getRowCount()):
		configured_Store_Procs_list.append(str(storeprocs_call.getValueAt(sp,"function_name")))
	
	data['configured_Store_Procs']=configured_Store_Procs_list
	

	# Check if the provided path is correct
	if function_name in configured_Store_Procs_list:
	    data['storeproc_Exist']=True
	    
	    ##get sp_id
	    params={"function_name":function_name,
	  			"database": API.Variables.API_CONFIG_DB}
	    sp_id=system.db.execScalar("API/Configurations/Get_Function_ID_temp",params)
	    data['sp_id']=int(sp_id)
	    
	    ##check if validated for production use
	    data["validated_for_prod"]=system.db.execScalar("API/Configurations/Valid_For_Prod", params)
	
	else:
	    data['message']="""API EIM--The provided Store Procedure--{0} does not exist in the list of configured Store Procedures.
	    			 	Either Add a new Store Procedure or edit an existing one.""".format(function_name)
	   
	return data	
	


def check_function_input_parameters_configured(function_id,input_params):

	data={"same_number_of_params":False,
	  "all_params_match":False,
	  "all_required_params_provided":False,
	  "input_params_datatype_values":[],
	  "message":""
	  }

	params={"function_id":function_id,
	  		"database": API.Variables.API_CONFIG_DB}
	configured_sp_params_result=[]
	configured_sp_params_call=system.db.execQuery("API/Configurations/Get_Function_Params", params)
	

	
	
	inputParams=input_params
	notmatchingnameInputParams=[]
	missingEntryRequiredParams=[]
	#print inputParams.keys()
	
	#configuredParams=[{'required': 'YES', 'param_name': 'par1_mod'}, {'required': 'YES', 'param_name': 'par2'}, {'required': 'YES', 'param_name': 'par3'}]
	configured_SP_Params=[]
	configured_SP_Params_dicts=[]
	configured_SP_Params_datatype_values=[]
	
	###Get all configured params into a list
	for rownum in range(configured_sp_params_call.getRowCount()):
		configured_SP_Params.append(str(configured_sp_params_call.getValueAt(rownum,"param_name")))
		dict={"required":str(configured_sp_params_call.getValueAt(rownum,"required_param")),
		"param_name":str(configured_sp_params_call.getValueAt(rownum,"param_name"))}
		configured_SP_Params_dicts.append(dict)
	
	#print "configuref params dict: "+str(configured_SP_Params_dicts)
	
	##Check for same number of params
	data['same_number_of_params']= len(inputParams.keys())==len(configured_SP_Params)
	#print inputParams.keys()
	#print configured_SP_Params
	
	##Check if input params match same name of configure params
	if data['same_number_of_params']:
		for inparam in inputParams.keys():
			if inparam in configured_SP_Params:
				pass
			else:
				notmatchingnameInputParams.append(inparam)
				
		if len(notmatchingnameInputParams)==0:
			data['all_params_match']=True
			
			##check if all the required parameters have provided data
			for confparam in configured_SP_Params_dicts:
				if confparam['required']=='True':
					if inputParams[confparam['param_name']]=="" or inputParams[confparam['param_name']]==None:
						missingEntryRequiredParams.append(str(confparam['param_name']))
					else:
						pass
				else:
					pass
			
			if len(missingEntryRequiredParams)==0:
				data['all_required_params_provided']=True
				
				##Create dictionary of conf params with datatype--to pass to execution fucntion to call store proc
				for rownum in range(configured_sp_params_call.getRowCount()):
					#dict={"DatatypeDescription":str(configured_sp_params_call.getValueAt(rownum,"data_type")),
					#"value":input_params[configured_sp_params_call.getValueAt(rownum,"param_name")]}
					#configured_SP_Params_datatype_values.append(dict)

					dict={str(configured_sp_params_call.getValueAt(rownum,"param_name")):(str(configured_sp_params_call.getValueAt(rownum,"data_type")),
					input_params[configured_sp_params_call.getValueAt(rownum,"param_name")])}
					configured_SP_Params_datatype_values.append(dict)
					
				data["input_params_datatype_values"]=configured_SP_Params_datatype_values
				
				
			else:
				data['message']="""API EIM--One or more of the required input params was left empty.
				This is the list of required params that must have a value {0}""".format(missingEntryRequiredParams)
		
		else:
			data['message']="""API EIM--The provided parameters are not matching the configured parameters.
			This is the list of parameters not found in the configured parameters {0}""".format(notmatchingnameInputParams)

	else:
		data['message']="""API EIM--Mismatch of parameters count. You are either missing or have extra unconfigured params.
		Check the list of configured params against the list of provided input params.
		Provided Input Params: {0}.
		Configured Input Params: {1}.""".format(sorted(inputParams.keys()),sorted(configured_SP_Params))
	
	
	return data



def StoreProcParam_DataType(TypeDescription):
    if TypeDescription=="BOOL":
        return system.db.BOOLEAN
    elif TypeDescription=="INTEGER":
        return system.db.INTEGER
    elif TypeDescription=="FLOAT":
        return system.db.DOUBLE
    elif TypeDescription=="" or TypeDescription==None or TypeDescription=="VARCHAR":
        return system.db.VARCHAR 
    else:
        return system.db.VARCHAR


def execSProc( function_name,in_params,database_name,database_schema):

	
	data={
	    "result": False,
	    "data":[],
	    "message":""
			}
	
	
#	if inParams is None:
#	    inParams = {}
	
	
	# Create stored procedure call
	function="[{0}].{1}".format(database_schema,function_name)
	call = system.db.createSProcCall(function, database_name)
	#print inParams
	# Register IN params (type + value required)
	for param in in_params:

		#print param.keys()[0], param.values()[0][0], param.values()[0][1]
		storeProcDataType=StoreProcParam_DataType(param.values()[0][0])
		call.registerInParam(param.keys()[0], storeProcDataType, param.values()[0][1])
	
	
	try:
		
		
		# Execute
		system.db.execSProcCall(call)
		
		result = call.getResultSet()

		data['data'] = dataset_to_json(result)
		#data['data'] = result
		data['result']=True
	
		try:
			if result.getRowCount() > 0:
				data['message'] = "API-EIM--Data retrieval successful"
			else:
				data['message'] = "API EIM--No response from stored procedure"	
		
		##for store procedures that provide no return
		except:
			data['message'] = "API EIM--This Store Procedure does not provide a response."
			data['data'] = []
			data['result']=True
				    

	
	except Throwable, e:
	   data['message']  = "Database Error: " + str(e.getCause())
	   #data_to_return['timings']["total_ms"] = round((time.time() - start_total) * 1000, 2)
	
	except Exception, e:
	   data['message']  = "Scripting Error: " + str(e)
	   #data_to_return['timings']["total_ms"] = round((time.time() - start_total) * 1000, 2)
	
	return data
	
	

	
	
def get_db_status(dbname):	
	
	data={"db_status":"",
			"message":""}
			
	dbinfo=system.db.getConnectionInfo(dbname)
	data["db_status"]=dbinfo[0][3]
	
	if data["db_status"]!="Valid":
		data['message']="API EIM--The connection to database {0} is not valid. Contact Admin".format(dbname)
			
	return data		
			
	
def execution(payload,sys_interface=None,simulator_user=None,simulator_call="NO"):
	data={"result" : False,
	  "debug":None,
	  "data" : [],
	  "message" : "",
	  "gateway":system.tag.readBlocking(['[System]Gateway/SystemName'])[0].value,
	  "timings":{"total_ms":None,
	  			 "sql_execution_ms":None}
	  }
	
	try:
		machine_name=payload['machine_name']
		function_name=payload['function_name']
		input_parameters=payload['input_parameters']
	except:
		data['message']="API EIM--The provided input payload format is not correct."
		return data
	
	
	
	data={"result" : False,
		  "debug":None,
		  "data" : [],
		  "message" : "",
		  "gateway":system.tag.readBlocking(['[System]Gateway/SystemName'])[0].value,
		  "timings":{"total_ms":None,
		  			 "sql_execution_ms":None}
		  }
	start_total = time.time()
	##step1 Check if connectiont to db is valid
	db_status_call=get_db_status(API.Variables.API_CONFIG_DB)
	if db_status_call['db_status']=="Valid":
		
		##step2 chech if machine name is configured and active
		machine_name_status_functionCall=check_machine_name_configured_active(machine_name)
	else:
		data["message"]=db_status_call['message']
		return data

		
	if machine_name_status_functionCall['machine_name_status']==1:
		equipment_id=machine_name_status_functionCall['equipment_id']
		
		##step3 check the equipment group to which the equipment belongs to
		check_equipment_group_functionCall=check_equipment_group(equipment_id)
		equipment_group_id=check_equipment_group_functionCall['equipment_group_id']
		equipment_group_name=check_equipment_group_functionCall['equipment_group_name']
			
	else:		
		data["message"]=machine_name_status_functionCall['message']
		return data
	
	if equipment_group_id!=None:
				
		##step4 check if equipment group has any assignment 
		check_assignment_functionCall=check_assignment_related(equipment_group_id,equipment_group_name)
		function_group_id=check_assignment_functionCall['function_group_id']
		function_group_name=check_assignment_functionCall['function_group_name']
		assignment_name=check_assignment_functionCall['assignment_name']
				
	else:
		data["message"]=check_equipment_group_functionCall['message']
		return data
		
	if function_group_id!=None:
		
		##step5 check if function is in function group related to the assignment
		check_function_functionCall=check_function_in_function_group(function_name, function_group_id,function_group_name,assignment_name)
		function_id=check_function_functionCall['function_id']
		sys_interface=check_function_functionCall['sys_interface']
		custom_function_name=check_function_functionCall['custom_function_name']
		database_schema=check_function_functionCall['database_schema']
		database_name=check_function_functionCall['database_name']
					
	else:
		data["message"]=check_assignment_functionCall['message']
		return data
					
	if function_id!=None:
											
		###step6--Check that all provided input parameters are correct and all required params are provided
		input_params_functionCall=check_function_input_parameters_configured(function_id,input_parameters)
	else:
		data["message"]=check_function_functionCall['message']	
		return data
					
	if input_params_functionCall["same_number_of_params"] and input_params_functionCall["all_params_match"] and input_params_functionCall["all_required_params_provided"]:

		###step7--Check the type of sys interface to use
		if sys_interface=='Database':
			# --- SQL timing ---
			start_sql = time.time()
			##Execute Store Procedure once all check points are clear
			sp_call=execSProc( function_name, input_params_functionCall["input_params_datatype_values"],database_name,database_schema)
			end_sql = time.time()
			data['data']=sp_call['data']
			data['message']=sp_call['message']
			data['result']=sp_call['result']
			data['debug']='{0} {1}'.format(sys_interface,custom_function_name)
			data['timings'] = {
			"total_ms": round((time.time() - start_total) * 1000, 2),
			"sql_execution_ms": round((end_sql - start_sql) * 1000, 2)}
		
		elif sys_interface=='Custom Function':
			
			custom_function_object=API.Function_Calls.CustomFunctions(payload)
			custom_function_string='custom_function_object.{0}()'.format(custom_function_name)
			custom_function_call=eval(custom_function_string)

			data['data']=custom_function_call['data']
			data['message']=custom_function_call['message']
			data['result']=custom_function_call['result']
			data['timings'] = {"total_ms": round((time.time() - start_total) * 1000, 2)}

	else:
		data['message']=input_params_functionCall["message"]			
		return data
				


	
	##Log event
	#trans_sqlite_logger(function_name,data['result'],data['data'],data['message'],sys_interface,input_params,function_name_functionCall["validated_for_prod"],data['gateway'] ,data['timings']['sql_execution_ms'],data['timings']['total_ms'], simulator_user,simulator_call)
	return data



def sync_all_params_per_sp():
	username="DB_AutoSync"
	#storeProcID=self.parent.parent.getChild("Store Proc Dropdown").getChild("Dropdown").props.value
	#inputParams=self.parent.parent.getChild("FlexRepeater").props.instances
	all_fields_completed=True
	storeProcSelected=True
	
	messageboxparams={"data":{"icon": "material/info",
					  "title": "",
					  "level": "warning",
					  "message": ""
					  }
					  }
	
	##check if all fields are completed
	for item in inputParams:
		dataType,paramName,required=item.values()
		
		if paramName=="" or paramName==None or dataType=="" or dataType==None or required=="" or required==None:
			all_fields_completed=False
			break
		else:
			pass
	
	if storeProcID=="" or storeProcID==None:
		storeProcSelected=False
	
	if all_fields_completed==False or storeProcSelected==False:
		if all_fields_completed==False:
			messageboxparams['data']['message']="You have one or more empty fields. Please make sure all parameter names and data types are provided."
			messageboxparams['data']['title']="Missing Fields"
		elif storeProcSelected==False:
			messageboxparams['data']['message']="You must select a store procedure."
			messageboxparams['data']['title']="Missing Store Procedure"
						  
		system.perspective.openPopup("MissingReqs", "API_Screens/Pop_Ups/Message_Box",messageboxparams, showCloseIcon=False, draggable=False, resizable=False, modal=True, overlayDismiss=True)
	else: 
		
		messageboxparams['data']['message']="All the entry parameters were successfully added to the configuration file."
		messageboxparams['data']['title']="Successful Configuration"
		messageboxparams['data']["level"]= "success"
		messageboxparams['data']["icon"]= "material/add_circle"
		
	
		for item in inputParams:
			dataType,paramName,required=item.values()
			
			params={"param_name": paramName ,
					"sp_id": storeProcID,
					"data_type": dataType,
					"required_param": required,
					"username":username,
	  				"database": API.Variables.API_CONFIG_DB
					}
			
			system.db.execUpdate("API/Configurations/Insert_SP_Params",params)
			
		system.perspective.closePopup("")				  
		system.perspective.openPopup("MissingReqs", "API_Screens/Pop_Ups/Message_Box",messageboxparams, showCloseIcon=False, draggable=False, resizable=False, modal=True, overlayDismiss=True)
			





def sync_all_db_sp(sys_interface,Sync_Dev_DB,Sync_Dev_Schema,API_Config_DB):
	##work in progress feature to use store forward
	update_keywords=['set','create', 'log']
	
	data={"new_functions_added":[],
		  "already_existing_functions":[]}
	
	username="DB_AutoSync"
	
	params={"database":Sync_Dev_DB}
	server_db_name=system.db.execScalar("API/Configurations/Get_DB_Name", params)
	
	##Get All Store Procs
	params={"database":Sync_Dev_DB,
			"schema":Sync_Dev_Schema}
	storeProcs_call=system.db.execQuery("API/Configurations/Get_DB_SPs",params)
	storeProcs_list=[]
	

	for sp_row in range(storeProcs_call.getRowCount()):
		storeProcs_list.append(storeProcs_call.getValueAt(sp_row,'function_name'))
		
	print storeProcs_list	
	##insert all function_names in [API].FunctionsList
	for function_name in storeProcs_list:
		


		##if sp not exist
		try:				
			parameters1={"function_name":function_name,
						 "database_schema":Sync_Dev_Schema,
						 "database_name":server_db_name ,
						 "username":username,
						 "sys_interface":sys_interface,
						 "database":API.Variables.API_CONFIG_DB,
						 "custom_function_name":""}
			function_id_call=system.db.execQuery("API/Configurations/Add_Function", parameters1)
			function_id=int(function_id_call.getValueAt(0,0))
			data["new_functions_added"].append(str(function_name))
		except:
			## sp_id for existing sp
			parameters2={'function_name':function_name,
						 "schema":Sync_Dev_Schema,
						 "server_db_name":server_db_name,
						 "database":API.Variables.API_CONFIG_DB}
			function_id_call=system.db.execQuery("API/Configurations/Get_Function_ID", parameters2)
			function_id=function_id_call.getValueAt(0,0)
			data["already_existing_functions"].append(str(function_name))
			
			
		
		##Get all params for store proc
		
		parameters3={"function_name":function_name,
					 "database":Sync_Dev_DB,
					 "schema":Sync_Dev_Schema}
		storeProc_params_call=system.db.execQuery("API/Configurations/Get_DB_SP_Params", parameters3)
		for param_row in range(storeProc_params_call.getRowCount()):
			param_name=storeProc_params_call.getValueAt(param_row,'param_name')
			data_type=storeProc_params_call.getValueAt(param_row,'data_type')
			required_param=storeProc_params_call.getValueAt(param_row,'required_param')
			parameters4={"param_name": param_name[1:] ,
					"function_id": function_id,
					"data_type": data_type.upper(),
					"required_param": required_param,
					"username":username,
					"database":API_Config_DB
					}
			system.db.execUpdate("API/Configurations/Insert_Function_Params",parameters4)

	return data

def log_activity(payload):
	
	params={"username":payload['username'],
			"event_type":payload['event_type'],
			"before_change":payload['before_change'],
			"after_change":payload['after_change'],
			"description":payload['description'],
			"database":API.Variables.API_CONFIG_DB}
	system.db.execUpdate("API/Logs/Insert_Event", params)
	












def doPost(request, session):
	logger=system.util.getLogger("Api_Test")
	
	#import json
	
	#exec_params = request['data']['input_parameters']
	#EQNum = request['data']['EQNum']
	#reads = tagReads.tagReads(EQNum)
	#result, message, data = EIM.Applicator.CreateStationRecord(reads).execute(**exec_params)
	
	#return {'json': {'Data': data, 'Result': result, 'Message': message}, 'contentType': 'application/json'}
	
	#data=system.util.jsonDecode(request['data'])
	#inputParams=data['input_parameters']
	#print(inputParams)
	#SProcName=request['data
	#print(inputParams)
	#result=Bolt.Functions.callProc(inputParams, SProcName)
	logger.info(str(request['data']['inputParameters']))
	return {'json':{'Data': "TestData", 'Result': "TestResult", 'Message': type(request['data'])}, 'contentType': 'application/json'}
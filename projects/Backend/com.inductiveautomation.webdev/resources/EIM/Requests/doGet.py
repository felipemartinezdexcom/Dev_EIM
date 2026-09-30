def doGet(request, session):

	payload=request['data']

	logger=system.util.getLogger("inputparams")
	logger.info(str(payload))
	call=API.Functions.execution( payload,"Database")	
	
	
	
	return {'json':{"result": call['result'],
			"gateway":call['gateway'], 
			"data":call['data'] ,
			"message":call['message'],
			"times":call['timings'],
			"debug":call['debug']}, 'contentType': 'application/json'}
	
	#return {'json':{"result": call}, 'contentType': 'application/json'}
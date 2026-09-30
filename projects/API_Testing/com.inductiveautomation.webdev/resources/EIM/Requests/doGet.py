def doGet(request, session):

	payload=request['data']

	#logger=system.util.getLogger("inputparams")
	#logger.info(input_params)
	call=API.Functions.execution(payload,"Custom_Function")	
	

	logger = system.util.getLogger("API_Testing")
	logger.info("value=%s" % str(call))
	logger.info('type=%s' % str(type(call)))
	return {'json':{"result": call['result'],
			"gateway":call['gateway'], 
			"data":call['data'] ,
			"message":call['message'],
			"times":call['timings'],
			"debug":call['debug']}, 'contentType': 'application/json'}
	
	#return {'json':{"result": call}, 'contentType': 'application/json'}
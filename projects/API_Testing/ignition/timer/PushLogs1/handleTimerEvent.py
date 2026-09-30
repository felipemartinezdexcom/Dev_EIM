def handleTimerEvent():
	
	triggerTag=system.tag.readBlocking(['[default]TriggerLogs'])
	if triggerTag[0].value:
		API.Sim.prepare_and_send_request()
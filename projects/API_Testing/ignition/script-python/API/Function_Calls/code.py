from datetime import datetime
from java.lang import Throwable
import json
import java.sql.Timestamp, java.sql.JDBCType
import array
from collections import OrderedDict
from java.time import ZoneId, LocalDateTime, ZonedDateTime
import traceback
import time
#from API.Functions import DBIdentities, Properties, InputParameters

def get_sw_version():
    return Properties('SW15170', '1.0.0.0')

class Properties:
    def __init__(self, SWNumber, SWVersion):
        self.EQNumber = system.tag.readBlocking(['[EIM]MachineName'])[0].value
        self.SWNumber = SWNumber
        self.SWVersion = SWVersion
        self.Ignition_SWNumber = "SW14323"
        self.Ignition_SWVersion = system.util.getVersion().getBasicString()

class Result:
	def __init__(self):
		pass
	
	Success = 1
	Failure = 2
	Null_Result = 4

class CustomFunctions():
    def __init__(self,payload):
    	
    	self.payload=payload
    	self.response={
            "result": True,
            "debug": None,
            "data": None,
            "message": None,
            "payload":payload,
            "gateway": system.tag.readBlocking(['[System]Gateway/SystemName'])[0].value,
            "timings": {
                "total_ms": "",
                "sql_execution_ms": ""
            }
        }
        self.payloadParams = payload['input_parameters']
        self.machineName = payload['machine_name']
        self.functionName = payload['function_name']
        self.dbName = payload['database_name']
#        self.mdb_name = InputParameters.mdb_name
#        self.dbIDs = InputParameters.dbidentities
        self.properties = get_sw_version()
#        self.instanceName = InputParameters.instancename
#        self.tnl_properties = InputParameters.tnl_properties
#        self.mioDBName = InputParameters.mio_name
#        self.oltpDBName = InputParameters.oltp_name
        self.debug_log_all = None #InputParameters.debug_log_all if InputParameters.debug_log_all is not None else True
        self.debug_log_count = 10 #InputParameters.debug_log_count if InputParameters.debug_log_count > 0 else 10
        self.function_name = type(self).__name__
        self.thread_name = 'InputParameters.thread_name'
        self.instanceName = self.function_name

        # Set Logger
        self.loggerBaseName = "EIM Custom Function: " + self.machineName + "." + self.instanceName

        if self.function_name not in self.instanceName:
            self.loggerBaseName = self.loggerBaseName + " " + self.function_name

        if self.thread_name is not None:
            self.loggerBaseName = self.loggerBaseName + "_" + self.thread_name

        self.logger = system.util.getLogger(self.loggerBaseName)
        self.loggerLevel = 'INFO'
        system.util.setLoggingLevel(self.loggerBaseName, self.loggerLevel)
        self.opcenter_executions = OrderedDict()
        self.db_executions = OrderedDict()
        self.startTime = datetime.now()
        self.endTime = None
        self.debug_tag_path = '[EIM]Debug/' + self.machineName + '/' + self.instanceName + '/EIM/' + self.functionName
        self.debug_data = None
        self.traceback = None
    
    
    
    def handle_error(self, message):
    	self.logger.error(message)
    	self.traceback = traceback.format_exc()
    	return self.handle_return(Result.Failure, message)
    
    def handle_return(self, result=Result.Success, message=None):
    	self.endtime = datetime.now()
    	self.executionTime = (self.endTime - self.startTime).total_seconds()
    	self.logger.info("Total execution time: " + str(self.executionTime))
    	self.debug_log(result, message)
    	return result, message, self.response['data']
    
    

    		
    def debug_log(self, result, message):
    	
    	if result == Result.Failure or self.debug_log_all:
    		
    		log_dict = {'call_inputs': self.payloadParams, 
    					'function_outputs': self.response['data'], 'db_executions': self.db_executions,
    					'result': result, 'message': message, 'start_time': self.startTime, 'end_time': self.endTime,
    					'execution_time': self.response['timings'], 'timestamp': datetime.now(), 'traceback': self.traceback
    					}
    		
    		if len(self.opcenter_executions) > 0:
    			log_dict['opcenter_executions'] = self.opcenter_executions
    		
    		if result == Result.Failure:
    			self.logger.error(json.dumps(log_dict, default=self.json_helper))
    		
    		history_max = self.debug_log_count
    		
    		tag_read = system.tag.readBlocking([self.debug_tag_path])
    		
    		if tag_read[0].quality.isGood():
    			if tag_read[0].value is None or not isinstance(tag_read[0].value, array.array):
    				self.debug_data = []
    			else:
    				self.debug_data = list(tag_read[0].value)
    			del self.debug_data[history_max-1:]
    			
    			for i, elem in enumerate(self.debug_data):
    				if not isinstance(elem, dict):
    					try:
    						self.debug_data[i] = elem.toDict()
    					except:
    						self.debug_data[i] = None
    		else:
    			tag = [{'name': self.debug_tag_path.split('/')[-1], 'datatype': 'Document', 'tagType': 'AtomicTag'}]
    			create_tag = system.tag.configure('[EIM]Debug' + '/' + self.machineName + '/' + self.functionName
    												+ '/EIM/', tag, 'i')
    			self.debug_data = []
    		
    		self.debug_data.insert(0,log_dict)
    		asyncVals = system.util.jsonEncode(self.debug_data, 4)
    		system.tag.writeAsync([self.debug_tag_path], [asyncVals])
    				
    
    
	def handle_error(self, message):
	
		self.logger.error(message)
		self.traceback = traceback.format_exc()
		return self.handle_return(Result.Failure, message)
	
	def handle_return(self, result=Result.Success, message=None):
		
		self.endTime = datetime.now()
		self.executionTime = (self.endTime - self.startTime).total_seconds()
		
		self.logger.info("Total execution time: " + str(self.executionTime))
		self.debug_log(result, message)
		
		return result, message, self.response['data']
	
	
	def execute_opcenter_api(self, url, payload, timeout=5000, call_name=None):
	        """ Executes a Camstar API
	
	        Args:
	            url (str): Relative API URL
	            payload (dict): list of input parameters (system.db Type, Value)
	            timeout (int): Timeout in milliseconds
	            call_name (str/None): The name of the Opcenter Function (if different from function_name)
	
	        Returns:
	            result (bool): Result of read operation
	            message (str): Error message, if applicable
	            data (dict): Opcenter Returned Data
	            
	            how to get base camstar URL, username/pw coming from secret mgr, add the url as a secret? easy to sync, site specific so not a big deal
	            how would we use a VAL camstar? can point to val MDB but how to point to val camstar?
	            keep in DB? possbile, but other options are avail, can hardcode for testing but unresolved for prod.
	
	        """
	        try:
	
	            dict_key = call_name or self.function_name
	
	            if sproc_name in self.rest_executions:
					i = ""
					for x in reversed(self.rest_executions):
						if x == sproc_name or x.startswith(sproc_name + '#'):
							if len(x) == len(sproc_name):
								i = '#1'
							else:
								i = '#' + str(int(x.split('#')[1]) + 1)
						dict_key = sproc_name + i
						break
	
	            self.opcenter_executions[dict_key] = {'payload': payload, 'start_time': datetime.now(), 'auth': None}
	
	            result, message, self.opcenter_executions[dict_key]['auth'] = self.get_secret('Opcenter')
	
	            if result != Result.Success:
	                return result, message, None
				#URl not going in configs anymore?
	            if 'Opcenter_URL' not in self.configs:
	                return Result.Failure, "Opcenter_URL missing from EIM Configs", None
	
	            try:
	                self.opcenter_executions[dict_key]['url'] = self.configs['Opcenter_URL'] + url # still using self.configs?
	
	                client = system.net.httpClient(timeout=timeout,bypassCertValidation=False)
	
	                response = client.post(url=self.opcenter_executions[dict_key]['url'],
	                                           headers=self.opcenter_executions[dict_key]['auth'],
	                                           data=self.opcenter_executions[dict_key]['payload'],
	                                           timeout=timeout)
	
	            except Throwable, err_info:
	                self.opcenter_executions[dict_key]['exception'] = str(err_info.cause.message)
	                return Result.Failure, err_info.cause.message, None
	
	            try:
	                opcenter_response = response.json
	
	            except:
	                self.opcenter_executions[dict_key]['response'] = response.text
	
	                if not response.isGood():
	                    return Result.Failure, "Opcenter Returned status code: " + str(response.statusCode), None
	                else:
	                    return Result.Failure, "Opcenter Returned a non-JSON response", None
	
	            self.opcenter_executions[dict_key]['response'] = opcenter_response
	
	            self.opcenter_executions[dict_key]['execution_time'] = (
                (self.opcenter_executions[dict_key]['end_time'] -
                 self.opcenter_executions[dict_key]['start_time']).total_seconds())
	
	            if 'ErrorCode' in opcenter_response:
	                err_msg = 'No error message'
	                if 'Details' in opcenter_response and len(opcenter_response['Details']) > 0:
	                    if 'Message' in opcenter_response['Details'][0]:
	                        err_msg = opcenter_response['Details'][0]['Message']
	                return (Result.Failure, 'Opcenter ErrorCode ' + str(opcenter_response['ErrorCode']) + ' - ' + err_msg,
	                        opcenter_response)
	
	            return Result.Success, None, opcenter_response
	
	        except Throwable, err_info:
	            self.opcenter_executions[dict_key]['exception'] = str(err_info.cause.message)
	            return Result.Failure, err_info.cause.message, None
	
	        except Exception as e:
	            self.opcenter_executions[dict_key]['exception'] = str(e)
	            return Result.Failure, str(e), None
	
	

	def Custom_GetNextLot(self, call_type=None):
	    	
	    	try:
	            
	
	            url = ('/query/api/isResourceInquiry?$select=dexNextLot&$expand=dexNextLot($select=Name,PlannedQty,'
	                   'dexFGExpirationDate,dexFGManufactureDate;$expand=Product($select=Name,'
	                   'Revision))&eventname=ResolveNextLot')
	
	            call_types = {
	                'ASN': '/query/api/isResourceInquiry?$expand=Resource('
	                       '$select=dexLastSSCC)&$select=dexNextLot&$expand=dexNextLot($select=Name,PlannedQty,'
	                       'dexFGExpirationDate,dexFGManufactureDate,dexLastCarton;$expand=Product($select=Name,'
	                       'Revision))&eventname=ResolveNextLot',
	                'FMC': '/query/api/isResourceInquiry?$expand=Resource('
	                       '$select=dexLastSSCC)&$select=dexNextLot&$expand=dexNextLot($select=Name,PlannedQty,'
	                       'dexFGExpirationDate,dexFGManufactureDate,dexLastCarton;$expand=Product($select=Name,Revision,'
	                       'dexGTIN),$expand=Product($select=Name,Revision,dexGTIN,ProductVariation),$expand=MfgOrder('
	                       '$expand=MaterialList))&eventname=ResolveNextLot'
	            }
	
	            if call_type is not None:
	                if call_type in call_types:
	                    url = call_types[call_type]
	                else:
	                    self.response['message'] = str(call_type) + ' is not a valid call type. Falling back to default'
	
	            opcenter_payload = {"Resource": {"name": self.machineName}}
	
	            result, message, opcenter_response = self.execute_opcenter_api(url=url,
	                                                                           payload=opcenter_payload,
	                                                                           timeout=5000)
	            if result == Result.Failure:
	                self.response['result'] = result
	                return 
	
	            if opcenter_response is None:
	            	self.response['message'] = 'Opcenter Returned Null Response'
	                return 'Opcenter Returned Null Response'
	
	            if 'Resource' in opcenter_response and 'dexLastSSCC' in opcenter_response['Resource']:
	                self.response['data']["dexLastSSCC"] = opcenter_response["Resource"]["dexLastSSCC"]
	
	            if 'dexNextLot' in opcenter_response:
	                next_lot = opcenter_response['dexNextLot']
	
	                if next_lot is not None:
	                    self.response['data']['dexNextLot'] = next_lot
	
	                    return self.handle_return(Result.Success), self.response
	
	            return self.handle_return(Result.Null_Result)
	
	        except Throwable, err_info:
	            return self.error_handle(str(err_info))
	
	        except Exception as e:
	            return self.error_handle(str(e))

	def CreateProcessRecord(self):
		""" Creates a new Process Record in the MDB according to the context provided as parameter inputs

            Args:
                station_record_id (long): The Station Record
                txid (str): TxID of WIP
                result (bool): Pass/Fail Result
                pallet_id (str/None): Pallet ID
                reject_code (str/None): Reject Code, if applicable
                start_time (java.time.ZonedDateTime): Time process began on part
                end_time (java.time.ZonedDateTime): Time process ended on part
                subcomponents (dict): Dictionary containing subcomponent data
                process_data (dict): Dictionary containing process data
                station_name (str): Name of station processing part
                allocation_type (str): Allocation type of WIP
                part_number (str): Part Number of WIP
                lot_number (str): Lot Number of WIP
                cycle_time (float): Cycle time of process

            Returns:
                Tuple containing the overall result, error message, and Process Record ID.

        """
        try:
            self.execute_input_parameters = locals()

            if process_data is not None:
                if type(process_data) is not dict:
                    return self.error_handle('process_data must be a dictionary. Provided type: '
                                             + str(type(process_data)))
                else:
                    if station_name is not None:
                        process_data['ZoneStation'] = {'Value': 0.0, 'StrValue': None, 'TestPosition': station_name}
                    process_data_json = json.dumps(process_data)
            else:
                if station_name is not None:
                    process_data_json = json.dumps(
                        {'ZoneStation': {'Value': 0.0, 'StrValue': None, 'TestPosition': station_name}})
                else:
                    process_data_json = None

            if subcomponents is not None:
                if type(subcomponents) is not dict:
                    return self.error_handle('Subcomponents must be a dictionary. Provided type: '
                                             + str(type(subcomponents)))
                else:
                    subcomponents_json = json.dumps(subcomponents)
            else:
                subcomponents_json = None

            input_parameters = [('StationRecordID', system.db.BIGINT, station_record_id),
                                ('TXID', system.db.VARCHAR, txid),
                                ('PalletID', system.db.VARCHAR, pallet_id),
                                ('Result', system.db.BIT, result),
                                ('RejectCode', system.db.VARCHAR, reject_code),
                                ('StartTime', system.db.VARCHAR, start_time),
                                ('EndTime', system.db.VARCHAR, end_time),
                                ('Subcomponents', system.db.VARCHAR, subcomponents_json),
                                ('ProcessStepDetails', system.db.VARCHAR, process_data_json)]

            result, message, data, outputs = self.execute_sproc("FST.CreateProcessRecord", self.dexcomDBName,
                                                                input_parameters)

            if not result:
                exception_string = "TXID cannot be added to lot"
                failure_message = message
                if exception_string in failure_message:
                    self.logger.warn(txid + ' ' + failure_message)

                    try:
                        lot_number = failure_message.split('), as it has already been added to another lot (')[1][:-1]
                    except:
                        return self.return_handler(Result.Success)

                    input_parameters = [('EQNumber', system.db.VARCHAR, self.machineName),
                                        ('LotNumber', system.db.VARCHAR, lot_number)]

                    result, message, data, outputs = self.execute_sproc("FST.GetStationRecord", self.dexcomDBName,
                                                                        input_parameters)

                    if not result:
                        # self.logger.error(message)
                        return self.error_handle(message)

                    try:
                        station_record_id = data[0]["StationRecordID"]
                    except:
                        # self.logger.error("No valid results returned from FST.GetStationRecord")
                        return self.error_handle("No valid results returned from FST.GetStationRecord")

                    input_parameters = [('StationRecordID', system.db.BIGINT, station_record_id),
                                        ('TXID', system.db.VARCHAR, txid),
                                        ('PalletID', system.db.VARCHAR, pallet_id),
                                        ('Result', system.db.BIT, False),
                                        ('RejectCode', system.db.VARCHAR, '77000'),
                                        ('StartTime', system.db.VARCHAR, start_time),
                                        ('EndTime', system.db.VARCHAR, end_time),
                                        ('Subcomponents', system.db.VARCHAR, None),
                                        ('ProcessStepDetails', system.db.VARCHAR, process_data_json)]

                    result, message, data, outputs = self.execute_sproc("FST.CreateProcessRecord", self.dexcomDBName,
                                                                        input_parameters)

                    if result:
                        return self.return_handler(Result.Success)

                    else:
                        return self.error_handle(message)

                else:
                    return self.error_handle(message)

            try:
                self.data = data[0]["ProcessRecordID"]

            except:
                # If Null Data returned, set returnCode to NullData and log it
                return self.error_handle('No ProcessRecordID Returned')

            if self.data is None:
                # If Null Data returned, set returnCode to NullData and log it
                return self.error_handle('No ProcessRecordID Returned')

            if allocation_type is not None and allocation_type != "Commercial":
                # Define SP Call

                input_parameters = [("TXID", system.db.VARCHAR, txid),
                                    ("StationID", system.db.INTEGER, self.dbIdentities.stationid),
                                    ("AllocationType", system.db.VARCHAR, allocation_type),
                                    ("ProcessRecordID", system.db.BIGINT, self.data)
                                    ]

                result, message, data, outputs = self.execute_sproc("FST.SetTransmitterAllocation", self.dexcomDBName,
                                                                    input_parameters)

                if not result:
                    # Log error message from the SPC
                    return self.error_handle('FST.SetTransmitterAllocation: ' + str(message))

            ret_val = EIM.PIInterface.Applicator.process_record(self.machineName, station_name, station_record_id,
                                                                self.data, txid, result, pallet_id, reject_code,
                                                                self.datetime_to_string(start_time, True),
                                                                self.datetime_to_string(end_time, True),
                                                                subcomponents, process_data, allocation_type,
                                                                part_number, lot_number, cycle_time)

            return self.return_handler(Result.Success)

        except Exception as e:
            return self.error_handle(str(e))

    def InitializeCell(self, software_number_versions=None):
    	
    	try:
	        try:
	        	self.logger.trace(str(software_number_versions))
	        	sw_number = software_number_versions[0]['SW']
	        except:
	        	return self.handle_error("SoftwareNumberVersion not found")
	        
	        if sw_number is None or sw_number == '':
	        	return self.handle_error("SoftwareNumberVersion not found")
	        
	        
	        #modify payload and set interface for dbo.GetDatabaseInfo
	        sys_interface = 'Database'
	        self.payload['function_name'] = 'GetDatabaseInfo'
	        self.payload['input_paramters'] = {}
	        DatabaseInfo = API.Functions.execution(self.payload, sys_interface)
	        
	        if not DatabaseInfo['result']:
	        	return self.handle_error(DatabaseInfo['message'])
	        
	        if DatabaseInfo is not None:
	        	self.response['data']['DatabaseInfo'] = DatabaseInfo['data'][0]
	        else:
	        	return self.handle_error("GetDatabaseInfo returned no data")
	        
	        result_set = []
	        for machineName in [self.machineName, self.properties.EQNumber]:
	        	#modify payload for FST.GetStationInfo
	        	self.payload['function_name'] = 'GetStationInfo'
	        	self.payload['input_parameters'] = {"MachineName": self.machineName}
	        	GetStationInfo = API.Functions.execution(self.payload, sys_interface)
	        	
	        	if not GetStationInfo['result']:
	        		return self.handle_error(GetStationInfo['message'])
	        	result_set.append(GetStationInfo['data'][0])
	        
	        if result_set[0] is not None:
	        	self.response['data']['StationInfo'] = {'StationID': result_set[0]['StationID'],
	        											'EQNumber': result_set[0]['EQNumber'],
	        											'ProcessID': result_set[0]['ProcessID'],
	        											'ProcessName': result_set[0]['ProcessName'],
	        											'SWNumber': sw_number}
	        else:
	        	return self.handle_error("Station Info not returned")
	        
	        if result_set[1] is not None:
	        	eim_station_id = result_set[1]['StationID']
	        else:
	        	return self.handle_error("EIM Station ID Not Returned. EQNumber: " + str(self.properties.EQNumber))
	        	
	        result_set = []
	        stationID = self.response['data']['StationInfo']['StationID']
	        swNumber = self.response['data']['StationInfo']['SWNumber']
	        for station in [(stationID, swNumber),(eim_station_id, self.properties.SWNumber),
	         				(eim_station_id, self.tnl_properties_SWNumber)]:
	        	input_parameters = [{'StationID': station[0]}, {'SoftwareNumVer': station[1]}]
	        	#modify payload for dbo.GetStationConfig
	        	self.payload['function_name'] = 'GetStationConfig'
	        	self.payload['input_paramters'] = input_parameters
	        	GetStationConfig = API.Functions.execution(self.payload, sys_interface)
	        	
	        	if not GetStationConfig['result']:
	        		return self.handle_error(GetStationConfig['message'])
	        	result_set.append(GetStationInfo)
	        	
	        if result_set[0] is not None and len(result_set[0]) > 0:
	        	self.response['data']['StationParams'] = {}
	        	self.response['data']['StationConfigs'] = {}
	        	for row in result_set[0]:
	        		config_name = row['ConfigName']
	        		config_type = row['ConfigTypeName']
	        		config_value = row['Value']
	        		config_datatype = row['DataType']
	        		
	        		if config_type == "Station":
	        			self.response['data']['StationConfigs'][config_name] = self.parse_by_datatype(config_value, config_datatype)
	        		elif config_type == "Software":
	        			self.response['data']['StationParams'][config_name] = self.parse_by_datatype(config_value, config_datatype)
	        	
	        config_dict = {"StationID": eim_station_id, 'Database': self.dbName, 'Timestamp': str(datetime.now()),
	        				'TNL_Configs': {}}
	        
	        if result_set[1] is not None and len(result_set[1]) > 0:
	        	for row in result_set[1]:
	        		config_name = row['Configname']
	        		config_value = self.parse_by_datatype(row['Value'], row['DataType'])
	        		config_dict[config_name] = config_value
	        
	        if result_set[2] is not None and len(result_set[2]) > 0:
	        	for row in result_set[2]:
	        		config_name = row['ConfigName']
	        		config_value = self.parse_by_datatype(row['Value'], row['DataType'])
	        		config_dict['TNL_Configs'][config_name] = config_value
	        
	        basePath = "[EIM]Configs/"
	        tag_path = basePath + self.machineName
	        
	        if not system.tag.exists(tag_path):
	        	tag = [{'name': self.machineName, 'datatype': 'Document', 'tagType': 'AtomicTag'}]
	        	result = system.tag.configure(base_path, tag, 'o')
	        result = system.tag.writeBlocking([tag_path], [json.dumps(config_dict)])
	        
	        self.response['data']['EIMConfigs'] = config_dict
	        
	        input_paramters = [{'StationID', stationID}, {'SoftwareNumberVersions': json.dumps(software_number_versions)}]
	        #modify payload for FST.SetStationProcessSoftware
	        self.payload['function_name'] = 'SetStationProcessSoftware'
	        self.payload['input_parameters'] = input_parameters
	        SetStationProcessSoftware = API.Functions.execution(self.payload, sys_interface)
	        
	        if not SetStationProcessSoftware['result']:
	        	self.handle_error(SetStationProcessSoftware['message'])
	        
	        software_number_versions = [{'SW': self.properties.SWNumber, 'Ver': self.properties.SWVersion},
	        							{'SW': self.tnl_properties.SWNumber, 'Ver': self.tnl_properties.SWVersion},
	        							{'SW': self.properties.Ignition_SWNumber, 'Ver': self.properties.Ignition_SWVersion}]
	        
	        input_params = [{"StationID": eim_station_id}, {"SoftwareNumberVersions": json.dumps(software_number_versions)}]
	        #modify payload for FST.SetStationProcessSoftware
	        self.payload['input_parameters'] = input_parameters
	        SetStationProcessSoftware = API.Functions.execution(self.payload, sys_interface)
	        
	        if not SetStationProcessSoftware['result']:
	        	self.handle_error(SetStationProcessSoftware['message'])
	        
	        self.logger.info("InitializeCell Complete")
	        return self.handle_return(Result.Success)
        
        except Exception as e:
        	self.logger.error(str(traceback.format_exc()))
        	return self.handle_error(str(e))
        	
    
    
    
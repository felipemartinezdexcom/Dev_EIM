import random
import time
import traceback
from java.lang import Throwable


def send_request(data_dict):
	logging=system.util.getLogger("EIM-TestLog")
	url = "http://30.30.30.50:8088/system/webdev/API_Testing/EIM/Requests"
	#client = system.net.httpClient()
	
	try:
		client = system.net.httpClient()
		response = client.get(url, params=data_dict)
		if response.json['result']==False:
			logdata={"EIM-Received-Payload": True,
					"EIM-Routed-Payload": False,
					"Reason-Failed-to-Route":response.json['message'],
					"EIM-Received-Payload": data_dict}
			logging.errorf("EIM Test Log: %s", str(logdata))
		return response
	except Exception as e:
	#except:
	    logging.errorf("EIM Transaction:%s ,Error1 during API call: %s", str(data_dict), str(e))
	    #logging.error("Error during API call: %s")
	    return None


	
	
	except Throwable as jErr:
	    # Catches underlying Java engine errors (SQL, OPC UA, Tag writes)
	    error_msg = "Java Error: %s" % jErr.getCause()
	    logging.errorf("EIM Transaction:%sError2 during API call: %s", str(data_dict), str(jErr))
	    #logging.error("Error during API call: %s")
	    return None




def get_dynamic_function_name():
    function_list = [
        "CloseCradleSession",
        "CloseProcessRecord",
        "CreateCradleSession",
        "CreateProcessRecord",
        "CreateStationRecord",
        "GetBathRecipeList",
        "GetBathRecipeParameters",
        "GetCradleStatus",
        "GetEnvironmentalValues",
        "GetLogoutReasons"
    ]
    return random.choice(function_list)


def generate_random_input_params():
    lot_types = ["TypeA", "TypeB", "TypeC"]
    part_numbers = ["P1001", "P1002", "P1003"]
    quantities = [1, 5, 10]

    val1 = random.randint(1, 99)
    val2 = random.randint(100, 999)

    random_params = {
        "ExpirationDate": "2024-12-31",
        "FeederName": "Feeder_{}".format(random.randint(1, 5)),
        "LotAllocationType": random.choice(lot_types),
        "LotTypeID": random.randint(1, 10),
        "MtLotNumber": "LOT-{}".format(val1),
        "MtPartNumber": "PART-{}".format(val2),
        "PartDescription": "Part_{}_Desc".format(val1).format(val2),
        "PartVersion": "v{0}".format(random.randint(1, 5)),
        "Quantity": random.choice(quantities),
        "StationEQ": "EQ-{}".format(random.randint(1, 50)),
        "StationID": "ID_{}".format(val2)
    }
    return random_params


def generate_random_machine_name():
    num = random.randint(1, 20)
    return "EQ-BOLT-{:04d}".format(num)


def prepare_and_send_request():

	machine_name = generate_random_machine_name()
	func_name = get_dynamic_function_name()
	params = generate_random_input_params()
	
	data_dict = {
	    "machine_name": machine_name,
	    "function_name": func_name,
	    "input_parameters": params
	}
	


	
	return send_request(data_dict)

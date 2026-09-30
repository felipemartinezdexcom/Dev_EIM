import time

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
	
  

    def Custom_func1(self):
        # Modify payload
        self.response["data"] = self.payload
        self.response["message"] = "Function 1 completed"

        return self.response

    def Custom_func2(self):
        # Modify payload
        self.response["data"] = "Custom_func2"
        self.response["message"] = "Function 2 completed"

        return self.response

    def Custom_func3(self):
        # Modify payload
        self.response["data"]= "Custom_func3"
        self.response["message"] = "Function 3 completed"

        return self.response
        
    def Custom_func6(self):
        # Modify payload
        self.response["data"]= "THis is another funct"
        self.response["message"] = "Test function number 6"

        return self.response
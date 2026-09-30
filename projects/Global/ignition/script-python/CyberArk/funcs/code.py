from API_Calls.Vars import *

def read_secret_value(LocalProviderName, secretName):
	pyPlaintext = system.secrets.readSecretValue(LocalProviderName, secretName)
	asString = pyPlaintext.getSecretAsString()
	pyPlaintext.clear()
	return asString


def list_provider_secrets(GWName, RemoteProviderName, LocalProviderName):
	##Find Ip_Port
	params={"GWName":GWName}
	selectedGateway=system.db.execQuery("LookUps/GW_IP_Port", params)
	IP_Port=selectedGateway[0][1]
	print(IP_Port)
	url="http://"+IP_Port+"/data/api/v1/secret-providers/"+RemoteProviderName+"/secrets"
	token=read_secret_value(LocalProviderName,GWName)
	print(token)
	headers = {'X-Ignition-API-Token': token ,'Content-Type':'application/json'}	
	client = system.net.httpClient()

	secretsList=client.get(url, headers=headers)
	
	return secretsList.json['secrets']
	
def get_Local_Secrets(LocalProviderName, secretName):
	token=read_secret_value(LocalProviderName, secretName)
	url="http://192.168.0.117:8081/data/api/v1/resources/find/ignition/secret-provider/"+LocalProviderName
	headers = { 'X-Ignition-API-Token': token ,'Content-Type':'application/json'}
	client = system.net.httpClient()
	secretsData=client.get(url, headers=headers)
	
	return secretsData.json['config']['settings']['secrets']

	
def addNewSecretProvider(ProviderName,ProviderDescription,IP_Port,token):
	template=addSecretProvider_Template(ProviderName,ProviderDescription)
	
	url="http://"+IP_Port+"/data/api/v1/resources/ignition/secret-provider"
	headers = { 
    'X-Ignition-API-Token': token,'Content-Type':'application/json'}
	client = system.net.httpClient()
	response=client.post(url, headers=headers,data=template)
	print template
	print(response)
	
	return response
	
def insertSecretUpdateLogs(data):
	params={"msg_code":data["msg_code"],"msg_text":str(data["msg_text"]),"gateway_name":data["gateway_name"],"step":data['step']}
	#print(data)

	system.db.execUpdate("Inserts/Logs/Secret_Syncs", params)
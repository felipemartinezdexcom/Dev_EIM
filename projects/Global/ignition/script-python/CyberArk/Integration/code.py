from urllib import urlencode
from API_Calls.funcs import *

def Authen_Cyber(accountName):
	try:
		LocalProviderName="CyberArk_Details"
		
		clientId= read_secret_value(LocalProviderName, "clientId")
		clientSecret= read_secret_value(LocalProviderName, "clientSecret")
		#print(clientId,clientSecret)
		
		clientID = clientId
		clientSECRET = clientSecret
		body = {
		    "grant_type":"client_credentials",
		    "client_id":clientID,
		    "client_secret":clientSECRET}
		
		
		url="https://aat4659.id.cyberark.cloud/oauth2/platformtoken" 
		response=system.util.jsonDecode(system.net.httpPost(url,'application/x-www-form-urlencoded',postData=urlencode(body)))
		token=response['access_token']
		
		#print("account: "+accountName)
		
		#print("token: "+token)
		headers = {'Content-Type': 'application/json','Authorization':'Bearer '+token}
		url="https://dexcom.privilegecloud.cyberark.cloud/PasswordVault/API/Accounts?search="+accountName
		
		
		response=system.util.jsonDecode(system.net.httpGet(url, headerValues=headers))
		accountId=response['value'][0]['id']
		
		body = {"reason":"Test"}
		
		#print(accountId)
		
		url="https://dexcom.privilegecloud.cyberark.cloud/PasswordVault/API/Accounts/"+accountId+"/Password/Retrieve"
		response=system.net.httpPost(url,'application/json',postData=body, headerValues=headers)
		#print(response)
		
		return response


	
		    
	except:
		
		#logger.info("Unable to reach the cyber ark server. No new secrets were retrieved")
		print("Unable to reach the cyber ark server. No new secrets were retrieved")
		
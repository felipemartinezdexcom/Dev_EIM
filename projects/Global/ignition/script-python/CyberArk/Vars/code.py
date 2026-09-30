
def addSecretProvider_Template(Name,Description):
	return	[
  {
    "name": Name,
    "enabled": True,
    "description": Description,
    "config": {
      "profile": {
        "type": "internal"
      },
      "settings": {
        "secrets": {
        
        }
      }
    },
    "backupConfig": {
      "profile": {
        "type": "internal"
      },
      "settings": {
        "secrets": {
        }
      }
    }
  }
]


def addDBConnection(Name,Description):
	return [
  {
    "name": Name,
    "enabled": True,
    "description": Description,
    "config": {
      "driver": "Microsoft SQLServer",
      "translator": "MSSQL",
      "includeSchemaInTableName": False,
      "connectURL": "jdbc:sqlserver://mssql-db",
      "username": "IgnUser",
      "password":  {
            "type": "Referenced",
            "data": {
                "providerName": "ALL_PWs",
                "secretName": "LocalDB"
            },
      "connectionProps": "",
      "connectionResetParams": "",
      "defaultTransactionLevel": "DEFAULT",
      "poolInitSize": 0,
      "poolMaxActive": 8,
      "poolMaxIdle": 8,
      "poolMinIdle": 0,
      "poolMaxWait": 5000,
      "validationQuery": "SELECT 1",
      "testOnBorrow": True,
      "testOnReturn": False,
      "testWhileIdle": False,
      "evictionRate": -1,
      "evictionTests": 3,
      "evictionTime": 1800000,
      "failoverProfile": "string",
      "failoverMode": "STANDARD",
      "slowQueryLogThreshold": 60000,
      "validationSleepTime": 10000
    },
    "backupConfig": {
    }
  }
  }
]


def addConnector(Name,Description):
	return [
  {
    "name": Name,
    "enabled": True,
    "description": Description,
    "config": {
    "profile": {
            "type": "kafka"
        },
        "settings": {
            "bootstrapServers": [
                "kafka:29092"
            ],
            "saslMechanism": "GSSAPI",
            "securityProtocol": "PLAINTEXT",
            "username": "IgnUser",
            "password": {
                "type": "Referenced",      
                
                "data": {
          					"providerName": "ALL_PWs",
                			"secretName": "Kafka_Local"
                }
            },
            "ssl": {
                "protocol": "TLSv1.3",
                "keystore": {},
                "truststore": {}
            },
            "props": {
                "client": "",
                "consumer": ""
            }
        }

    }

      }
]
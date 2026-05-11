import json

class configHandler:

    configFileName = "ModProtGrowattV1.39.json"
    defaultRegister = "holdingRegister"

    def __init__(self, fileName=configFileName):
        self.configFileName = fileName

    def getRegisterVariables(self, targetRegister = defaultRegister):
        with open(self.configFileName) as configFileRef:
            data = json.load(configFileRef)
        variables = data[targetRegister]
        #print(variables)
        return variables
    
    # def getAllVariables(self):
    
    #     with open(self.configFileName) as configFileRef:
    #         data = json.load(configFileRef)

    #     for (register, variables) in data.items():
    #         #print(register)
    #         #print(variables)

    #         for variable in variables:
    #             print(variable)





    




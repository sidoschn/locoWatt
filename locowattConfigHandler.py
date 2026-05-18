import json

class configHandler:
    configFileName = "ModProtGrowattV1.39.json"
    defaultRegister = "holdingRegister"

    def __init__(self, fileName=configFileName):
        self.configFileName = fileName
        with open(self.configFileName) as configFileRef:
            variables = json.load(configFileRef)
        
        self.registerVariableDict = {}
        for key, value in variables.items():
            self.registerVariableDict[key] = registerVariable(value)
            
            # if (len(self.registerVariableList)<1):
            #     self.registerVariableList = [registerVariable(varDict)]
            # else:
            #     self.registerVariableList.append(registerVariable(varDict))


        # self.registerVariableList = []
        # for varDict in variables:
        #     if (len(self.registerVariableList)<1):
        #         self.registerVariableList = [registerVariable(varDict)]
        #     else:
        #         self.registerVariableList.append(registerVariable(varDict))

class registerVariable:
    defaultRegisterDict = {"register":3,"address":0,"length":1,"type":"int","maxVal":3,"minVal":0,"bWriteable":True, "valueMultiplier":1,"unit":""}
    

    def __init__(self, registerDict=defaultRegisterDict):
        self.register = registerDict["register"]
        #self.name = registerDict["name"]
        self.address = registerDict["address"]
        self.length = registerDict["length"]
        self.type = registerDict["type"]
        self.bWriteable = registerDict["bWriteable"]
        self.valueMultiplier = registerDict["valueMultiplier"]
        self.unit = registerDict["unit"]
        self.populatedRegisterDict={}
        for entry in registerDict:
            self.populatedRegisterDict[entry]= registerDict[entry]

    def content(self):
        return self.populatedRegisterDict


    
# # legacy code


# register = 3
    # name = "OnOff"
    # address = 0
    # length = 1
    # type = "int"
    # maxVal = 255
    # minVal = 0
    # bWriteable = True
    # valueMultiplier = 1
    # unit = ""


# def getRegisterVariables(self):
    #     with open(self.configFileName) as configFileRef:
    #         variables = json.load(configFileRef)
        
    #     self.registerVariableList = []
    #     for varDict in variables:
    #         if len(self.registerVariableList<1):
    #             self.registerVariableList = [registerVariable(varDict)]
    #         else:
    #             self.registerVariableList.append(registerVariable(varDict))


        #print(variables)
    
    # def getAllVariables(self):
    
    #     with open(self.configFileName) as configFileRef:
    #         data = json.load(configFileRef)

    #     for (register, variables) in data.items():
    #         #print(register)
    #         #print(variables)

    #         for variable in variables:
    #             print(variable)
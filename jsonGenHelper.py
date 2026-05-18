import json

outDict = {}
StartReg = 142
for i in range(1,17,1):
    outDict["V_String"+str(i)] = {"register":4,"address":StartReg+(i*2) ,"length":1,"type":"int", "bWriteable":False, "valueMultiplier":0.1,"unit":" V", "bMakeSensor":True}
    outDict["Curr_Sting"+str(i)] = {"register":4,"address":StartReg+1+(i*2) ,"length":1,"type":"int", "bWriteable":False, "valueMultiplier":0.1,"unit":" A", "bMakeSensor":True}


with open ("helper.json", "w") as f:
    json.dump(outDict, f)


for key in outDict:
    print(""+str(key) + ": "+str(outDict[key]) + ",")
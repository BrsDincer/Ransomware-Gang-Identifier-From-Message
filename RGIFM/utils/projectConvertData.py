from utils.projectFunctions import GETISFILE,RETURNINITIALERROR,RETURNINITIALMESSAGE
from utils.projectDirectories import MAINDIRECTORIES
from typing import Type
import os,json

def CONVERTMESSAGEDATA()->Type[bool]:
    resultDict = {}
    for mainDir,_,files in os.walk(MAINDIRECTORIES.SOURCE):
        try:
            if len(files) > 0:
                for initFile in files:
                    mainPath = os.path.join(mainDir,initFile)
                    isFile = GETISFILE(mainPath)
                    if isFile:
                        gangName = mainPath.split("\\")[-2]
                        _,fileExt = os.path.splitext(mainPath)
                        if fileExt == ".txt":
                            normPath = os.path.normpath(mainPath)
                            with open(str(normPath),"r",encoding="utf-8",errors="ignore") as ops:
                                dataRaw = ops.read()
                            if gangName not in resultDict:
                                resultDict[gangName] = []
                            resultDict[gangName].append(str(dataRaw))
                        else:
                            pass
                    else:
                        pass
            else:
                pass
        except Exception as err:
            RETURNINITIALERROR(err)
            return False
    if len(resultDict) > 0:
        with open(MAINDIRECTORIES.MESSAGESOURCE,"w",encoding="utf-8") as wops:
            json.dump(resultDict,wops,indent=4,sort_keys=False,allow_nan=True)
        RETURNINITIALMESSAGE(f"MESSAGE DATA HAS BEEN SAVED TO {MAINDIRECTORIES.MESSAGESOURCE}")
        return True
    else:
        RETURNINITIALMESSAGE(F"NOTHING TO SAVE")
        return False
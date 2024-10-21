from utils.projectFunctions import RETURNINITIALMESSAGE,GETISFILE
from utils.projectDirectories import MAINDIRECTORIES
from typing import Union
import json

def READMESSAGEDATA()->Union[dict,None]:
    if GETISFILE(MAINDIRECTORIES.MESSAGESOURCE):
        source = json.load(open(MAINDIRECTORIES.MESSAGESOURCE,"r"))
        return source
    else:
        RETURNINITIALMESSAGE("MESSAGE SOURCE NOT AVAILABLE - CHECK DIRECTORY")
        return None

from utils.projectUtilization import I_Function
from typing import Type
from datetime import datetime
import os,shutil,re,difflib,string,math

CREATEDIRECTORY:Type[I_Function] = lambda path:os.makedirs(path,exist_ok=True)
DELETEDIRECTORY:Type[I_Function] = lambda path:shutil.rmtree(path) if (os.path.exists(path)) else None
GETISFILE:Type[I_Function] = lambda path:True if os.path.isfile(path) else None
RETURNINITIALMESSAGE:Type[I_Function] = lambda message:print(f"[ INITIAL INFORMATION ] [?] {message}")
RETURNINITIALERROR:Type[I_Function] = lambda message:print(f"[ INITIAL ERROR ] [!] {message}")
FINDGENERALURL:Type[I_Function] = lambda raw:re.findall(r'((smb|srm|ssh|ftps?|file|https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)',raw,re.MULTILINE)
FINDIP:Type[I_Function] = lambda raw:re.findall(r'[0-9]+(?:\.[0-9]+){3}',raw)
FINDEMAIL:Type[I_Function] = lambda raw:re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',raw)
CALCULATESEQUENCE:Type[I_Function] = lambda msg,raw:round(difflib.SequenceMatcher(None,msg,str(raw)).ratio(),4)
GETTIMENOW:Type[I_Function] = lambda:datetime.now()
TRANSLATIONTABLE:Type[I_Function] = str.maketrans(string.punctuation+string.ascii_uppercase," "*len(string.punctuation)+string.ascii_uppercase)

def COUNTFREQUENCY(wordlist:Type[list])->Type[dict]:
    frequency = {}
    for word in wordlist:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def DOTPRODUCT(ratio_1:Type[dict],ratio_2:Type[dict])->Type[float]:
    result = 0.0
    for r in ratio_1:
        if r in ratio_2:
            result += (ratio_1[r]*ratio_2[r])
        else:
            pass
    return result

def VECTORANGLE(ratio_1:Type[dict],ratio_2:Type[dict])->Type[float]:
    numerator = DOTPRODUCT(ratio_1,ratio_2)
    denominator = math.sqrt(DOTPRODUCT(ratio_1,ratio_1)*DOTPRODUCT(ratio_2,ratio_2))
    return round(math.acos(numerator/denominator),4)

def CHECKVALIDIP(raw:Type[str])->Type[bool]:
    try:
        initial = raw.split(".")
        validation = [int(init) for init in initial]
        validation = [bt for bt in validation if (bt >= 0) and (bt <= 255)]
        return (len(initial) == 4) and (len(validation) == 4)
    except:
        return False

from utils.projectFunctions import RETURNINITIALMESSAGE,TRANSLATIONTABLE,COUNTFREQUENCY,CALCULATESEQUENCE
from utils.projectReadData import READMESSAGEDATA
from modules.stringExtraction import GetStringExtraction
from typing import Union,Type
from operator import itemgetter

def GetSequenceCalculation(raw:Type[str],threshold:Type[float]=0.7000)->Union[dict,None]:
    retries = {}
    data = READMESSAGEDATA()
    count = 0
    if data is not None:
        try:
            retries["MAIN_MOST_USED_WORD"] = {}
            retries["STRING_RESULT"] = GetStringExtraction(raw)
            wordlistRaw = raw.translate(TRANSLATIONTABLE).split()
            frequencyRaw = COUNTFREQUENCY(wordlistRaw)
            try:
                mostMain = sorted(frequencyRaw.items(),key=itemgetter(1),reverse=True)[:10]
            except:
                try:
                    mostMain = sorted(frequencyRaw.items(),key=itemgetter(1),reverse=True)[:4]
                except:
                    mostMain = []
            if len(mostMain) > 0:
                for itemInit in mostMain:
                    retries["MAIN_MOST_USED_WORD"][itemInit[0]] = itemInit[1]
            else:
                pass
            for key,val in data.items():
                for msg in val:
                    seqRatio = CALCULATESEQUENCE(msg,raw)
                    if seqRatio >= threshold:
                        count += 1
                        if key not in retries:
                            retries[key] = {}
                        retries[key][f"SEQUENCE_RATIO_RELATED_TO_MESSAGE_DATA_{count}"] = seqRatio
                    else:
                        pass
                count = 0
            return retries
        except:
            return None
    else:
        RETURNINITIALMESSAGE("SIMILARITY COULD NOT BE CALCULATED")
        return None
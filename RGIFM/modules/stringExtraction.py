from utils.projectFunctions import FINDGENERALURL,FINDIP,FINDEMAIL,CHECKVALIDIP,RETURNINITIALERROR,RETURNINITIALMESSAGE
from typing import Union,Type

def GetStringExtraction(raw:Type[str])->Union[dict,None]:
    results = {}
    results["URL"] = []
    results["IP"] = []
    results["EMAIL"] = []
    emails = FINDEMAIL(raw)
    urls = FINDGENERALURL(raw)
    ips = FINDIP(raw)
    if urls:
        try:
            for url in urls:
                if url not in results["URL"]:
                    results["URL"].append(url[0])
                else:
                    pass
        except:
            pass
    else:
        pass
    if ips:
        try:
            for ip in ips:
                isValid = CHECKVALIDIP(ip)
                if isValid:
                    if ip not in results["IP"]:
                        results["IP"].append(ip)
                    else:
                        pass
                else:
                    pass
        except:
            pass
    else:
        pass
    if emails:
        try:
            for mail in emails:
                if mail not in results["EMAIL"]:
                    results["EMAIL"].append(mail)
        except:
            pass
    return results

    


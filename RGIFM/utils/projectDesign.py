from utils.projectFunctions import RETURNINITIALMESSAGE
from typing import Type

def PrintBaseHeader()->Type[None]:
    banner = """

         ____   ____ ___ _____ __  __ 
        |  _ \ / ___|_ _|  ___|  \/  |
        | |_) | |  _ | || |_  | |\/| |
        |  _ <| |_| || ||  _| | |  | |
        |_| \_\\____|___| _|   |_|  |_|

    A CTI-CYBER THREAT INTELLIGENCE PROJECT

    [ RGIFM - V:0.0.1 ]
    >> Ransomware Gang Identifier From Message

"""
    print(banner)

def PrintWarningMessage()->Type[None]:
    print("\n\tText recognition and similarity are performed using different convergence and angular calculations.")
    print("\tDo not forget to check the outputs you find.")

def PrintSubHeader(inputTitle:Type[str])->Type[None]:
    print("\n")
    print("".ljust(50,"-"))
    print(str(inputTitle).upper())
    print("".ljust(50,"-"))

def PrintMetaHeader(inputTitle:Type[str])->Type[None]:
    print("\n")
    print("".ljust(20,">"))
    print(str(inputTitle).upper())
    print("".ljust(20,">"))
    print("\n")

def PrintUsageExamples()->Type[None]:
    usageOutput = """

    python .\RGIFM.py <TARGET_MESSAGE_FILE> --all
    python .\RGIFM.py <TARGET_MESSAGE_FILE> --sequence
    python .\RGIFM.py <TARGET_MESSAGE_FILE> --distance
    python .\RGIFM.py <TARGET_MESSAGE_FILE> --jaccard
    python .\RGIFM.py <TARGET_MESSAGE_FILE> -s -d -j
    
"""
    print(usageOutput)

def PrintResults(rawOutput:Type[dict])->Type[bool]:
    isOutputOK = False
    try:
        try:
            mostWord = rawOutput["MAIN_MOST_USED_WORD"]
            PrintMetaHeader("MOST USED WORDS IN THE GIVEN TEXT")
            for key,value in mostWord.items():
                print(f"--> {key} : Used {value} times")
            print("\n")
            isOutputOK = True
        except:
            pass
        try:
            stringResult = rawOutput["STRING_RESULT"]
            if (len(rawOutput["STRING_RESULT"]["IP"]) > 0) or (len(rawOutput["STRING_RESULT"]["URL"]) > 0) or (len(rawOutput["STRING_RESULT"]["EMAIL"]) > 0):
                PrintMetaHeader("IOC-LIKE INPUTS IN THE GIVEN TEXT")
                for key,value in stringResult.items():
                    if len(value) > 0:
                        print(key)
                        for val in value:
                            print(f"--> {val}")
                    else:
                        pass
                print("\n\n")
                isOutputOK = True
            else:
                isOutputOK = False
        except:
            pass
        try:
            for mK,mV in rawOutput.items():
                if (mK != "MAIN_MOST_USED_WORD") and (mK != "STRING_RESULT"):
                    print(f"[!] [ SIMILAR ACTOR FOUND :: {mK}  ] [!]")
                    for iK,iV in mV.items():
                        print(f"{iK.replace('_',' ')}: {iV}")
                    print("\n")
                else:
                    pass
            isOutputOK = True
        except:
            pass
    except:
        RETURNINITIALMESSAGE("CONTENT NOT DETECTED - CHECK FILE OR CODE SOURCE")
    return isOutputOK
        
    


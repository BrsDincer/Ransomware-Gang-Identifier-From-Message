from utils.projectConvertData import CONVERTMESSAGEDATA
from utils.projectFunctions import GETISFILE,RETURNINITIALMESSAGE
from utils.projectDesign import PrintBaseHeader,PrintSubHeader,PrintWarningMessage,PrintResults,PrintUsageExamples
from modules.sequenceCalculation import GetSequenceCalculation
from modules.distanceCalculation import GetDistanceCalculation
from modules.jaccardCalculation import GetJaccardCalculation
from argparse import RawTextHelpFormatter
import argparse,warnings,time,sys

warnings.filterwarnings(action="ignore",message="[CHECK PYTHON VERSION]")
warnings.filterwarnings(action="ignore",message="[ALREADY IMPORTED]",category=UserWarning)
warnings.filterwarnings(action="ignore",category=DeprecationWarning)
warnings.filterwarnings(action="ignore",category=FutureWarning)

parser = argparse.ArgumentParser(
    prog="RGIFM",
    description="Ransomware Gang Identifier From Message",
    formatter_class=RawTextHelpFormatter,
    add_help=True,
    exit_on_error=True,
    epilog=PrintWarningMessage()
)

parser.add_argument("path",nargs="?",help="Ransomware message file path",default=None)
parser.add_argument("-s","--sequence",required=False,action="store_true",help="Sequence-oriented similarity calculation")
parser.add_argument("-d","--distance",required=False,action="store_true",help="Distance-oriented similarity calculation")
parser.add_argument("-j","--jaccard",required=False,action="store_true",help="Jaccard-oriented similarity calculation")
parser.add_argument("-a","--all",required=False,action="store_true",help="Calculation using all modules")

args = parser.parse_args()

PrintBaseHeader()
time.sleep(1)

target = args.path

if target is not None:
    isFile = GETISFILE(target)
else:
    isFile = False

if isFile:
    try:
        readingByte = open(str(target),"rb")
        readingStabil = open(str(target),"r")
        rawByte = readingByte.read()
        raw = readingStabil.read()
        try:
            rawUTF161E = rawByte.decode("utf-16le","ignore")
        except:
            rawUTF161E = None
        isRead = True
    except:
        isRead = False
else:
    isRead = False

if isRead:
    if args.all:
        PrintSubHeader("SEQUENCE-BASED CALCULATION")
        if rawUTF161E is not None:
            result161E = GetSequenceCalculation(rawUTF161E)
        else:
            result161E = None
        result = GetSequenceCalculation(raw)
        if result is not None:
            print("\n---\nBASED ON STABIL READING\n---\n")
            isPrintOK = PrintResults(result)
            print(f"{'-'*27} [SCROLL DOWN]")
        if result161E is not None:
            print("\n---\nBASED ON STABIL FORMAT 16-1e READING\n---\n")
            isPrintOK161E = PrintResults(result161E)
            print(f"{'-'*27}")
        #
        PrintSubHeader("DISTANCE-BASED CALCULATION")
        if rawUTF161E is not None:
            result161E = GetDistanceCalculation(rawUTF161E)
        else:
            result161E = None
        result = GetDistanceCalculation(raw)
        if result is not None:
            print("\n---\nBASED ON STABIL READING\n---\n")
            isPrintOK = PrintResults(result)
            print(f"{'-'*27} [SCROLL DOWN]")
        if result161E is not None:
            print("\n---\nBASED ON STABIL FORMAT 16-1e READING\n---\n")
            isPrintOK161E = PrintResults(result161E)
            print(f"{'-'*27}")
        #
        PrintSubHeader("JACCARD-BASED CALCULATION")
        if rawUTF161E is not None:
            result161E = GetJaccardCalculation(rawUTF161E)
        else:
            result161E = None
        result = GetJaccardCalculation(raw)
        if result is not None:
            print("\n---\nBASED ON STABIL READING\n---\n")
            isPrintOK = PrintResults(result)
            print(f"{'-'*27} [SCROLL DOWN]")
        if result161E is not None:
            print("\n---\nBASED ON STABIL FORMAT 16-1e READING\n---\n")
            isPrintOK161E = PrintResults(result161E)
            print(f"{'-'*27}")
        sys.exit()
    ##
    if args.sequence:
        PrintSubHeader("SEQUENCE-BASED CALCULATION")
        if rawUTF161E is not None:
            result161E = GetSequenceCalculation(rawUTF161E)
        else:
            result161E = None
        result = GetSequenceCalculation(raw)
        if result is not None:
            print("\n---\nBASED ON STABIL READING\n---\n")
            isPrintOK = PrintResults(result)
            print(f"{'-'*27} [SCROLL DOWN]")
        if result161E is not None:
            print("\n---\nBASED ON STABIL FORMAT 16-1e READING\n---\n")
            isPrintOK161E = PrintResults(result161E)
            print(f"{'-'*27}")
    ##
    if args.distance:
        PrintSubHeader("DISTANCE-BASED CALCULATION")
        if rawUTF161E is not None:
            result161E = GetDistanceCalculation(rawUTF161E)
        else:
            result161E = None
        result = GetDistanceCalculation(raw)
        if result is not None:
            print("\n---\nBASED ON STABIL READING\n---\n")
            isPrintOK = PrintResults(result)
            print(f"{'-'*27} [SCROLL DOWN]")
        if result161E is not None:
            print("\n---\nBASED ON STABIL FORMAT 16-1e READING\n---\n")
            isPrintOK161E = PrintResults(result161E)
            print(f"{'-'*27}")
    ##
    if args.jaccard:
        PrintSubHeader("JACCARD-BASED CALCULATION")
        if rawUTF161E is not None:
            result161E = GetJaccardCalculation(rawUTF161E)
        else:
            result161E = None
        result = GetJaccardCalculation(raw)
        if result is not None:
            print("\n---\nBASED ON STABIL READING\n---\n")
            isPrintOK = PrintResults(result)
            print(f"{'-'*27} [SCROLL DOWN]")
        if result161E is not None:
            print("\n---\nBASED ON STABIL FORMAT 16-1e READING\n---\n")
            isPrintOK161E = PrintResults(result161E)
            print(f"{'-'*27}")
    ##
    try:
        readingByte.close()
    except:
        pass
    try:
        readingStabil.close()
    except:
        pass
    sys.exit()
else:
    try:
        readingByte.close()
    except:
        pass
    try:
        readingStabil.close()
    except:
        pass
    PrintUsageExamples()
    RETURNINITIALMESSAGE("TARGET MESSAGE FILE: NOT FOUND OR PATH IS INCORRECT\n")
    sys.exit()



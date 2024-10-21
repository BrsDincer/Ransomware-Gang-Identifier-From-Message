from utils.projectUtilization import I_Directory
from typing import Type
import os

class MAINDIRECTORIES:
    BASE:Type[I_Directory] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SOURCE:Type[I_Directory] = os.path.join(BASE,"sources")
    RESULT:Type[I_Directory] = os.path.join(BASE,"results")
    MESSAGESOURCE:Type[I_Directory] = os.path.join(SOURCE,"ransomware_messages.json")
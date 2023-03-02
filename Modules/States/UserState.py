"""
    사용자 관련 변수들이 저장되는 State
"""
from .State import state
import pynecone as pc

class userState(state):
    UID : str = ""
    UNAME : str = ""
    ADMIN : bool = False

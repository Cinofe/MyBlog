"""
    사용자 관련 변수들이 저장되는 State
"""
from .State import state
import pynecone as pc

class userState(state):
    UID : str = ""
    UNAME : str = ""
    ADMIN : bool = False

    def getUserInfo(self):
        print(f'userid : {self.UID}')
        print(f'ussername : {self.UNAME}')
        # return self.UID, self.UNAME

    def setUserInfo(self,id,name):
        print('1')
        self.UID = id
        self.UNAME = name
        print(f'userid : {self.UID}')
        print(f'ussername : {self.UNAME}')
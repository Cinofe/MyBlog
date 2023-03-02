"""
    drawer 구성을 위한 State 모듈
"""

from .State import state
from .UserState import userState

class drawerState(state):

    def show_drawer(self):
        if self.Auth:
            self.show_signIn = False
            if userState.ADMIN:
                self.show_admin_user = True
            else:
                self.show_user = True
        else:
            self.show_signIn = True
            self.show_user = False
            self.show_admin_user = False

    def close_signIn_drawer(self):
        self.show_signIn = False
    
    def close_user_drawer(self):
        self.show_user = False

    def close_admin_drawer(self):
        self.show_admin_user = False
    
    def close_signUp_drawer(self):
        self.show_signUp = False
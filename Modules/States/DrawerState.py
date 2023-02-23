"""
    drawer 구성을 위한 State 모듈
"""

from .State import state

class drawerState(state):

    def show_drawer(self):
        if self.Auth:
            self.show_signIn = False
            self.show_user = not (self.show_user)
        else:
            self.show_signIn = not (self.show_signIn)
            self.show_user = False

    def close_signIn_drawer(self):
        self.show_signIn = False
    
    def close_user_drawer(self):
        self.show_user = False
    
    def close_signUp_drawer(self):
        self.show_signUp = False
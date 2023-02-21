"""
    각종 State 구성을 위한 모듈
"""

import pynecone as pc

class state(pc.State):
    show_signIn: bool = False
    show_user: bool = False
    show_signUp : bool = False

    id : str
    pw : str

    Permission : bool = False

    def show_drawer(self):
        if self.Permission:
            self.show_signIn = False
            self.show_user = not (self.show_user)
        else:
            self.show_signIn = not (self.show_signIn)
            self.show_user = False
    
    def show_signUp_drawer(self):
        self.show_signIn = False
        self.show_user = False
        self.show_signUp = not (self.show_signUp)

    def close_signIn_drawer(self):
        self.show_signIn = False
    
    def close_user_drawer(self):
        self.show_user = False
    
    def close_signUp_drawer(self):
        self.show_signUp = False

    def set_id(self, id):
        self.id = id

    def set_pw(self, pw):
        self.pw = pw
    
    def show_data(self):
        print(f"id : {self.id}, pw : {self.pw}")

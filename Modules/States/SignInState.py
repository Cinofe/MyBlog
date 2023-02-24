"""
    Sign in State 구성 모듈
"""

from .State import state, Users
import pynecone as pc

class signInState(state):
    user_id : str = ""
    username : str = ""
    email : str = ""
    password : str = ""
    confirm_password : str = ""

    def signIn(self):
        with pc.session() as session:
            pass
        print(f"id : {self.user_id}, pw : {self.password}")
    
    def signUp(self):
        with pc.session() as session:
            print('signUp Clicked')
            if self.user_id == "" or self.username == "" or self.email == "" or self.password == "" or self.confirm_password == "":
                return pc.window_alert("Please fill the all empty.")

            if self.password != self.confirm_password:
                self.password = ""
                self.confirm_password = ""
                return pc.window_alert("Password do not match.")

            if session.exec(Users.select.where(Users.user_id == self.user_id)).first():
                return pc.window_alert("The ID is already exists.")

            if session.exec(Users.select.where(Users.email == self.email)).first():
                return pc.window_alert("The Email is already exists.")

            if session.exec(Users.select.where(Users.username == self.username)).first():
                return pc.window_alert("The username is already exists.")
            
            new_user = Users(user_id=self.user_id, username=self.username, email=self.email,passwd=self.password)

            session.add(new_user)
            session.commit()
            self.Auth = True

            return self.successSignUp()

    def goSignUp(self):
        self.show_signIn = False
        self.show_user = False
        self.show_signUp = True
    
    def cancelSignUp(self):
        self.show_signUp = False
        self.show_user = False
        self.show_signIn = True

    def successSignUp(self):
        self.show_signIn = False
        self.show_signUp = False
        self.show_user = False

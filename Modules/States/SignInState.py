"""
    Sign in State 구성 모듈
"""

from .State import state, Users
import pynecone as pc

class signInState(state):
    user_id : str
    username : str
    email : str
    password : str
    confirm_password : str

    def idKeyDown(self,key):
        if key == "Enter":
            return self.signIn()
        elif key == "Backspace":
            self.user_id = self.user_id[:-1]
            
    def pwKeyDown(self,key):
        if key == "Enter":
            return self.signIn()
        elif key == "Backspace":
            self.password = self.password[:-1]
            
    def signIn(self):
        with pc.session() as session:
            if self.user_id == "" or self.password == "":
                return pc.window_alert("Please fill ID or PW")
            
            user = session.exec(
                Users.select.where(Users.user_id == self.user_id)
            ).first()

            if user == None or user.passwd != self.password:
                self.user_id = ""
                self.password = ""
                return pc.window_alert("ID or PW was wrong")

            self.Auth = True
            self.admin = user.admin
            
            return self.successSign()
                
    def signUp(self):
        with pc.session() as session:
            if self.user_id == "" or self.username == "" or self.email == "" or self.password == "" or self.confirm_password == "":
                return pc.window_alert("Please fill the all empty.")
            
            if session.exec(Users.select.where(Users.user_id == self.user_id)).first():
                self.user_id = ""
                return pc.window_alert("The ID is already exists.")
            
            if session.exec(Users.select.where(Users.username == self.username)).first():
                self.username = ""
                return pc.window_alert("The username is already exists.")
            
            if session.exec(Users.select.where(Users.email == self.email)).first():
                self.email = ""
                return pc.window_alert("The Email is already exists.")
            
            if self.password != self.confirm_password:
                self.password = ""
                self.confirm_password = ""
                return pc.window_alert("Password do not match.")

            new_user = Users(user_id=self.user_id, username=self.username, email=self.email,passwd=self.password)

            session.add(new_user)
            session.commit()
            self.Auth = True

            return self.successSign()

    def goSignUp(self):
        self.show_signIn = False
        self.show_user = False
        self.show_admin_user = False
        self.show_signUp = True
    
    def cancelSignUp(self):
        self.show_signUp = False
        self.show_user = False
        self.show_admin_user = False
        self.show_signIn = True

    def successSign(self):
        self.show_signIn = False
        self.show_signUp = False
        self.show_user = False
        self.show_admin_user = False
        self.user_id = ""
        self.username = ""
        self.email = ""
        self.password = ""
        self.confirm_password = ""
        
        return pc.redirect("/")

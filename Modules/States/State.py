"""
    base State 모듈
"""

import pynecone as pc

class Users(pc.Model, table=True):
    """Users 테이블"""

    user_id : str
    username: str
    email : str
    passwd: str
    admin : bool = False

class state(pc.State):
    Auth : bool = False

    show_signIn: bool = False
    show_user: bool = False
    show_signUp : bool = False

    show_navbar : str = "fixed"

    def signOut(self):
        self.show_user = False
        self.Auth = False

        return pc.redirect('/')

    def fixNav(self):
        self.show_navbar = "fixed"

    def nonFixNav(self):
        self.show_navbar = ""
    
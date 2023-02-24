"""
    Menu 구성을 위한 모듈
"""
import pynecone as pc
from Modules.States.DrawerState import drawerState
from Modules.FrameModule.DrawerFrame import drawerFrame
from .SignInForm import signInForm

class menu():
    def __init__(self):
        self.padding = 10

    def CloseIcon(self, event):
        return pc.square(
            pc.icon(
                tag="CloseIcon",
                on_click=event,
                width='0.8em',
                height='0.8em'
            ),
            _hover={"bg": "lightgray"},
            width = '2em',
            height = '2em',
            border_radius = "3em",
        )

    def signIn_drawer(self):
        return drawerFrame.drawer(
            head = pc.drawer_header(
                pc.hstack(
                    self.CloseIcon(drawerState.close_signIn_drawer),
                    justify_content="right",
                ),
                pc.center("Sign in")
            ),
            body = pc.drawer_body(
                signInForm.signIn(),
            ),
            isOpen = drawerState.show_signIn
        )

    def signUp_drawer(self):
        return drawerFrame.drawer(
            head = pc.drawer_header(
                pc.hstack(
                    self.CloseIcon(drawerState.close_signUp_drawer),
                    justify_content="right",
                ),
                pc.center("Sign up")
            ),
            body = signInForm.signUp(),
            isOpen=drawerState.show_signUp
        )

    def User_drawer(self):
        return drawerFrame.drawer(
            head = pc.drawer_header(
                pc.hstack(
                    self.CloseIcon(drawerState.close_user_drawer),
                    justify_content = "right"
                ),
                pc.center("Signed")
            ),
            body = pc.drawer_body(
                pc.center(
                    pc.button(
                    'Sign out',
                    on_click=drawerState.signOut
                    )
                )
            ),
            isOpen=drawerState.show_user
        )
    
    ## 위 함수들은 해당 함수가 실행될 때 실행된 상태에서 state의 is open 값에 의해 실행되어야 함
    def menu(self):
        return pc.square(
            pc.center(
                pc.button(
                    pc.image(src="/person.png", width="2em"),
                    on_click=drawerState.show_drawer,
                    width = "3em",
                    height = "3em",
                    padding = 0,
                    border_radius = "3em",
                    _hover={"bg": "lightgray"}
                ),
                self.signIn_drawer(),
                self.User_drawer(),
                self.signUp_drawer(),
                padding=self.padding,
            )
        )
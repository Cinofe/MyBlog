"""
    Menu 구성을 위한 모듈
"""
import pynecone as pc
from Modules.State import state
from Modules.DrawerFrame import drawerFrame

class menu():
    def __init__(self):
        self.padding = 10

    def signIn_drawer(self):
        return drawerFrame.drawer(
            head = pc.drawer_header(
                pc.hstack(
                    pc.icon(tag="CloseIcon",on_click=state.close_signIn_drawer),
                    justify_content="right",
                ),
                pc.center("Sign in")
            ),
            body = pc.drawer_body(
                pc.vstack(
                    pc.input(placeholder="ID",
                        on_change=state.set_id,
                        width="15em",
                    ),
                    pc.input(placeholder="PW",
                        type_="password",
                        on_change=state.set_pw,
                        width="15em",
                    ),
                    pc.center(
                        pc.hstack(
                            pc.button(
                                pc.text("Sign in"),
                                on_click=state.show_data,
                                width="7em"
                            ),
                            pc.spacer(),
                            pc.button(
                                pc.text("Sign up"),
                                on_click=state.show_signUp_drawer,
                                width="7em"
                            )
                        )
                    ),
                ),
            ),
            isOpen = state.show_signIn
        )

    def User_drawer(self):
        return drawerFrame.drawer(
            head = pc.drawer_header(
                pc.hstack(
                    pc.icon(tag="CloseIcon",on_click=state.close_user_drawer),
                    justify_content = "right"
                ),
                pc.center("Signed")
            ),
            isOpen=state.show_user
        )
    
    def signUp_drawer(self):
        return drawerFrame.drawer(
            head = pc.drawer_header(
                pc.hstack(
                    pc.icon(tag="CloseIcon",on_click=state.close_signUp_drawer),
                    justify_content="right",
                ),
                pc.center("Sign up")  
            ),
            isOpen=state.show_signUp
        )
    
    ## 위 함수들은 해당 함수가 실행될 때 실행된 상태에서 state의 is open 값에 의해 실행되어야 함
    def menu(self):
        return pc.square(
            pc.center(
                pc.button(
                    pc.image(src="/person.png", width="2em"),
                    on_click=state.show_drawer,
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
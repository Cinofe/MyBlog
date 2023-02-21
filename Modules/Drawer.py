"""
    Drawer 구성을 위한 모듈
"""
import pynecone as pc
from Modules.State import state

class drawer():
    def __init__(self):
        self.padding = 10

    def signIn_drawer(self):
        return pc.drawer(
            pc.drawer_overlay(
                pc.drawer_content(
                    pc.drawer_header(
                        pc.hstack(
                            pc.icon(
                                tag="CloseIcon",
                                on_click=state.close_signIn_drawer,
                            ),
                            justify_content="right",
                        ),
                        pc.center("Sign in")
                    ),
                    pc.drawer_body(
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
                    pc.drawer_footer(),
                ),
            ),
            is_open=state.show_signIn,
        )

    def User_drawer(self):
        return pc.drawer(
            pc.drawer_overlay(
                pc.drawer_content(
                    pc.drawer_header(
                        pc.hstack(
                            pc.icon(
                                tag="CloseIcon",
                                on_click=state.close_user_drawer
                            ),
                            justify_content = "right",
                        ),
                        pc.center('Signed')
                    )
                )
            ),
            is_open = state.show_user
        )
    
    def signUp_drawer(self):
        return pc.drawer(
            pc.drawer_overlay(
                pc.drawer_content(
                    pc.drawer_header(
                        pc.hstack(
                            pc.icon(tag="CloseIcon",on_click=state.close_signUp_drawer)
                        ),
                        justify_content="right",
                    ),
                    pc.center("Sign up")
                )
            ),
            is_open = state.show_signUp
        )
    ## 위 함수들은 해당 함수가 실행될 때 실행된 상태에서 state의 is open 값에 의해 실행되어야 함
    def drawer(self):
        return pc.square(
                pc.button(
                    pc.icon(tag = "HamburgerIcon", width="1.5em",height="1.5em"),
                    on_click=state.show_drawer,
                    width = "5vw",
                    bg = "lightgray",
                ),
                self.signIn_drawer(),
                self.User_drawer(),
                self.signUp_drawer(),
                padding=self.padding,
            )
"""
    Drawer 구성을 위한 모듈
"""
import pynecone as pc
from Modules.State import drawerState

class drawer():
    def __init__(self):
        self.padding = 10

    def drawer(self):
        return pc.square(
                pc.button(
                    pc.icon(tag = "HamburgerIcon", width="1.5em",height="1.5em"),
                    on_click=drawerState.right,
                    width = "5em",
                ),
                pc.drawer(
                    pc.drawer_overlay(
                        pc.drawer_content(
                            pc.drawer_header("Confirm"),
                            pc.drawer_body(
                                "Do you want to confirm example?"
                            ),
                            pc.drawer_footer(),
                            on_click = drawerState.close,
                        ),
                    ),
                    is_open=drawerState.show_right,
                ),
                padding=self.padding,
            )
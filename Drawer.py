import pynecone as pc
from DrawerState import drawerState

class drawer():
    def __init__(self):
        self.padding = 10

    def drawer(self):
        return pc.square(
                pc.button(
                    "Show Right Drawer", on_click=drawerState.right
                ),
                pc.drawer(
                    pc.drawer_overlay(
                        pc.drawer_content(
                            pc.drawer_header("Confirm"),
                            pc.drawer_body(
                                "Do you want to confirm example?"
                            ),
                            pc.drawer_footer()
                        )
                    ),
                    is_open=drawerState.show_right,
                    on_overlay_click=drawerState.close
                ),
                padding=self.padding,
            )
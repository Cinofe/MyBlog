import pynecone as pc


class State(pc.State):
    """The app state."""

    pass

class DrawerState(pc.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)
    
    def close(self):
        self.show_right = False

def drawer():
    return 

def index():
    return pc.vstack(
        pc.box(
            pc.text("1"),
        ),
        pc.box(
            pc.text("2"),
        ),
        pc.box(
            pc.text("3"),
        ),
        pc.box(
            pc.button(
                "Show Right Drawer", on_click=DrawerState.right
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
                is_open=DrawerState.show_right,
                on_overlay_click=DrawerState.close
            ),
        )
    )
    


# Add state and page to the app.
app = pc.App(state=DrawerState)
app.add_page(index)
app.compile()
import pynecone as pc
from Modules.Banner import banner
from Modules.DrawerState import drawerState

class MyBlog():
    def __init__(self):
        self.Ban = banner()
        self.width = 100
        self.height = 100

    def index(self):
        return pc.vstack(
            self.Ban.banner(),
            pc.center(
                pc.text("1"),
            ),
            pc.center(
                pc.text("2"),
            ),
            pc.center(
                pc.text("3"),
            ),
            width = str(self.width) + "%",
            height = str(self.height - self.Ban.height) + 'vh',
        )
        
# Add state and page to the app.
app = pc.App(state=drawerState)
app.add_page(MyBlog().index)
app.compile()
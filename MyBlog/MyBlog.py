import pynecone as pc
from Modules.Banner import banner
from Modules.State import drawerState
from Modules.Body import body
from Modules.Fotter import fotter


class MyBlog():
    def __init__(self):
        self.Ban = banner()
        self.body = body()
        self.fotter = fotter()
        self.width = 100
        self.height = 100

    def index(self):
        return pc.vstack(
            self.Ban.banner(),
            self.body.body(),
            self.fotter.footer(),
            width = str(self.width) + "%",
        )
        
# Add state and page to the app.
app = pc.App(state=drawerState)
app.add_page(MyBlog().index)
app.compile()
import pynecone as pc
from Modules.Head import head
from Modules.State import drawerState
from Modules.Body import body
from Modules.Fotter import fotter

class MyBlog():
    def __init__(self):
        self.width = 100
        self.height = 100

    def index(self):
        return pc.vstack(
            head().head(),
            body().body(),
            fotter().footer(),
            width = str(self.width) + "%",
        )
        
# Add state and page to the app.
app = pc.App(state=drawerState)
app.add_page(MyBlog().index)
app.compile()
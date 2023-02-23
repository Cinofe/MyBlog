from Modules.States.State import state
from Modules.MainModule.Head import head
from Modules.MainModule.Body import body
from Modules.MainModule.Footer import footer
import pynecone as pc

class MyBlog():
    def __init__(self):
        self.width = 100
        self.height = 100

    def index(self):
        return pc.vstack(
            head().head(),
            body().body(),
            footer().footer(),
            width = str(self.width) + "%",
        )
        
# Add state and page to the app.
app = pc.App(state=state)
app.add_page(MyBlog().index)
app.compile()
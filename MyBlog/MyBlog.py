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
            ## 모달 창을 띄워서 포스트 작성
            
            width = str(self.width) + "%",
        )
        
# Add state and page to the app.
app = pc.App(state=state)
app.add_page(MyBlog().index)
app.compile()
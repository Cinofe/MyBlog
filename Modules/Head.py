"""
    Banner 구성을 위한 모듈
"""
from Modules.Drawer import drawer
import pynecone as pc

class head:
    def __init__(self):
        self.height = 15    
        self.width = 100
    
    def head(self):
        return pc.flex(
            pc.square(
                pc.image(src="/logo.png", width="5em"),
                padding=10,
            ),
            pc.spacer(),
            pc.square(
                pc.heading("My Blog"),
                padding=10,
            ),
            pc.spacer(),
            drawer().drawer(),
            width = str(self.width) + "%",
            height = str(self.height) + "vh",
        )
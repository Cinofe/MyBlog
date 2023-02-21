"""
    Banner 구성을 위한 모듈
"""
from Modules.Menu import menu
import pynecone as pc

class head:
    def __init__(self):
        self.height = 15    
        self.width = 100
    
    def head(self):
        return pc.flex(
            pc.square(
                pc.center(
                    pc.image(src="/logo.png", width="5em"),
                    padding=10,
                )
            ),
            pc.spacer(),
            pc.square(
                pc.center(
                    pc.heading("My Blog"),
                    padding=10,
                )
            ),
            pc.spacer(),
            menu().menu(),
            width = str(self.width) + "%",
            height = str(self.height) + "vh",
        )
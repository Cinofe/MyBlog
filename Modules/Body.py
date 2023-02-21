"""
    Body 구성을 위한 모듈
"""
import pynecone as pc
from Modules.Head import head
from Modules.Fotter import fotter

class body:
    def __init__(self):
        self.width = 75
        self.height = 100
    
    def chooseWidth(self):
        return

    def body(self):
        return pc.square(
            pc.center(
                pc.text("Body Area"),
                width = str(self.width) + "%",
                height = str(self.height + head().height + fotter().height) + "vh",
                bg = "yellow",
                padding = 10,
            )
        ),
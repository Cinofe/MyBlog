"""
    Body 구성을 위한 모듈
"""
import pynecone as pc
from Modules.States.State import state
from .Head import head
from .Footer import footer

class body:
    def __init__(self):
        self.width = 75
        self.height = 100

    def body(self):
        return pc.square(
            pc.center(
                pc.text("Body Area"),
                width = str(self.width)+"vw",
                height = str(self.height + head().height + footer().height) + "vh",
                bg = "yellow",
                padding = 10,
            )
        )
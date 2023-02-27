"""
    Banner 구성을 위한 모듈
"""
from Modules.States.State import state
from Modules.FrameModule.Menu import menu
import pynecone as pc

def Banner():
    return pc.box(
        pc.hstack(
            pc.hstack(
                pc.image(src="/logo.png", width="75px"),
                pc.heading("My Blog", size="lg"),
                pc.flex(
                    pc.badge("2022-2023 Season", color_scheme="blue"),
                ),
            ),
            menu().menu(),
            justify="space-between",
            border_bottom="0.2em solid #F0F0F0",
            padding_x="2em",
            bg="rgba(255,255,255, 0.75)",
        ),
        position=state.show_navbar,
        width="100%",
        top="0px",
    )

class head:
    def __init__(self):
        self.height = 15    
        self.width = 100
    
    def head(self):
        return pc.flex(
            Banner(),
            pc.spacer(),
            width = str(self.width) + "%",
            height = str(self.height) + "vh",
        )
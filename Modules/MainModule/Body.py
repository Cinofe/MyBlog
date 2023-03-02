"""
    Body 구성을 위한 모듈
"""
import pynecone as pc
from .Head import head
from .Footer import footer
from Modules.States.PostState import postState

class body:
    def __init__(self):
        self.width = 65
        self.height = 100
    
    def postingModal(self):
        return pc.box(
            pc.modal(
                pc.modal_overlay(
                    pc.modal_content(
                        pc.modal_header("Posting"),
                        pc.modal_body(
                            pc.vstack(
                                pc.hstack(),
                                pc.text_area(
                                    value=postState.post_text,
                                    on_change=postState.setText,
                                    height = "30vw"
                                )
                            )
                        ),
                        pc.modal_footer(
                            pc.button(
                                "Close", on_click=postState.closeModal
                            )
                        )
                    )
                ),
                is_open=postState.show_modal,
                size = "5xl"
            )
        )

    def body(self):
        return pc.square(
            pc.center(
                pc.text("Body Area"),
                width = str(self.width)+"vw",
                height = str(self.height + head().height + footer().height) + "vh",
                bg = "yellow",
                padding = 10,
            ),
            self.postingModal()
        )
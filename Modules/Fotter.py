"""
    Fotter 구성을 위한 모듈
"""

import pynecone as pc

class fotter:
    def __init__(self):
        self.width = 100
        self.height = 20
    
    def footer(self):
        return pc.square(
            pc.center(
                pc.text("Footer Area"),
            ),
            width = str(self.width) + "%",
            height = str(self.height) + "vh",
        )

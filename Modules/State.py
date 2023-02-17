"""
    각종 State 구성을 위한 모듈
"""

import pynecone as pc

class drawerState(pc.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
            self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)
    
    def close(self):
        self.show_right = False
import pynecone as pc
from Drawer import drawer

class banner():
    def __init__(self):
        self.height = 15    
        self.width = 100
        self.Dw = drawer()
    
    def banner(self):
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
            self.Dw.drawer(),
            width = str(self.width) + "%",
            height = str(self.height) + "vh",
        )
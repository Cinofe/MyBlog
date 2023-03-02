
from .State import state
import pynecone as pc

class postState(state):
    def posting(self):
        return pc.window_alert("Post Clicked")
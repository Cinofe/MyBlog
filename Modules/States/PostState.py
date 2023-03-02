
from .State import state

class postState(state):
    show_modal : bool = False
    post_text : str

    def posting(self):
        self.show_admin_user = False
        self.show_modal = True
    
    def closeModal(self):
        self.show_modal = False

    def setText(self,text):
        self.post_text = text
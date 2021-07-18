from .image import Image
from .input import Input
from .flash import Flash

class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()
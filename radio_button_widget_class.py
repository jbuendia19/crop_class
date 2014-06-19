from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """This class create a group of radio buttons from a given list of labels"""

    def __init__(self, label, instruction, button_list):
        super().__init__()
        

from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .QXFrame import QXFrame
from .QXVBoxLayout import QXVBoxLayout

class QXFrameVBox(QXFrame):
    def __init__(self, widgets=None, contents_margins=0, spacing=0, **kwargs):
        super().__init__(layout=QXVBoxLayout(widgets=widgets, contents_margins=contents_margins, spacing=spacing), **kwargs)

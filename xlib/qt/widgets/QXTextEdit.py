from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ._part_QXWidget import _part_QXWidget


class QXTextEdit(QTextEdit, _part_QXWidget):
    def __init__(self, placeholder_text=None,
                       style_sheet=None,
                       read_only=False,
                       **kwargs):
        super().__init__()
        _part_QXWidget.__init__(self, **kwargs)
        #_part_QXWidget.connect_signal(editingFinished, self.editingFinished)

        if placeholder_text is not None:
            self.setPlaceholderText(placeholder_text)
        if style_sheet is not None:
            self.setStyleSheet(style_sheet)
        if read_only:
            self.setReadOnly(True)

    def focusInEvent(self, ev : QFocusEvent):
        super().focusInEvent(ev)
        _part_QXWidget.focusInEvent(self, ev)

    def resizeEvent(self, ev : QResizeEvent):
        super().resizeEvent(ev)
        _part_QXWidget.resizeEvent(self, ev)

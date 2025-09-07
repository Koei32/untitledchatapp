from PySide6.QtGui import QFont, QPalette, QColor


warning_font = QFont("Trebuchet MS", pointSize=10, weight=900)

default_font = QFont("Tahoma", pointSize=8)

warning_font.setStyleStrategy(QFont.StyleStrategy.NoAntialias)
default_font.setStyleStrategy(QFont.StyleStrategy.NoSubpixelAntialias)

def main_pallete():
    pal = QPalette()
    # Core greys
    pal.setColor(QPalette.ColorRole.Window, QColor(240, 240, 240))       # Main window background
    pal.setColor(QPalette.ColorRole.Button, QColor(240, 240, 240))       # Button face
    pal.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))         # Text entry background
    pal.setColor(QPalette.ColorRole.AlternateBase, QColor(192, 192, 192))
    pal.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))               # Normal text
    pal.setColor(QPalette.ColorRole.ButtonText, QColor(0, 0, 0))         # Button text
    
    # 3D effect shades
    pal.setColor(QPalette.ColorRole.Light, QColor(244, 244, 244))        # Top/left highlight
    pal.setColor(QPalette.ColorRole.Midlight, QColor(232, 232, 232))     # Mid highlight
    pal.setColor(QPalette.ColorRole.Mid, QColor(168, 168, 168))          # Middle shadow
    pal.setColor(QPalette.ColorRole.Dark, QColor(177, 177, 177))         # Deep shadow
    pal.setColor(QPalette.ColorRole.Shadow, QColor(118, 118, 118))             # Outlines

    # Selection
    pal.setColor(QPalette.ColorRole.Highlight, QColor(0, 0, 128))        # Dark blue highlight
    pal.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))

    # Tooltips / text variations
    pal.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
    pal.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))

    return pal



from PyQt5.QtGui import QPixmap, QPainter
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class CustomWebEngineView(QWebEngineView):
    def __init__(self, parent=None):
        super(CustomWebEngineView, self).__init__(parent)
        self.new_windows = []

    def createWindow(self, _type):
        new_webview = CustomWebEngineView()
        new_window = QMainWindow()
        new_window.setCentralWidget(new_webview)

        # Set new window to full screen
        new_window.showFullScreen()

        self.new_windows.append(new_window)  # Keep a reference to the new window
        return new_webview

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("RF DRISHTI")  # Set window title

        # Set up the browser
        self.browser = CustomWebEngineView()
        self.browser.setUrl(QUrl('https://access.dwservice.net/login.dw#s'))
        self.setCentralWidget(self.browser)

        # Show in full screen
        self.showFullScreen()

        # Navigation toolbar
        navbar = QToolBar()

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        # navbar.addWidget(self.url_bar)

        # Connect URL change signal to update URL bar
        self.browser.urlChanged.connect(self.update_url)

        # Add logo
        self.add_logo()

    def add_logo(self):
        logo_label = QLabel(self)
        logo_label2 = QLabel(self)
        pixmap = QPixmap('logo3.png')  # Replace 'path_to_your_logo' with the actual path to your logo image
        logo_label.setPixmap(pixmap)
        # logo_label.setFixedSize(300, 300)
        logo_label.setGeometry(0, 1010, pixmap.width(), pixmap.height())
        logo_label.show()
        logo_label2.setPixmap(pixmap)
        # logo_label2.setFixedSize(300, 300)
        logo_label2.setGeometry(1730, 1010, pixmap.width(), pixmap.height())
        logo_label2.show()

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('RF DRISHTI')
window = MainWindow()
app.exec_()

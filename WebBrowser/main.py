from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWebEngineWidgets import * 

'''
Functions for the GUI
'''
class MyWebBrowser():
    def __init__(self):
        
        self.window = QWidget()
        self.window.setWindowTitle("Web Browser")
        
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        
        # Component for the URL Bar
        self.urlBar = QTextEdit()
        self.urlBar.setMaximumHeight(30)
        
        # Component for executing go
        self.goButton = QPushButton("Go")
        self.goButton.setMinimumHeight(30)
        
        # Component for executing forward
        self.forwardButton = QPushButton("<")
        self.forwardButton.setMinimumHeight(30)
        
        # Component for executing back
        self.backButton = QPushButton(">")
        self.backButton.setMinimumHeight(30)
        
        # Adding all the components to the horizontal bar
        self.horizontal.addWidget(self.urlBar)
        self.horizontal.addWidget(self.goButton)
        self.horizontal.addWidget(self.forwardButton)
        self.horizontal.addWidget(self.backButton)
        
        # Creating the window for the browser
        self.browser = QWebEngineView()
        
        # Mapping the go, forward and backward buttons to their related functions
        self.goButton.clicked.connect(lambda: self.navigate(self.urlBar.toPlainText()))
        self.forwardButton.clicked.connect(self.browser.back)
        self.goButton.clicked.connect(self.browser.forward)
        
        
        # Adding the browser window to the normal layout
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        # Set a starting link for the broswer to boot up into
        self.browser.setUrl(QUrl("https://google.com"))
        
        # Setting up the window
        self.window.setLayout(self.layout)
        self.window.show()
        
    def navigate(self, url):
        if url.startswith('http'):
            self.urlBar.setText(url)
            self.browser.setUrl(QUrl(url))
        else: 
            url = "http:" + url
            self.urlBar.setText(url)
            self.browser.setUrl(QUrl(url))
        
'''
Functions for the actual operation of the web Browser
''' 
app = QApplication([])
window = MyWebBrowser()
app.exec_()    
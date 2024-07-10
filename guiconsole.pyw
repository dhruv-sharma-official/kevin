import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTabWidget, QWidget, QShortcut, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl
import subprocess
import dns.resolver
import asyncio
import aiodns
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtWidgets import QComboBox
# import uvloop


zoom=1.5
# if sys.platform == 'win32':
#     asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.initUI()
        self.tabcount = 0
        
     ## ===================================UI management=======================================
    def initUI(self):
        self.tabs = QTabWidget()
        self.url_input = QLineEdit()          ## search bar
        self.go_button = QPushButton('Go')
        self.new_tab_button = QPushButton('New Tab')
        self.close_tab_button = QPushButton('Close Tab')
        self.reload_button = QPushButton('Reload')
        self.back_button = QPushButton('Back')
        self.ctrl = QPushButton('Control')
        self.serverbtn = QPushButton('Server')
        self.connectindicator = QLabel('Search Status: Public')

        self.go_button.clicked.connect(self.loadURL)
        self.new_tab_button.clicked.connect(self.addNewTab)
        self.close_tab_button.clicked.connect(self.closeCurrentTab)
        self.reload_button.clicked.connect(self.reloadPage)
        self.back_button.clicked.connect(self.goBack)
        self.ctrl.clicked.connect(self.ctrlpnl)
        self.serverbtn.clicked.connect(self.servercd)
        

        address_bar_layout = QHBoxLayout()
        address_bar_layout.addWidget(self.go_button)
        address_bar_layout.addWidget(self.new_tab_button)
        address_bar_layout.addWidget(self.close_tab_button)
        address_bar_layout.addWidget(self.reload_button)
        address_bar_layout.addWidget(self.back_button)
        address_bar_layout.addWidget(self.url_input)        ## search bar
        address_bar_layout.addWidget(self.ctrl)
        address_bar_layout.addWidget(self.serverbtn)
        
        
        


        ## layout management here  =========================================================
        layout = QVBoxLayout()
        layout.addLayout(address_bar_layout)
        layout.addWidget(self.connectindicator)              ### light indicator 
        layout.addWidget(self.tabs)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setGeometry(100, 100, 1800, 1200)
        
        self.addNewTab()
        
        ## shortcuts from here =========================================================
        new_tab_shortcut = QShortcut(Qt.CTRL + Qt.Key_T, self)
        new_tab_shortcut.activated.connect(self.addNewTab)

        close_tab_shortcut = QShortcut(Qt.CTRL + Qt.Key_W, self)
        close_tab_shortcut.activated.connect(self.closeCurrentTab)
        
        servercon_shortcut = QShortcut(Qt.CTRL + Qt.Key_C, self)
        servercon_shortcut.activated.connect(self.servercd)
        
        enter_shortcut = QShortcut(Qt.Key_Enter,self)
        enter_shortcut.activated.connect(self.loadURL)
        
        return_shortcut_shortcut = QShortcut(Qt.Key_Return,self)
        return_shortcut_shortcut.activated.connect(self.loadURL)
        
        reload_shortcut = QShortcut(Qt.CTRL + Qt.Key_R, self)
        reload_shortcut.activated.connect(self.reloadPage)
        
        back_shortcut = QShortcut(Qt.AltModifier + Qt.LeftArrow, self)
        back_shortcut.activated.connect(self.goBack)
        
        forward_shortcut = QShortcut(Qt.AltModifier + Qt.RightArrow, self)
        forward_shortcut.activated.connect(self.goForward)
        
        control_shortcut = QShortcut(Qt.AltModifier + Qt.Key_H, self)
        control_shortcut.activated.connect(self.ctrlpnl)
        
        self.dark_mode_button = QPushButton('Dark Mode')
        self.dark_mode_button.clicked.connect(self.toggleDarkMode)  # Connect the button click event

        # Add the dark mode button to the address bar layout
        address_bar_layout.addWidget(self.dark_mode_button)

        # dropdown box
        self.dropdown = QComboBox()
        self.dropdown.addItem("Google")
        self.dropdown.addItem("DuckDuckGo")
        self.dropdown.addItem("Bing")
        self.dropdown.currentIndexChanged.connect(self.handleDropdownSelection)
        
        # Add the dropdown box to the address bar layout
        address_bar_layout.addWidget(self.dropdown)


    def handleDropdownSelection(self):
        # Get the selected option from the dropdown
        selected_option = self.dropdown.currentText()

        if selected_option == "Google":
            print("Option 1 selected")
        elif selected_option == "DuckDuckGo":
            print("Option 2 selected")
        elif selected_option == "Bing":
            print("Option 3 selected")

    def toggleDarkMode(self):
        self.dark_mode = not self.dark_mode  # dark mode status

        if self.dark_mode:
            self.setStyleSheet("background-color: #333; color: #FFF;")  # Dark theme
            
        else:
            self.setStyleSheet("")  # light theme
        
        
    def loadURL(self):
        url = self.url_input.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        if not '.com' in url:
            url = url + '.com'
        if 'youtube.com' in url:
            
            self.tabs.currentWidget().settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.tabs.currentWidget().setUrl(QUrl(url))
        self.tabs.currentWidget().setZoomFactor(zoom)

        

    def addNewTab(self):
        web_view = QWebEngineView()
        web_view.load(QUrl('http://duckduckgo.com'))  # Default page
        self.tabs.addTab(web_view, 'Tab')
        self.tabs.setCurrentWidget(web_view)
        self.tabs.currentWidget().setZoomFactor(zoom)
        

    def closeCurrentTab(self):
        if self.tabs.count() > 1:
            current_index = self.tabs.currentIndex()
            self.tabs.removeTab(current_index)
        else:
            print("operations ended")
            exit()

    def reloadPage(self):
        self.tabs.currentWidget().reload()
        self.tabs.currentWidget().setZoomFactor(zoom)
        

    def goBack(self):
        self.tabs.currentWidget().back()
        self.tabs.currentWidget().setZoomFactor(zoom)
        
    def goForward(self):
        
        current_web_view = self.tabs.currentWidget()
        if current_web_view and current_web_view.history().canGoForward():
            current_web_view.forward()
        
    def ctrlpnl(self):
        self.tabs.currentWidget().setUrl(QUrl('http://localhost:5000'))
        self.tabs.currentWidget().setZoomFactor(zoom)
        
    def setZoomFactor(self, factor):
        current_web_view = self.tabs.currentWidget()
        if current_web_view:
            current_web_view.setZoomFactor(factor)
        
    def start_warp(self):
        try:
            subprocess.run(["warp-cli", "connect"],check=True)
            print("WARP Connected!")
        except subprocess.CalledProcessError as e:
            print("Error occurred:", e)

    def stop_warp(self):
        try:
            subprocess.run(["warp-cli", "disconnect"], check=True)
            print("WARP Disconnected!")
        except subprocess.CalledProcessError as e:
            print("Error occurred:", e)

## ================================= functions ends here ======================================


if __name__ == '__main__':
    try:
        
        app = QApplication(sys.argv)
        browser = WebBrowser()
        browser.show()
        browser.stop_warp()
        sys.exit(app.exec_())
    except KeyboardInterrupt as e:
        print("browser off")



# import time

# start = time.time()
# for i in range(1,101):
#     print(i)
    
# print(time.time()-start)
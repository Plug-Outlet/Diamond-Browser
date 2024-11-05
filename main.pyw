import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets, uic, QtWebEngineWidgets
import os
from selenium import webdriver
import PyQt5.QtWebEngineWidgets
from PyQt5.QtWidgets import QMessageBox, QMenu, QDialog, QVBoxLayout, QLabel
import requests
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from urllib.parse import urlparse  # Add this import statement at the beginning of your script
from PyQt5.QtWebEngineWidgets import QWebEngineView  # Import QWebEngineView
from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QVBoxLayout  # Import necessary classes for subwindow
from view_boosting_handlers import ViewBoostingHandlers  # Import your handler module

capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['acceptInsecureCerts'] = True


os.environ['QT_LOGGING_RULES'] = 'qt.*=False'




class SubWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SubWindow, self).__init__()
        self.setWindowTitle("Sub Window")
        layout = QVBoxLayout()
        label = QLabel("This is a subwindow")
        layout.addWidget(label)
        self.setLayout(layout)






class ConsoleOutput:
    def __init__(self, console_widget):
        self.console_widget = console_widget

    def write(self, text):
        self.console_widget.insertPlainText(text)

    def flush(self):
        pass  # Implement the flush method if necessary

class UserAgentSpoofingDialog(QtWidgets.QDialog):
    def __init__(self):
        super(UserAgentSpoofingDialog, self).__init__()
        self.setWindowTitle("User-Agent Spoofing")
        self.setFixedSize(300, 500)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(5, 234, 255);
                color: #fff;
            }
        """)
        layout = QtWidgets.QVBoxLayout(self)
        self.result_label = QtWidgets.QLabel("")
        layout.addWidget(self.result_label)
        self.console_widget_textedit = QtWidgets.QTextEdit()
        layout.addWidget(self.console_widget_textedit)
        sys.stdout = ConsoleOutput(self.console_widget_textedit)

        label = QtWidgets.QLabel("Select User-Agent:")
        layout.addWidget(label)

        # Add QComboBox for user selection
        combo_box = QtWidgets.QComboBox()
        combo_box.addItem("Desktop", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Gecko/58.0.3029.110 Safari/537.3")
        combo_box.addItem("Laptop", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Gecko/91.0.4472.124 Safari/537.36")
        combo_box.addItem("Tablet", "Mozilla/5.0 (iPad; CPU OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1")
        combo_box.addItem("Android", "Mozilla/5.0 (Linux; Android 11; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Gecko/91.0.4472.120 Mobile Safari/537.36")
        combo_box.addItem("iPhone", "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1")
        combo_box.addItem("Linux", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0")
        combo_box.addItem("Custom")
        combo_box.currentTextChanged.connect(self.handle_combo_box_change)
        layout.addWidget(combo_box)

        # Add QLineEdit for custom User-Agent input
        self.custom_line_edit = QtWidgets.QLineEdit()
        self.custom_line_edit.setVisible(False)
        layout.addWidget(self.custom_line_edit)

        # Add QPushButton for spoofing
        button = QtWidgets.QPushButton("Spoof User-Agent")
        # Add QPushButton for spoofing
        button = QtWidgets.QPushButton("Spoof User-Agent")
        button.clicked.connect(self.spoof_user_agent)
        layout.addWidget(button)

    def handle_combo_box_change(self, text):
        # Show or hide the custom line edit based on the selected option
        self.custom_line_edit.setVisible(text == "Custom")

    def spoof_user_agent(self):
        # Function to handle the "Spoof User-Agent" button click
        combo_box = self.findChild(QtWidgets.QComboBox)
        selected_user_agent = combo_box.currentData()
        if combo_box.currentText() == "Custom":
            selected_user_agent = self.custom_line_edit.text()
        spoofed = self.perform_user_agent_spoofing(selected_user_agent)
        if spoofed:
            self.result_label.setText("User-Agent successfully spoofed!")
        else:
            self.result_label.setText("Failed to spoof User-Agent.")




class ProxySettingsDialog(QtWidgets.QDialog):
    def __init__(self):
        super(ProxySettingsDialog, self).__init__()
        self.setWindowTitle("Proxy Settings")
        self.setFixedSize(200, 500)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(5, 234, 255);
                color: #fff;
            }
        """)
        layout = QtWidgets.QVBoxLayout(self)
        # Add widgets and layouts to the dialog
        # ...

class UserAgentSpoofingDialog(QtWidgets.QDialog):
    def __init__(self):
        super(UserAgentSpoofingDialog, self).__init__()
        self.setWindowTitle("User-Agent Spoofing")
        self.setFixedSize(300, 500)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(5, 234, 255);
                color: #fff;
            }
        """)
        layout = QtWidgets.QVBoxLayout(self)
        self.result_label = QtWidgets.QLabel("")
        layout.addWidget(self.result_label)
        self.console_widget_textedit = QtWidgets.QTextEdit()
        layout.addWidget(self.console_widget_textedit)
        sys.stdout = ConsoleOutput(self.console_widget_textedit)

        label = QtWidgets.QLabel("Select User-Agent:")
        layout.addWidget(label)

        # Add QComboBox for user selection
        combo_box = QtWidgets.QComboBox()
        combo_box.addItem("Desktop", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Gecko/58.0.3029.110 Safari/537.3")
        combo_box.addItem("Laptop", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Gecko/91.0.4472.124 Safari/537.36")
        combo_box.addItem("Tablet", "Mozilla/5.0 (iPad; CPU OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1")
        combo_box.addItem("Android", "Mozilla/5.0 (Linux; Android 11; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Gecko/91.0.4472.120 Mobile Safari/537.36")
        combo_box.addItem("iPhone", "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1")
        combo_box.addItem("Linux", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0")
        combo_box.addItem("Custom")
        combo_box.currentTextChanged.connect(self.handle_combo_box_change)
        layout.addWidget(combo_box)

        # Add QLineEdit for custom User-Agent input
        self.custom_line_edit = QtWidgets.QLineEdit()
        self.custom_line_edit.setVisible(False)
        layout.addWidget(self.custom_line_edit)

        # Add QPushButton for spoofing
        button = QtWidgets.QPushButton("Spoof User-Agent")
        button.clicked.connect(self.spoof_user_agent)
        layout.addWidget(button)


    def handle_combo_box_change(self, text):
        # Show or hide the custom line edit based on the selected option
        self.custom_line_edit.setVisible(text == "Custom")

    def spoof_user_agent(self):
        # Function to handle the "Spoof User-Agent" button click
        combo_box = self.findChild(QtWidgets.QComboBox)
        selected_user_agent = combo_box.currentData()
        if combo_box.currentText() == "Custom":
            selected_user_agent = self.custom_line_edit.text()
        spoofed = self.perform_user_agent_spoofing(selected_user_agent)
        if spoofed:
            self.result_label.setText("User-Agent successfully spoofed!")
        else:
            self.result_label.setText("Failed to spoof User-Agent.")

    def perform_user_agent_spoofing(self, user_agent):
        url = "https://www.f.vision/"  # Replace with the URL you want to test

        # Set up Firefox options
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Run Firefox in headless mode
        firefox_options.add_argument("--disable-dev-shm-usage")

        # Set the desired capabilities
        capabilities = DesiredCapabilities.FIREFOX.copy()
        capabilities['acceptInsecureCerts'] = True

        # Get the path to the GeckoDriver executable
        script_dir = os.path.dirname(os.path.abspath(__file__))
        geckodriver_path = os.path.join(script_dir, "geckodriver.exe")

        # Start the WebDriver service
        service = Service(geckodriver_path)

        # Start the Firefox WebDriver
        driver = webdriver.Firefox(service=service, options=firefox_options, capabilities=capabilities)

        try:
            driver.get(url)
            driver.execute_script(f"navigator.userAgent = '{user_agent}'")  # Set the user agent using JavaScript

            # Wait for the page to load
            time.sleep(2)

            # Get the page source
            page_source = driver.page_source

            # Parse the HTML response
            soup = BeautifulSoup(page_source, "html.parser")

            # Extract and display the desired values
            # You can customize this part based on your requirements
            general_section = soup.find("div", class_="general")
            basic_section = soup.find("div", class_="basic")
            hashes_section = soup.find("div", class_="hashes")

            if general_section:
                ip4 = general_section.find("div", text="IP4").find_next_sibling("div").text.strip()
                webrtc_ip = general_section.find("div", text="WEBRTC").find_next_sibling("div").text.strip()
                user_agent_version = general_section.find("div", text="USERAGENT").find_next_sibling("div").text.strip()
                platform = general_section.find("div", text="PLATFORM").find_next_sibling("div").text.strip()
                print("GENERAL:")
                print(f"IP4: {ip4}")
                print(f"WEBRTC IP: {webrtc_ip}")
                print(f"USERAGENT VERSION: {user_agent_version}")
                print(f"PLATFORM: {platform}")
                print()

            if basic_section:
                browser_percentage = basic_section.find("div", text="BROWSER").find_next_sibling("div").text.strip()
                ip_percentage = basic_section.find("div", text="IP").find_next_sibling("div").text.strip()
                timezone = basic_section.find("div", text="TIMEZONE").find_next_sibling("div").text.strip()
                language = basic_section.find("div", text="LANGUAGE").find_next_sibling("div").text.strip()
                print("BASIC:")
                print(f"BROWSER PERCENTAGE: {browser_percentage}")
                print(f"IP PERCENTAGE: {ip_percentage}")
                print(f"TIMEZONE: {timezone}")
                print(f"LANGUAGE: {language}")

                print()
            if hashes_section:
                hst_hash = hashes_section.find("div", text="HST").find_next_sibling("div").text.strip()
                webgl_hash = hashes_section.find("div", text="WEBGL").find_next_sibling("div").text.strip()
                canvas_hash = hashes_section.find("div", text="CANVAS").find_next_sibling("div").text.strip()
                plugins_hash = hashes_section.find("div", text="PLUGINS").find_next_sibling("div").text.strip()
                audio_hash = hashes_section.find("div", text="AUDIO").find_next_sibling("div").text.strip()
                client_rects_hash = hashes_section.find("div", text="CLIENT RECTS").find_next_sibling("div").text.strip()
                fonts_hash = hashes_section.find("div", text="FONTS").find_next_sibling("div").text.strip()
                print("HASHES:")
                print(f"HST HASH: {hst_hash}")
                print(f"WEBGL HASH: {webgl_hash}")
                print(f"CANVAS HASH: {canvas_hash}")
                print(f"PLUGINS HASH: {plugins_hash}")
                print(f"AUDIO HASH: {audio_hash}")
                print(f"CLIENT RECTS HASH: {client_rects_hash}")
                print(f"FONTS HASH: {fonts_hash}")
                print()
            
            return True
        except Exception as e:
            print("An error occurred:", e)
            return False
        finally:
            driver.quit()

        # Create the UserAgentSpoofingDialog instance and execute it
        dialog = UserAgentSpoofingDialog()
        dialog.exec_()


class RequestThrottlingDialog(QtWidgets.QDialog):
    def __init__(self):
        super(RequestThrottlingDialog, self).__init__()
        self.setWindowTitle("Request Throttling")
        self.setFixedSize(200, 400)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(5, 234, 255);
                color: #fff;
            }
        """)
        layout = QtWidgets.QVBoxLayout(self)
        # Add widgets and layouts to the dialog
        # ...


class AuthenticationMethodsDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AuthenticationMethodsDialog, self).__init__()
        self.setWindowTitle("Authentication Methods")
        self.setFixedSize(500, 300)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(5, 234, 255);
                color: #fff;
            }
        """)
        layout = QtWidgets.QVBoxLayout(self)
        # Add widgets and layouts to the dialog
        # ...




class NullStream:
    def write(self, data):
        pass

# Replace sys.stdout and sys.stderr with custom stream objects
sys.stdout = NullStream()
sys.stderr = NullStream()

# Rest of your code goes here

# Restore sys.stdout and sys.stderr (optional)
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

class ElementInspector(QtWidgets.QMainWindow):
    def __init__(self, url):
        super(ElementInspector, self).__init__()
        # Add context menu
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        self.context_menu = QtWidgets.QMenu(self)
        self.inspect_action = self.context_menu.addAction("Inspect Element")
        self.inspect_action.triggered.connect(self.inspect_element)
        self.copy_id_action = self.context_menu.addAction("Copy Element ID")
        self.copy_id_action.triggered.connect(self.copy_element_id)

    def show_context_menu(self, pos):
        # Get the element at the mouse position
        element = self.webview.page().currentFrame().hitTestContent(pos).element()
    
        if element:
            element_id = element.attribute("id")
            self.console_widget.insertPlainText(f"Element ID: {element_id}\n")
            self.console_widget.verticalScrollBar().setValue(self.console_widget.verticalScrollBar().maximum())  # Scroll to the bottom of the console
            self.highlight_element(element)  # Optional: Highlight the element if desired
            self.context_menu.exec_(self.mapToGlobal(pos))
    

    def copy_element_id(self):
        # Get the element at the mouse position
        element = self.webview.page().currentFrame().hitTestContent(self.context_menu_pos).element()

        if element:
            element_id = element.attribute("id")
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(element_id)
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("main.ui", self)
        website_text_edit = None
        self.fingerprints = []  # Initialize fingerprints list
        self.proxies = []  # Initialize proxies list
        self.start_hyperlink_button.clicked.connect(self.start_hyperlink_button_clicked)
        self.stop_hyperlink_button.clicked.connect(self.stop_hyperlink_button_clicked)
        self.save_hyperlink_button.clicked.connect(self.save_hyperlink_button_clicked)
        menubar = self.menuBar()
        menubar.setStyleSheet("QMenuBar::item { border: 1px solid teal; padding: 4px; font-weight: bold; }")
        # Create a File menu
        file_menu = menubar.addMenu('File')
        settings_menu = menubar.addMenu('Settings')
        network_settings_menu = settings_menu.addMenu('Network Settings')
        capture_settings_menu = settings_menu.addMenu('Capture Settings')
        about_menu = menubar.addMenu('About')
        
        # Create an Exit action in the File menu
        exit_action = QtWidgets.QAction('Exit', self)
        exit_action.triggered.connect(QtWidgets.QApplication.quit)
        file_menu.addAction(exit_action)
        
        # Add Proxy Settings and Authentication Methods to Network Settings menu
        proxy_settings_action = QtWidgets.QAction('Proxy Settings', self)
        auth_methods_action = QtWidgets.QAction('Authentication Methods', self)
        network_settings_menu.addAction(proxy_settings_action)
        network_settings_menu.addAction(auth_methods_action)
        
        # Add Scan for Username, Scan for Password, and Scan for Login Button to Capture Settings menu
        scan_username_action = QtWidgets.QAction('Scan for Username', self)
        scan_password_action = QtWidgets.QAction('Scan for Password', self)
        scan_login_button_action = QtWidgets.QAction('Scan for Login Button', self)
        capture_settings_menu.addAction(scan_username_action)
        capture_settings_menu.addAction(scan_password_action)
        capture_settings_menu.addAction(scan_login_button_action)
        
        # Connect actions to their respective dialogs or code implementation
        proxy_settings_action.triggered.connect(self.open_proxy_settings_dialog)
        auth_methods_action.triggered.connect(self.open_authentication_methods_dialog)
        scan_username_action.triggered.connect(self.scan_for_username)
        scan_password_action.triggered.connect(self.scan_for_password)
        scan_login_button_action.triggered.connect(self.scan_for_login_button)

        # Create a custom widget for recording
        recording_widget = QtWidgets.QWidget()
        recording_layout = QtWidgets.QHBoxLayout(recording_widget)

        # Create a label for the recording symbol
        recording_label = QtWidgets.QLabel()
        recording_label.setPixmap(QtGui.QPixmap("recording_icon.png"))  # Replace with your own recording icon
        recording_layout.addWidget(recording_label)

        # Add the custom widget to the menu bar
        menubar.setCornerWidget(recording_widget, QtCore.Qt.TopRightCorner)

        # Connect the recording widget's click event to the slot
        recording_widget.mousePressEvent = self.start_recording
        website_text_edit = QtWidgets.QTextEdit()  # Assign website_text_edit attribute
        # Rest of your code
        website_text_edit.textChanged.connect(self.connect_webview_load_finished)
        self.cookie_start_button.clicked.connect(self.cookie_start_button_clicked)
        self.stop_hyperlink_button.clicked.connect(lambda: self.stop_hyperlink_button_clicked("Stop"))
        # Create a custom context menu
        context_menu = QMenu()
        self.widget = QtWidgets.QWidget()
        self.widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.goto_website_button.clicked.connect(self.goto_website_function)
        self.combolist_text_edit = QtWidgets.QTextEdit()

        # Initialize browser layout
        self.browser_frame = self.findChild(QtWidgets.QFrame, 'browser_frame')  # Replace 'browser_frame' with the actual object name from your .ui file
        self.browser_layout = QtWidgets.QGridLayout(self.browser_frame)

        # Add button to layout (you may want to adjust where this goes)

        # Initialize view boosting handlers
        self.view_boosting_handlers = ViewBoostingHandlers(self)
        self.launch_subwindow_button.clicked.connect(self.open_sub_windows)

    def apply_settings_to_browsers(self):
         """Apply settings to each thread browser."""
         threads_count = self.view_boost_threads_spinbox.value()  # Get number of threads from spinbox

         if not self.fingerprints:
             QtWidgets.QMessageBox.warning(self, "Warning", "No fingerprints loaded.")
             return

         if not self.proxies:
             QtWidgets.QMessageBox.warning(self, "Warning", "No proxies loaded.")
             return

         assigned_fingerprints = [self.fingerprints[i % len(self.fingerprints)] for i in range(threads_count)]
         assigned_proxies = [self.proxies[i % len(self.proxies)] for i in range(threads_count)]

         for i in range(threads_count):
             fingerprint = assigned_fingerprints[i]
             proxy = assigned_proxies[i]

             # Update or display the fingerprint and proxy in the respective browser interface or console
             print(f"Thread {i + 1}: Fingerprint - {fingerprint}, Proxy - {proxy}")  # Replace with actual UI updates as needed


    def show_context_menu(self, pos, sub_window):
         """Show context menu for setting resolution options."""
         context_menu = QtWidgets.QMenu(sub_window)

         resolutions = {
             "800x600": (800, 600),
             "1024x768": (1024, 768),
             "1280x720": (1280, 720),
             "1920x1080": (1920, 1080),
         }

         for resolution_name, (width, height) in resolutions.items():
             action = context_menu.addAction(resolution_name)
             action.triggered.connect(lambda checked, w=width, h=height: sub_window.resize(w, h))

         context_menu.exec_(sub_window.mapToGlobal(pos))
    def open_browser_in_thread(self, url):
         """Open a browser instance in a separate thread."""
         web_view = QWebEngineView()  # Create a new web view instance
         web_view.setUrl(QtCore.QUrl(url))  # Navigate to the specified URL

         # You may want to manage this web view instance properly in your application,
         # such as adding it to a layout or displaying it in a specific way.



    def create_browser_interfaces(self, count):
         """Create and add browser interfaces to the browser frame."""
         
         total_width = 1001
         total_height = 500
         
         columns = 5  # Number of columns
         rows = (count + columns - 1) // columns  # Calculate number of rows needed
         
         web_view_width = total_width // columns
         web_view_height = total_height // rows
        
         available_fingerprints = self.fingerprints[:count]  # Get only as many fingerprints as there are browsers
    
         for i in range(count):
             web_view = QWebEngineView()  # Create a new web view instance
            
             fingerprint = available_fingerprints[i % len(available_fingerprints)] if available_fingerprints else "No Fingerprint Loaded"
            
             html_content = f"""
             <!DOCTYPE html>
             <html lang="en">
             <head>
                 <meta charset="UTF-8">
                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
                 <title>Browser #{i + 1}</title>
                 <style>
                     body {{
                         font-family: Arial, sans-serif;
                         text-align: center;
                         margin: 0;
                         padding: 20px;
                     }}
                 </style>
             </head>
             <body>
                 <h1>Browser #{i + 1}</h1>
                 <p>This is the content of Browser #{i + 1}.</p>
                 <p>Assigned Fingerprint: {fingerprint}</p>
                 <p>Proxy: Not Set</p> <!-- Placeholder for Proxy -->
             </body>
             </html>
             """
            
             web_view.setHtml(html_content)  # Load the HTML content into the web view
            
             web_view.setFixedSize(web_view_width, web_view_height)
    
             row, col = divmod(i, columns)  # Arrange in a grid
             self.browser_layout.addWidget(web_view, row, col)  # Add web view to the layout

    def open_sub_windows(self):
         """Open multiple subwindows based on the number of threads set by the user."""
         threads_count = self.view_boost_threads_spinbox.value()  # Get number of threads from spinbox

         url_target = self.view_boost_url_target_textEdit.toPlainText() or "http://example.com"  # Default URL if not set

         for i in range(threads_count):
             sub_window = QMdiSubWindow()
             sub_window.setWindowTitle(f"Browser Thread #{i + 1}")
             
             browser_view = QWebEngineView()
             browser_view.setUrl(QtCore.QUrl(url_target))  # Navigate to the specified URL

             content_widget = QtWidgets.QWidget()
             layout = QtWidgets.QVBoxLayout(content_widget)

             label = QtWidgets.QLabel(f"Thread #{i + 1} navigating to {url_target}")
             layout.addWidget(label)
             layout.addWidget(browser_view)  # Add the browser view to the layout

             sub_window.setWidget(content_widget)  # Set the content widget for the subwindow

             # Add the new subwindow to the MDI area (assuming mdiArea is defined in your .ui file)
             self.mdiArea.addSubWindow(sub_window)  
             sub_window.show()

    def apply_settings_to_browsers(self):
         """Apply loaded fingerprints and proxies to each browser."""
         threads_count = self.view_boost_threads_spinbox.value()  # Get number of threads from spinbox

         if not self.fingerprints:
             QtWidgets.QMessageBox.warning(self, "Warning", "No fingerprints loaded.")
             return

         if not self.proxies:
             QtWidgets.QMessageBox.warning(self, "Warning", "No proxies loaded.")
             return

         assigned_fingerprints = [self.fingerprints[i % len(self.fingerprints)] for i in range(threads_count)]
         assigned_proxies = [self.proxies[i % len(self.proxies)] for i in range(threads_count)]

         for i in range(threads_count):
             fingerprint = assigned_fingerprints[i]
             proxy = assigned_proxies[i]

             print(f"Thread {i + 1}: Fingerprint - {fingerprint}, Proxy - {proxy}")  # Replace with actual UI updates as needed






    def goto_website_function(self):
        url = self.website_text_edit.toPlainText()
        
        # Clear existing content
        if self.browser_frame.layout():
            while self.browser_frame.layout().count():
                item = self.browser_frame.layout().takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()
        else:
            # Create a new layout if one doesn't exist
            self.browser_frame.setLayout(QtWidgets.QVBoxLayout())
        
        browser_view = QtWebEngineWidgets.QWebEngineView()
        
        # Set user agent
        browser_view.page().profile().setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        
        browser_view.setUrl(QtCore.QUrl(url))
        
        # Add the browser view to the layout
        self.browser_frame.layout().addWidget(browser_view)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            with open(file_path, 'r') as file:
                text = file.read()
                self.combolist_text_edit.toPlainText(text)


    
    def toolbox_element_changed(self, current_index):
        toolbox_item = self.toolbox_combo_box.itemText(current_index)
        if toolbox_item == "Cookie Import Automation":
            self.close_selenium_browser()
            self.print_to_response_frame("Please start the Selenium browser again.")
        else:
            self.print_to_response_frame(f"Selected toolbox: {toolbox_item}")
    
    def close_selenium_browser(self):
        # Implement code to close the Selenium browser (e.g., driver.quit())
        if hasattr(self, 'driver'):
            self.driver.quit()
            self.driver = None



    def scan_for_username(self):
        self.display_scanning_dialog()
        element_classes = self.get_element_classes(['login', 'email', 'username', 'user', 'login-id'])
        self.display_element_classes(element_classes)

    def scan_for_password(self):
        self.display_scanning_dialog()
        element_classes = self.get_element_classes(['pass', 'password'])
        self.display_element_classes(element_classes)

    def scan_for_login_button(self):
        self.display_scanning_dialog()
        element_classes = self.get_element_classes(['login-button'])
        self.display_element_classes(element_classes)

    def display_scanning_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Scanning Source Code")
        layout = QVBoxLayout(dialog)
        label = QLabel("Scanning Source Code...")
        layout.addWidget(label)
        dialog.exec_()



    def display_element_classes(self, element_classes):
        # Implement the logic to display the element classes
        if element_classes:
            classes_str = "\n".join(element_classes)
            QtWidgets.QMessageBox.information(self, "Element Classes", classes_str)
        else:
            QtWidgets.QMessageBox.information(self, "Element Classes", "No relevant element classes found.")



    def start_recording(self, event):
        if not hasattr(self, 'driver') or self.driver is None:    
            recording_widget = self.menuBar().cornerWidget(QtCore.Qt.TopRightCorner)
            recording_label = recording_widget.layout().itemAt(0).widget()
            recording_label.setPixmap(QtGui.QPixmap("recording_icon_red.png"))
            browser_view = QtWebEngineWidgets.QWebEngineView()
            # Add the browser to the frame
            layout = QtWidgets.QVBoxLayout(self.browser_frame)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(browser_view)
            # Set the URL to the specified hyperlink
            browser_view.setUrl(QtCore.QUrl(self.website_text_edit.toPlainText()))
        else:
            self.print_to_response_frame("Recording is already active.")


    def show_record_started_dialog(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Information)
        dialog.setWindowTitle("Recording Started")
        dialog.setText("Recording has started.")
        dialog.exec_()

    def connect_webview_load_finished(self):
        url = self.website_text_edit.toPlainText()
        self.webview.loadFinished.disconnect()  # Disconnect the previous connection
        self.webview.loadFinished.connect(lambda _, url=url: self.on_load_finished(url))
    
    def on_load_finished(self, ok):
        if ok:
            # Get the main frame of the web page
            frame = self.webview.page().mainFrame()

            # Execute JavaScript code to access the input element
            element = frame.evaluateJavaScript(
                """
                document.querySelector('input[name="email"]')
                """
            )

            # Set the value of the input element
            element.setProperty("value", "example@example.com")

            # Print the value of the input element
            print("Input value:", element.property("value"))

            # Focus on the input element
            frame.evaluateJavaScript(
                """
                var input = document.querySelector('input[name="email"]');
                input.focus();
                """
            )

        
    def closeEvent(self, event):
        # Implement the desired actions when the window is closed
        # ...
        super(MainWindow, self).closeEvent(event)  # Call the superclass method to handle the event

    def open_proxy_settings_dialog(self):
        dialog = ProxySettingsDialog()
        dialog.exec_()

    def open_user_agent_spoofing_dialog(self):
        dialog = UserAgentSpoofingDialog()
        dialog.exec_()

    def open_request_throttling_dialog(self):
        dialog = RequestThrottlingDialog()
        dialog.exec_()

    def open_authentication_methods_dialog(self):
        dialog = AuthenticationMethodsDialog()
        dialog.exec_()

        # Connect actions to their respective dialogs
        proxy_settings_action.triggered.connect(self.open_proxy_settings_dialog)
        user_agent_spoofing_action.triggered.connect(self.open_user_agent_spoofing_dialog)
        request_throttling_action.triggered.connect(self.open_request_throttling_dialog)
        authentication_methods_action.triggered.connect(self.open_authentication_methods_dialog)


    def username_dropdown_button_clicked(self):
        print("Username dropdown button clicked")

    def combo_box_changed(self, index):
        selected_value = self.combo_box.itemText(index)
        print(f"Selected Value: {selected_value}")


    def signin_dropdown_button_clicked(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Signin Dropdown")

        layout = QtWidgets.QVBoxLayout(dialog)

        combo_box = QtWidgets.QComboBox()
        combo_box.addItem("Option 1")
        combo_box.addItem("Option 2")
        combo_box.addItem("Option 3")
        combo_box.addItem("Option 4")

        layout.addWidget(combo_box)
        dialog.setLayout(layout)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            selected_value = combo_box.currentText()
            print(f"Selected Signin Option: {selected_value}")


    def cookie_start_button_clicked(self):
        url = self.cookie_url_text_edit.text()
        self.console_widget_textedit.append(f"Loading URL: {url}")
        self.load_url(url)

    def load_url(self, url):
        # Implement code to load the URL using QtWebEngineWidgets
        # Example:
        self.web_view = QtWebEngineWidgets.QWebEngineView()
        self.web_view.load(QtCore.QUrl(url))
        self.web_view.page().loadFinished.connect(self.page_load_finished)

    def page_load_finished(self, ok):
        if ok:
            self.console_widget_textedit.append("Page loaded successfully!")
        else:
            self.console_widget_textedit.append("Failed to load page!")

    def password_dropdown_button_clicked(self):
        print("Password dropdown button clicked")


    def is_valid_url(self, url):
        parsed_url = urlparse(url)
        return bool(parsed_url.scheme) and bool(parsed_url.netloc)

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    layout.removeItem(item)
            del layout

    def start_hyperlink_button_clicked(self):
        homepage_url = "https://browserleaks.com/canvas"
    
        layout = self.browser_frame.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()
                else:
                    spacer = item.spacerItem()
                    if spacer:
                        spacer.changeSize(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            del layout
    
        browser_view = QtWebEngineWidgets.QWebEngineView()
        browser_view.setUrl(QtCore.QUrl(homepage_url))
        self.browser_frame.layout().addWidget(browser_view)
        self.browser_frame.show()
        
    

    def show_dropdown_dialog(self, button_name):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle(f"{button_name} Dropdown")
        layout = QtWidgets.QVBoxLayout(dialog)

        combo_box = QtWidgets.QComboBox()
        combo_box.addItem("X Path")
        combo_box.addItem("ID")
        combo_box.addItem("Element ID")
        combo_box.addItem("Name")

        layout.addWidget(combo_box)
        dialog.setLayout(layout)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            selected_value = combo_box.currentText()
            print(f"{button_name} dropdown selected value: {selected_value}")


    def print_to_response_frame(self, message):
        self.console_widget_textedit.append(message)






    def stop_hyperlink_button_clicked(self):
        if hasattr(self, 'driver'):
            # Safely retrieve and close the browser view if it exists
            layout = self.browser_frame.layout()
            if layout and layout.count() > 0:
                browser_view = layout.itemAt(0).widget()
                if browser_view:
                    browser_view.close()
                else:
                    self.print_to_response_frame("Browser view not found.")
            else:
                self.print_to_response_frame("Browser frame layout is empty.")
    
            self.driver.quit()
            self.print_to_response_frame("Browser stopped.")
    
            # Optionally, clear any UI elements related to the browser session here
        else:
            self.print_to_response_frame("No active browser session.")


    def save_hyperlink_button_clicked(self):
        hyperlink = self.website_text_edit.toPlainText()
        username_value = self.username_text_edit.toPlainText()
        password_value = self.password_text_edit.toPlainText()
        continue_value = self.continue_text_edit.toPlainText()
        signin_button_value = self.signin_button_text_edit.toPlainText()
    
        # Save the values to a file or use them as needed
    
        self.print_to_response_frame("Settings saved.")
    



class ElementInspector(QtWidgets.QMainWindow):
    def __init__(self, url):
        super(ElementInspector, self).__init__()

        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.webview)

        self.webview.loadFinished.connect(self.on_load_finished)
        self.webview.load(QtCore.QUrl(url))

        # Add context menu
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        self.context_menu = QtWidgets.QMenu(self)
        self.inspect_action = self.context_menu.addAction("Inspect Element")
        self.inspect_action.triggered.connect(self.inspect_element)
        self.grab_class_action = self.context_menu.addAction("Grab Element Class")
        self.grab_class_action.triggered.connect(self.grab_element_class)
        self.network_stats_action = self.context_menu.addAction("Network Stats")
        self.network_stats_action.triggered.connect(self.show_network_stats)
        self.start_sniffer_action = self.context_menu.addAction("Start Sniffer")
        self.start_sniffer_action.triggered.connect(self.start_sniffer)
        self.captcha_solver_action = self.context_menu.addAction("Captcha Solver")
        self.captcha_solver_action.triggered.connect(self.solve_captcha)
        self.customContextMenuRequested.connect(self.show_context_menu)

        # Store the recorded elements' XPath and CSS values
        self.recorded_elements = []

        # Store the highlighted element
        self.highlighted_element = None

        # Enable mouse tracking to capture mouse hover events
        self.setMouseTracking(True)

    def show_context_menu(self, pos):
        # Get the element at the mouse position
        element = self.webview.page().currentFrame().hitTestContent(pos).element()
    
        if element:
            element_id = element.attribute("id")
            self.console_widget.insertPlainText(f"Element ID: {element_id}\n")
            self.console_widget.verticalScrollBar().setValue(self.console_widget.verticalScrollBar().maximum())  # Scroll to the bottom of the console
            self.highlight_element(element)  # Optional: Highlight the element if desired
            self.context_menu.exec_(self.mapToGlobal(pos))
    
    def grab_element_class(self):
        if self.highlighted_element:
            class_id = self.highlighted_element.attribute("class")
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(class_id)

    def show_network_stats(self):
        # Implement code to show network stats
        pass

    def start_sniffer(self):
        # Implement code to start the sniffer
        pass

    def solve_captcha(self):
        # Implement code to solve the captcha
        pass

    def on_load_finished(self, ok):
        if ok:
            self.webview.page().runJavaScript(
                """
                document.addEventListener('mouseover', function(event) {
                    event.preventDefault();
                    var element = event.target;
                    var tag = element.tagName;
                    var id = element.id;
                    var classes = element.className.split(' ');
                    var attributes = Array.from(element.attributes).map(attr => attr.name + '=' + attr.value);
                    var info = {
                        'tag': tag,
                        'id': id,
                        'classes': classes,
                        'attributes': attributes
                    };
                    window.elementInspector.showElementInfo(info);
                });
                """
            )















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
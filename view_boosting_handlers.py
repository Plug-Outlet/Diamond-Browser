# view_boosting_handlers.py
import os
import sys
from PyQt5 import QtWidgets

class ViewBoostingHandlers:
    def __init__(self, main_window):
        self.main_window = main_window
        
        # Initialize console with default values
        self.initialize_console()

        # Connect UI elements to their respective functions
        self.main_window.view_boost_start_button.clicked.connect(self.start_view_boost)
        self.main_window.view_boost_proxy_load_pushButton.clicked.connect(self.load_proxies)
        self.main_window.view_boost_fingerprint_set_button.clicked.connect(self.set_fingerprint)

        # Connect spinbox value changes to update console
        self.main_window.view_boost_threads_spinbox.valueChanged.connect(self.update_console)
        self.main_window.view_boost_target_number_spinbox.valueChanged.connect(self.update_console)

    def initialize_console(self):
        """Initialize the console text edit with default values."""
        self.main_window.view_boost_console_textedit.setPlainText(
            "Threads: 1\n"
            "Target Number: 1\n"
            "URL Target: Not Set\n"
            "Fingerprints: None Loaded\n"
            "Proxies: Not Set\n"
            "Proxy Type: (Http or Socks5)\n"
            "Proxy Format: Not Set\n"
        )

    def update_console(self):
        """Update the console with current threads and target number."""
        threads = self.main_window.view_boost_threads_spinbox.value()
        target_number = self.main_window.view_boost_target_number_spinbox.value()
        
        # Clear previous lines related to threads and target number
        console_text = self.main_window.view_boost_console_textedit.toPlainText().splitlines()
        
        # Update threads and target number lines
        console_text[0] = f"Threads: {threads}"
        console_text[1] = f"Target Number: {target_number}"
        
        # Join updated lines back into a single string
        updated_console_text = "\n".join(console_text)
        
        # Set updated text back to console
        self.main_window.view_boost_console_textedit.setPlainText(updated_console_text)

    def start_view_boost(self):
        """Start the view boosting process."""
        url_target = self.main_window.view_boost_url_target_textEdit.toPlainText() or "Not Set"
        
        # Update console with current parameters
        self.main_window.view_boost_console_textedit.append(f"\nStarting View Boosting...")
        self.main_window.view_boost_console_textedit.append(f"URL Target: {url_target}")

    def load_proxies(self):
        """Load proxies from a file or other source."""
        proxy_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self.main_window, "Open Proxy File", "", "Text Files (*.txt);;All Files (*)")
        
        if proxy_file_path:
            with open(proxy_file_path, 'r') as file:
                proxies = file.readlines()
                # Assuming you want to populate a combo box or similar with these proxies
                self.main_window.view_boost_proxy_file_textedit.setPlainText(''.join(proxies))
                self.main_window.view_boost_console_textedit.append(f"Loaded {len(proxies)} proxies.")
                self.main_window.view_boost_console_textedit.append("Proxies: Loaded")

    def set_fingerprint(self):
        """Set fingerprint settings by selecting a folder containing fingerprint files."""
        
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            self.main_window,
            "Select Fingerprint Folder",
            "",
            QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks
        )
        
        if folder_path:
            # Display the selected folder path in the text edit
            self.main_window.view_boost_fingerprint_textedit.setPlainText(folder_path)
            
            # Count valid fingerprint files in the selected folder
            fingerprint_files = [f for f in os.listdir(folder_path) if f.endswith('.txt') or f.endswith('.json')]
            
            # Limit to first 10 fingerprints
            limited_fingerprints = fingerprint_files[:10]
            file_count = len(limited_fingerprints)
            
            if file_count > 0:
                self.main_window.fingerprints = limited_fingerprints  # Store only the first 10 fingerprints
                fingerprints_list = "\n".join(limited_fingerprints)
                self.main_window.view_boost_console_textedit.append(f"Fingerprints Loaded:\n{fingerprints_list}")
                self.main_window.view_boost_console_textedit.append(f"Total Fingerprints Loaded: {file_count}")
            else:
                self.main_window.view_boost_console_textedit.append("No valid fingerprint files found in the selected folder.")
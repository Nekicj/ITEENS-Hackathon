from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from ui.window_profile import Ui_Dialog

class ProfileDialog(QDialog):
    def __init__(self,username,name):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Profile")
        self.ui.profile_button.clicked.connect(self.close_dialog)
        self.ui.Name_profile.setText(f"Name: {name}")

    def close_dialog(self):
        self.close()

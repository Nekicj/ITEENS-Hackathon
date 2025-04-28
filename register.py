from PySide6.QtWidgets import QDialog, QLineEdit, QMessageBox
from logic.database import Database
from ui.window_register import Ui_Dialog

class RegisterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.db = Database()

        self.ui.register_button.clicked.connect(self.register_user)
        self.ui.see_password_cb_register.stateChanged.connect(self.toggle_password_visibility)
        self.setWindowTitle("Register")

    
    def toggle_password_visibility(self, state):
        if state == 2:
            self.ui.password_register.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.password_register.setEchoMode(QLineEdit.Password)

    def register_user(self):
        username = self.ui.username_register.text()
        password = self.ui.password_register.text()
        name = self.ui.name_register.text()

        if self.db.register_user(username, password, name):
            msg_box = QMessageBox()
            msg_box.setStyleSheet("QLabel{color: white;}")
            msg_box.setWindowTitle("Success")
            msg_box.setText("Вы Зарегистрированы!")
            msg_box.exec()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Такой пользователь уже есть, повторите")

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dialog = RegisterDialog()
    dialog.show()
    sys.exit(app.exec())
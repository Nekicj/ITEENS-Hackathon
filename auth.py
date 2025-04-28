# auth.py
from PySide6.QtWidgets import QDialog, QLineEdit, QMessageBox
from ui.window_auth import Ui_User
from logic.database import Database
from register import RegisterDialog
from my_profile import ProfileDialog

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_User()
        self.ui.setupUi(self)

        self.db = Database()

        self.ui.login_button.clicked.connect(self.try_login)  # Соединяем с методом try_login
        self.ui.see_password_cb.stateChanged.connect(self.toggle_password_visibility)
        self.ui.no_account.clicked.connect(self.open_register_dialog)

        self.setWindowTitle("Login")

    def open_register_dialog(self):
        register_dialog = RegisterDialog()
        self.db.close()
        self.close()
        register_dialog.exec()

    def toggle_password_visibility(self, state):
        if state == 2:
            self.ui.password_login.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.password_login.setEchoMode(QLineEdit.Password)

    def try_login(self):
        # Вызываем метод login() и сохраняем результат
        login_result = self.login()
        if login_result["success"]:
            # Если аутентификация успешна, получаем имя пользователя и открываем профиль
            username = login_result["username"]
            name = login_result["name"]
            self.close()
            self.show_profile_dialog(username, name)
        else:
            QMessageBox.warning(self, "Error", "Пользователь не найден:(")

    def login(self):
        username = self.ui.username_login.text()
        password = self.ui.password_login.text()
        user_data = self.db.login_user(username, password)
        if user_data:
            username = user_data[0]
            name = user_data[3]
            return {"success": True, "username": username, "name": name}
        else:
            return {"success": False}

    def show_profile_dialog(self, username, name):
        profile_dialog = ProfileDialog(username, name)
        profile_dialog.exec()
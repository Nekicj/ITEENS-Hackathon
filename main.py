from PySide6.QtWidgets import QApplication, QMainWindow,QDialog
from ui.window_main import Ui_MainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from logic.cipher import *
from logic.password_logic import *
from auth import LoginDialog
from my_profile import ProfileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Начальные настройки
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.show_menu1()

        # Коннектим функции к кнопкам
        ##############################################################
        self.ui.Button_Cipher_change.clicked.connect(self.show_cipher)    
        self.ui.PW_button.clicked.connect(self.show_PW_generator)
        self.ui.first.clicked.connect(self.show_menu1)
        self.ui.second.clicked.connect(self.show_menu2)
        self.ui.third.clicked.connect(self.show_menu3)
        self.ui.cipher_button.clicked.connect(self.perform_cipher)
        self.ui.pw_button.clicked.connect(self.generate_password)
        self.ui.Copy_password.clicked.connect(self.copy_password)
        self.ui.login_button.clicked.connect(self.open_login_dialog)
        ##############################################################

        self.set_hover_effects("icons/png/home_normal.png", "icons/png/home_hover.png", self.ui.first)
        self.set_hover_effects("icons/png/book_normal.png", "icons/png/book_hover.png", self.ui.second)
        self.set_hover_effects("icons/png/key_normal.png", "icons/png/key_hover.png", self.ui.third)
        self.set_hover_effects("icons/png/user_normal.png","icons/png/user_hover.png",self.ui.login_button)

    def set_hover_effects(self, normal_icon_path, hover_icon_path, button):
        button.setIcon(QIcon(normal_icon_path))
        button.enterEvent = lambda event, path=hover_icon_path: button.setIcon(QIcon(path))
        button.leaveEvent = lambda event, path=normal_icon_path: button.setIcon(QIcon(path))

    def open_login_dialog(self):
        login_dialog = LoginDialog()  # Создание экземпляра LoginDialog
        username = login_dialog.exec()  # Отображение диалогового окна и получение имени пользователя
        if username:  # Если имя пользователя получено (авторизация успешна)
            self.show_profile_dialog(str(username))  # Показать диалоговое окно профиля с именем пользователя

    def show_profile_dialog(self, username):
        profile_dialog = ProfileDialog(username)  # Создание экземпляра ProfileDialog с именем пользователя
        profile_dialog.exec()  # Отображение диалогового окна

    def generate_password(self):
        # Получаем параметры для генерации пароля
        length = self.ui.password_length_slider.value()
        use_lower = self.ui.lower_case.isChecked()
        use_upper = self.ui.upper_case.isChecked()
        use_digits = self.ui.numbers.isChecked()
        use_symbols = self.ui.symbols.isChecked()

        # Генерируем пароль
        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)

        # Отображаем пароль в Password_labe
        self.ui.Password_labe.setText(password)

    def copy_password(self):
        # Копируем текст из Password_labe в буфер обмена
        password = self.ui.Password_labe.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(password)
        
    def perform_cipher(self): # Функция для Шифера
        algorithm = self.ui.comboBox.currentText()
        text = self.ui.input.toPlainText()  # Используйте toPlainText() для получения текста из QTextBrowser

        result = hash_text(text, algorithm)

        self.ui.output.setText(str(result))
    
    def align_output_with_button(self):# Нужно для того чтобы цинтрировать результат если он слишом большой чтобы не выходил за рамки
        button_geometry = self.ui.cipher_button.geometry()
        output_geometry = self.ui.output.geometry()

        new_x = button_geometry.center().x() - output_geometry.width() / 2

        self.ui.output.move(new_x-15, output_geometry.y())


# Функции для вкладок   
    def show_PW_generator(self):# Показываем ТОЛЬКО вкладку с генератором пароля
        self.ui.menu1.hide()
        self.ui.menu2.hide()
        self.ui.menu3.show()
        self.ui.PW.show()
        self.ui.cipher.hide()
    def show_cipher(self):# Показываем ТОЛЬКО вкладку с Шифратором 
        self.ui.menu1.hide()
        self.ui.menu2.hide()
        self.ui.menu3.show()
        self.ui.PW.hide()
        self.ui.cipher.show()
    def show_menu1(self):# Показывать menu1
        self.ui.menu1.show()
        self.ui.menu2.hide()
        self.ui.menu3.hide()
    def show_menu2(self):# Показывать menu2
        self.ui.menu1.hide()
        self.ui.menu2.show()
        self.ui.menu3.hide()
    def show_menu3(self):# Показывать menu3
        self.ui.menu1.hide()
        self.ui.menu2.hide()
        self.ui.menu3.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Steps with a Shield")
    window.show()
    app.exec()

"""
Простой Калькулятор от
            Егора Твердохлеба
"""
import sys

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow
import config


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.entry_max_len = self.ui.le_entry.maxLength()

        QFontDatabase.addApplicationFont("font/Segoe UI Bold.ttf")

        self.entry_max_len = self.ui.le_entry.maxLength()
        self.entry = self.ui.le_entry
        self.temp = self.ui.lbl_temp

        for btn in config.BUTTONS:
            getattr(self.ui, btn).clicked.connect(self.add_digit)

        # Действия
        self.ui.btn_CE.clicked.connect(self.clear_entry_text)
        self.ui.btn_C.clicked.connect(self.clear_all_text)
        self.ui.btn_dot.clicked.connect(self.add_dot)
        self.ui.btn_calc.clicked.connect(self.calculate)
        self.ui.btn_remove.clicked.connect(self.backspace)
        self.ui.btn_change_sign.clicked.connect(self.change_sign)

        # Арифметические операции
        self.ui.btn_add.clicked.connect(self.math_operations)
        self.ui.btn_sub.clicked.connect(self.math_operations)
        self.ui.btn_div.clicked.connect(self.math_operations)
        self.ui.btn_mul.clicked.connect(self.math_operations)

        # Тригонометрические операции и другие
        self.ui.btn_cos.clicked.connect(self.math_trigonometric_operations_and_other)
        self.ui.btn_sin.clicked.connect(self.math_trigonometric_operations_and_other)
        self.ui.btn_tan.clicked.connect(self.math_trigonometric_operations_and_other)
        self.ui.btn_ln.clicked.connect(self.math_trigonometric_operations_and_other)
        self.ui.btn_sqrt.clicked.connect(self.math_trigonometric_operations_and_other)

    def add_digit(self) -> None:
        """Дабавляет числа в панель ввода.

        Args:
            digit(str): Хранит в себе число ввода

        Returns:
            None
        """
        self.clear_temp_text()
        self.remove_text_error()

        btn = self.sender()

        # Если в панеле ввода стоит 0, то ставим число кнопки, иначе дабавляем к ней число
        if self.entry.text() == '0':
            self.entry.setText(btn.text())
        else:
            self.entry.setText(self.entry.text() + btn.text())

    def clear_entry_text(self) -> None:
        self.clear_temp_text()
        self.remove_text_error()
        """Удаление текста из панели ввода

        Returns:
                None
        """
        self.entry.setText('0')

    def clear_all_text(self) -> None:
        """Удаляет текст из всех панелей вывода

        Returns:
                None
        """
        self.remove_text_error()
        self.temp.clear()
        self.entry.setText('0')

    def add_dot(self) -> None:
        self.clear_temp_text()
        """Дабавляет точку к числу

        Returns:
                None
        """
        if '.' not in self.entry.text():
            self.entry.setText(self.entry.text() + '.')

    def add_temp(self) -> None:
        """Берем текст из панели ввода и с знаком его ложим во временую панель

        Returns:
                None
        """
        btn = self.sender()

        if not self.temp.text() or self.temp.text().split()[-1] == '=':
            self.temp.setText(self.remove_trailing_zeros(self.entry.text()) + f' {btn.text()}')
            self.entry.setText('0')

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        """Убирает все незначающие нули и убирает пустую точку из числа

        Args:
            num(str): Строковое число у которого мы убираем нули

        Returns:
                str
        """
        n = "{:.10f}".format(float(num)).rstrip('0').rstrip('.')
        return n.replace('.0', '') if n.endswith('.0') else n

    def get_entry_text(self) -> float | int:
        """Преобразует строчный тип в удобный для вычисления

        Returns:
                float,
                int
        """
        entry = self.remove_trailing_zeros(self.entry.text())
        return float(entry) if '.' in entry else int(entry)

    def get_temp_text(self) -> float | int | None:
        """Если находит во временой панеле строку то преобразует в число удобное для вычисления

        Returns:
                float,
                int,
                None
        """
        if self.temp.text():
            temp = self.temp.text().split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> str:
        """Забираем знак у временой панели если оное существует

        Returns:
                str
        """
        if self.temp.text():
            sign = self.temp.text().split()[-1]
            return sign

    def calculate(self) -> None:
        """Вычисляет выражение

        Returns:
                None
        """
        self.clear_temp_text()

        try:
            if self.temp.text():
                result = self.remove_trailing_zeros(config.OPERATIONS[self.get_math_sign()]
                                                    (self.get_temp_text(), self.get_entry_text()))
                self.temp.setText(self.temp.text() + f" {self.remove_trailing_zeros(self.entry.text())} =")
                self.entry.setText(result)
        except KeyError:
            pass
        except ZeroDivisionError:
            self.show_error(config.ERROR_ZERO_DIV)

    def math_operations(self) -> None:
        """Поведение при нажатии на арифметические операции

        Returns:
                None
        """
        btn = self.sender()
        if not self.temp.text():
            self.add_temp()
        else:
            if self.get_math_sign() == '=':
                self.add_temp()
            else:
                self.temp.text().split()[-1] = btn.text()

    def disable_buttons(self, disable: bool) -> None:
        """Выключает определенный кнопки на нажатие во время ошибки

        Returns:
                None
        """
        self.ui.btn_dot.setDisabled(disable)
        self.ui.btn_ln.setDisabled(disable)
        self.ui.btn_change_sign.setDisabled(disable)
        self.ui.btn_sqrt.setDisabled(disable)
        self.ui.btn_calc.setDisabled(disable)
        self.ui.btn_add.setDisabled(disable)
        self.ui.btn_tan.setDisabled(disable)
        self.ui.btn_sin.setDisabled(disable)
        self.ui.btn_sub.setDisabled(disable)
        self.ui.btn_div.setDisabled(disable)
        self.ui.btn_cos.setDisabled(disable)
        self.ui.btn_mul.setDisabled(disable)

        color = 'color: #888;' if disable else 'color: white;'
        self.change_buttons_color(color)

    def change_buttons_color(self, css_color: str) -> None:
        """Меняет цвет кнопок

        Args:
            css_color: строка типа: 'color: #234;'

        Returns:
                None
        """
        self.ui.btn_dot.setStyleSheet(css_color)
        self.ui.btn_ln.setStyleSheet(css_color)
        self.ui.btn_change_sign.setStyleSheet(css_color)
        self.ui.btn_sqrt.setStyleSheet(css_color)
        self.ui.btn_calc.setStyleSheet(css_color)
        self.ui.btn_add.setStyleSheet(css_color)
        self.ui.btn_tan.setStyleSheet(css_color)
        self.ui.btn_sin.setStyleSheet(css_color)
        self.ui.btn_sub.setStyleSheet(css_color)
        self.ui.btn_div.setStyleSheet(css_color)
        self.ui.btn_cos.setStyleSheet(css_color)
        self.ui.btn_mul.setStyleSheet(css_color)

    def show_error(self, text: str) -> None:
        """Метод для выставления ошибки с увеличение строки ввода

        Args:
            text(str): Текст ошибки

        Returns:

        """
        self.temp.clear()
        self.disable_buttons(True)

        self.entry.setMaxLength(len(text))
        self.entry.setText(text)

    def remove_text_error(self) -> None:
        """Удаляет все изменения ошибки и саму ошибку

        Returns:
                None
        """
        if self.entry.text() in (config.ERROR_ZERO_DIV, config.ERROR_UNDEFINED):
            self.entry.setMaxLength(self.entry_max_len)
            self.entry.setText('0')
            self.disable_buttons(False)

    def math_trigonometric_operations_and_other(self) -> None:
        """Поведение при нажатии на тригонометрические операции и другие

        Returns:
                None
        """
        self.clear_temp_text()

        btn = self.sender()
        try:
            self.entry.setText(str(self.remove_trailing_zeros(config.TRIGONOMETRIC_OPERATIONS[btn.text()]
                                                              (self.get_entry_text()))))
        except ValueError:
            self.show_error(config.ERROR_UNDEFINED)

    def clear_temp_text(self) -> None:
        """Удаляет текст из временой панели когда во временом выражении уже есть =

        Returns:
                None
        """
        if self.temp.text():
            if self.temp.text().split()[-1] == '=':
                self.temp.clear()

    def backspace(self) -> None:
        """Удаляем символ из панели вывода

        Returns:
                None
        """
        self.clear_temp_text()
        self.remove_text_error()

        entry = self.entry.text()
        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.entry.setText('0')
            else:
                self.entry.setText(self.entry.text()[:-1])
        else:
            self.entry.setText('0')

    def change_sign(self) -> None:
        """Меняет знак числа

        Returns:
                None
        """
        self.clear_temp_text()
        entry = self.entry.text()

        if '-' not in entry:
            if entry != '0':

                if len(entry) == self.entry_max_len:
                    self.entry.setMaxLength(self.entry_max_len + 1)
                else:
                    self.entry.setMaxLength(self.entry_max_len)

                entry = '-' + entry
        else:
            entry = entry[1:]
            self.entry.setMaxLength(self.entry_max_len)

        self.entry.setText(entry)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())

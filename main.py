import sys
import os
import math

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from functools import partial

num = ''
temp_num = ''
opr = ''
dote = False


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()
        self.ui.textEdit.setText('0')

        self.ui.btn_zero.clicked.connect(partial(self.enter_num, 0))
        self.ui.btn_one.clicked.connect(partial(self.enter_num, 1))
        self.ui.btn_two.clicked.connect(partial(self.enter_num, 2))
        self.ui.btn_three.clicked.connect(partial(self.enter_num, 3))
        self.ui.btn_four.clicked.connect(partial(self.enter_num, 4))
        self.ui.btn_five.clicked.connect(partial(self.enter_num, 5))
        self.ui.btn_six.clicked.connect(partial(self.enter_num, 6))
        self.ui.btn_seven.clicked.connect(partial(self.enter_num, 7))
        self.ui.btn_eight.clicked.connect(partial(self.enter_num, 8))
        self.ui.btn_nine.clicked.connect(partial(self.enter_num, 9))

        self.ui.btn_mul.clicked.connect(self.enter_mul)
        self.ui.btn_divide.clicked.connect(self.enter_divid)
        self.ui.btn_sub.clicked.connect(self.enter_sub)
        self.ui.btn_plus.clicked.connect(self.enter_plus)
        self.ui.btn_tan.clicked.connect(self.enter_tan)
        self.ui.btn_cos.clicked.connect(self.enter_cos)
        self.ui.btn_sin.clicked.connect(self.enter_sin)

        self.ui.btn_equal.clicked.connect(self.enter_equal)
        self.ui.btn_clear.clicked.connect(self.enter_clear)
        self.ui.btn_dote.clicked.connect(self.enter_dote)

    def enter_num(self, n):
        global num
        global temp_num
        num = num + str(n)
        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_mul(self):
        global temp_num
        global num
        global opr
        if (num or temp_num):
            if opr:
                if num:
                    temp_num = str(self.amaliat())
                    num = ''
                    self.ui.textEdit.setText((str(temp_num) + "*"))
                else:
                    self.ui.textEdit.setText((str(temp_num) + "*"))

            else:
                self.ui.textEdit.setText((str(num) + "*"))
                temp_num = num
                num = ''
            opr = '*'

    def enter_divid(self):
        global temp_num
        global num
        global opr
        if (num or temp_num):
            if opr:
                if num:
                    temp_num = str(self.amaliat())
                    num = ''
                    self.ui.textEdit.setText((str(temp_num) + "/"))
                else:
                    self.ui.textEdit.setText((str(temp_num) + "/"))

            else:
                self.ui.textEdit.setText((str(num) + "/"))
                temp_num = num
                num = ''
            opr = '/'

    def enter_sub(self):
        global temp_num
        global num
        global opr
        if (num or temp_num):
            if opr:
                if num:
                    temp_num = str(self.amaliat())
                    num = ''
                    self.ui.textEdit.setText((str(temp_num) + "-"))
                else:
                    self.ui.textEdit.setText((str(temp_num) + "-"))

            else:
                self.ui.textEdit.setText((str(num) + "-"))
                temp_num = num
                num = ''
            opr = '-'

    def enter_plus(self):
        global temp_num
        global num
        global opr

        if (num or temp_num):
            if opr:
                if num:
                    temp_num = str(self.amaliat())
                    num = ''
                    self.ui.textEdit.setText((str(temp_num) + "+"))
                else:
                    self.ui.textEdit.setText((str(temp_num) + "+"))
            else:
                self.ui.textEdit.setText((str(num) + "+"))
                temp_num = num
                num = ''
            opr = '+'

    def enter_tan(self):
        global num
        if num:
            self.ui.textEdit.setText(str(math.tan(float(num))))
        elif temp_num:
            self.ui.textEdit.setText(str(math.tan(float(temp_num))))
        num = ''

    def enter_cos(self):
        global num
        if num:
            self.ui.textEdit.setText(str(math.cos(float(num))))
        elif temp_num:
            self.ui.textEdit.setText(str(math.cos(float(temp_num))))
        num = ''

    def enter_sin(self):
        global num
        if num:
            self.ui.textEdit.setText(str(math.sin(float(num))))
        elif temp_num:
            self.ui.textEdit.setText(str(math.sin(float(temp_num))))
        num = ''

    def enter_dote(self):
        global num
        if (num.count('.') == 0):
            num = num + '.'
            if temp_num:
                self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
            else:
                self.ui.textEdit.setText(str(num))

    def enter_equal(self):
        global temp_num
        global num
        global opr
        temp_num = float("{:.2f}".format(float(temp_num)))
        num = float("{:.2f}".format(float(num)))
        if opr == '*':
            self.ui.textEdit.setText(str(temp_num * num))
            temp_num = num * temp_num
        elif opr == '/':
            self.ui.textEdit.setText(str(temp_num / num))
            temp_num = num / temp_num
        elif opr == '-':
            self.ui.textEdit.setText(str(temp_num - num))
            temp_num = num - temp_num
        elif opr == '+':
            self.ui.textEdit.setText(str(temp_num + num))
            temp_num = num + temp_num
        else:
            self.ui.textEdit.setText('')
        num = ''
        print('eq opr => ', opr)

    def amaliat(self):
        global temp_num
        global num
        global opr
        print(num, '-------', temp_num)
        print('ama opr => ', opr)

        temp_num = float("{:.2f}".format(float(temp_num)))
        num = float("{:.2f}".format(float(num)))
        print(num, '-------', temp_num)
        if opr == '*':
            return float("{:.2f}".format(float(temp_num * num)))
        elif opr == '/':
            return float("{:.2f}".format(float(temp_num / num)))
        elif opr == '-':
            return float("{:.2f}".format(float(temp_num - num)))
        else:
            return float("{:.2f}".format(float(temp_num + num)))

    def enter_clear(self):
        global temp_num
        global num
        global opr
        num = ''
        temp_num = ''
        opr = ''
        self.ui.textEdit.setText("0")

#------------------- END CLASS MAIM -------------------#


if __name__ == "__main__":
    app = QApplication([])
    widget = main()
    sys.exit(app.exec_())

# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

nums = 0
temp_num_1 = 0
opr = ''


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()
        self.ui.textEdit.setText('0')
        nums = 0

        self.ui.btn_zero.clicked.connect(self.enter_num_0)
        self.ui.btn_one.clicked.connect(self.enter_num_1)
        self.ui.btn_two.clicked.connect(self.enter_num_2)
        self.ui.btn_three.clicked.connect(self.enter_num_3)
        self.ui.btn_four.clicked.connect(self.enter_num_4)
        self.ui.btn_five.clicked.connect(self.enter_num_5)
        self.ui.btn_six.clicked.connect(self.enter_num_6)
        self.ui.btn_seven.clicked.connect(self.enter_num_7)
        self.ui.btn_eight.clicked.connect(self.enter_num_8)
        self.ui.btn_nine.clicked.connect(self.enter_num_9)

        self.ui.btn_mul.clicked.connect(self.enter_mul)
        self.ui.btn_divide.clicked.connect(self.enter_divid)
        self.ui.btn_sub.clicked.connect(self.enter_sub)
        self.ui.btn_plus.clicked.connect(self.enter_plus)
        self.ui.btn_tan.clicked.connect(self.enter_tan)
        self.ui.btn_cos.clicked.connect(self.enter_cos)
        self.ui.btn_sin.clicked.connect(self.enter_sin)

        self.ui.btn_equal.clicked.connect(self.enter_equal)

    # def sum_two_numbers(self):

    #     a = float(self.ui.tb1.text())
    #     b = float(self.ui.tb2.text())
    #     c = a + b
    #     self.ui.tb3.setText(str(c))

    def enter_num_1(self):
        global nums
        nums *= 10
        nums += 1
        self.ui.textEdit.setText(str(nums))

    def enter_num_2(self):
        global nums
        nums *= 10
        nums += 2
        self.ui.textEdit.setText(str(nums))

    def enter_num_3(self):
        global nums
        nums *= 10
        nums += 3
        self.ui.textEdit.setText(str(nums))

    def enter_num_4(self):
        global nums
        nums *= 10
        nums += 4
        self.ui.textEdit.setText(str(nums))

    def enter_num_5(self):
        global nums
        nums *= 10
        nums += 5
        self.ui.textEdit.setText(str(nums))

    def enter_num_6(self):
        global nums
        nums *= 10
        nums += 6
        self.ui.textEdit.setText(str(nums))

    def enter_num_7(self):
        global nums
        nums *= 10
        nums += 7
        self.ui.textEdit.setText(str(nums))

    def enter_num_8(self):
        global nums
        nums *= 10
        nums += 8
        self.ui.textEdit.setText(str(nums))

    def enter_num_9(self):
        global nums
        nums *= 10
        nums += 9
        self.ui.textEdit.setText(str(nums))

    def enter_num_0(self):
        global nums
        nums *= 10
        self.ui.textEdit.setText(str(nums))

    def enter_mul(self):
        global temp_num_1
        global nums
        global opr
        self.ui.textEdit.setText((str(nums) + " * "))
        opr = '*'
        temp_num_1 = nums
        nums = 0

    def enter_divid(self):
        global temp_num_1
        global nums
        global opr
        self.ui.textEdit.setText((str(nums) + " / "))
        opr = '/'
        temp_num_1 = nums
        nums = 0

    def enter_sub(self):
        global temp_num_1
        global nums
        global opr
        self.ui.textEdit.setText((str(nums) + " - "))
        opr = '-'
        temp_num_1 = nums
        nums = 0

    def enter_plus(self):
        global temp_num_1
        global nums
        global opr
        self.ui.textEdit.setText((str(nums) + " + "))
        opr = '+'
        temp_num_1 = nums
        nums = 0

    def enter_tan(self):
        global temp_num_1
        global nums
        self.ui.textEdit.setText((str(nums) + " tan "))
        temp_num_1 = nums
        nums = 0

    def enter_cos(self):
        global temp_num_1
        global nums
        global opr
        self.ui.textEdit.setText((str(nums) + " cos "))
        temp_num_1 = nums
        nums = 0

    def enter_sin(self):
        global temp_num_1
        global nums
        global opr
        self.ui.textEdit.setText((str(nums) + " sin "))
        temp_num_1 = nums
        nums = 0

    def enter_equal(self):
        global temp_num_1
        global nums
        global opr
        if opr == '*':
            self.ui.textEdit.setText(str(temp_num_1 * nums))
        elif opr == '/':
            self.ui.textEdit.setText(str(temp_num_1 / nums))
        elif opr == '-':
            self.ui.textEdit.setText(str(temp_num_1 - nums))
        elif opr == '+':
            self.ui.textEdit.setText(str(temp_num_1 + nums))
        else:
            self.ui.textEdit.setText('')


# num_text='0'
arr = []
if __name__ == "__main__":
    app = QApplication([])
    widget = main()
    sys.exit(app.exec_())

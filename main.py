import sys
import os
import math

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

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
        self.ui.btn_clear.clicked.connect(self.enter_clear)
        self.ui.btn_dote.clicked.connect(self.enter_dote)

        #----------------------- STYLES -------------------------#

        self.ui.btn_zero.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: white")
        self.ui.btn_one.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: white")
        self.ui.btn_two.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: white")
        self.ui.btn_three.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: white")
        self.ui.btn_four.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: white")
        self.ui.btn_five.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: white")
        self.ui.btn_six.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: white")
        self.ui.btn_seven.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: white")
        self.ui.btn_eight.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: white")
        self.ui.btn_nine.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: white")

        self.ui.btn_mul.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: #fdfdfd ; color: orange ;")
        self.ui.btn_divide.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: #fdfdfd ; color: orange ;")
        self.ui.btn_sub.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: #fdfdfd ; color: orange ;")
        self.ui.btn_plus.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: #fdfdfd ; color: orange ;")
        self.ui.btn_tan.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: #fdfdfd ; color: orange ;")
        self.ui.btn_cos.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: #fdfdfd ; color: orange ;")
        self.ui.btn_sin.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: #fdfdfd ; color: orange ;")
        self.ui.btn_equal.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: #fdfdfd ; color: orange ;")
        self.ui.btn_clear.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: #fdfdfd ; color: orange ;")
        self.ui.btn_dote.setStyleSheet(
            " border-radius: 25px ; font-size : 16px ; margin: 2px ; background-color: #fdfdfd ; color: orange ;")

        self.ui.textEdit.setStyleSheet(
            " background-color: #f1f1f1 ; border: 0px ;font-size : 18px ; padding: 15px")

        #----------------------- END STYLES -------------------------#

    def enter_num_1(self):
        global num
        global temp_num
        num = num + '1'
        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_num_2(self):
        global num
        num = num + '2'
        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_num_3(self):
        global num
        num = num + '3'
        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_num_4(self):
        global num
        num = num + '4'
        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_num_5(self):
        global num
        num = num + '5'

        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_num_6(self):
        global num
        num = num + '6'
        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_num_7(self):
        global num
        num = num + '7'
        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_num_8(self):
        global num
        global temp_num
        global opr
        num = num + '8'
        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_num_9(self):
        global num
        num = num + '9'
        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_num_0(self):
        global num
        if len(num) > 0 or temp_num:
            num = num + '0'
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
                temp_num = self.amaliat()
                num = ''
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
                temp_num = self.amaliat()
                num = ''
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
                temp_num = self.amaliat()
                num = ''
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
                temp_num = self.amaliat()
                num = ''
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
        num = num + '.'
        if temp_num:
            self.ui.textEdit.setText(str(temp_num) + (opr) + str(num))
        else:
            self.ui.textEdit.setText(str(num))

    def enter_equal(self):
        global temp_num
        global num
        global opr
        if opr == '*':
            self.ui.textEdit.setText(str((float(temp_num)) * (float(num))))
            temp_num = (float(num)) * (float(temp_num))
        elif opr == '/':
            self.ui.textEdit.setText(str((float(temp_num)) / (float(num))))
            temp_num = (float(num)) / (float(temp_num))
        elif opr == '-':
            self.ui.textEdit.setText(str((float(temp_num)) - (float(num))))
            temp_num = (float(num)) - (float(temp_num))
        elif opr == '+':
            self.ui.textEdit.setText(str(float(temp_num) + (float(num))))
            temp_num = (float(num)) + (float(temp_num))
        else:
            self.ui.textEdit.setText('')
        num = ''

    def amaliat(self):
        global temp_num
        global num
        global opr
        if opr == '*':
            return(str(float(temp_num) * float(num)))
        elif opr == '/':
            return(str(float(temp_num) / float(num)))
        elif opr == '-':
            return(str(float(temp_num) - float(num)))
        else:
            return(str(float(temp_num) + float(num)))

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

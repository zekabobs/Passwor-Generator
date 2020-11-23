import sys, random, re
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui import Ui_MainWindow

class PGenerator(QMainWindow):
    def __init__(self):
        super(PGenerator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Password generator')
        self.ui.spinBox.setValue(8)
        self.ui.pushButton.clicked.connect(self.generate_password)

    def generate_password(self):
        self.ui.lineEdit.setText('')

        #password settings
        password = ''
        password_length = self.ui.spinBox.value()
        password_complexity = self.ui.horizontalSlider.value()

        #pattern for password from only one alphabet
        pattern = '[a-z]+|[A-Z]+|[0-9]+'

        # E - Easy password. Alphabet volume = 10 or 23
        if password_complexity == 1:
            password = ''.join(random.choices(random.choice(level), k = password_length))

        # M - Middle password. Alphabet volume = 33 or 46
        elif password_complexity == 2:
            alphabet = level.copy()
            alphabet.pop(random.randint(0,2))
            alphabet = alphabet[0] + alphabet[1]
            while True:
                password = self.getPassword(alphabet, password_length)
                if re.match(pattern, password).group(0) != password:
                    break

        # H - Hard password. Alphabet volume = 56
        elif password_complexity == 3:
            alphabet = latin_lower + latin_upper + digits # or level.copy() and alp[0] + alp[1] + alp[2]
            while True:
                password = self.getPassword(alphabet, password_length)

                r1, r2, r3 = re.search('[a-z]+', password) is None,\
                             re.search('[A-Z]+', password) is None,\
                             re.search('[0-9]+', password) is None

                if re.match(pattern, password).group(0) != password and  not r1 and not r2 and not r3:
                    break

        # VH - Very Hard password. Alphabet volume = 65
        else:
            alphabet = latin_lower + latin_upper + digits + chars
            while True:
                password = self.getPassword(alphabet, password_length)
                r1, r2, r3 ,r4 = re.search('[a-z]+', password) is None,\
                                 re.search('[A-Z]+', password) is None,\
                                 re.search('[0-9]+', password) is None, \
                                 re.search('[!#-&*?+^]+', password) is None

                if re.match(pattern, password) != None and re.match(pattern, password).group(0) != password\
                        and not r1 and not r2 and not r3 and not r4:
                    break
        self.ui.lineEdit.setText(password)

    #return a random value until it matches the template requirements
    def getPassword(self,alphabet, length):
        return ''.join((random.choices(alphabet, k = length)))

chars = ['#','$','%','^','&','*','!','@','?']
latin_lower = [chr(x) for x in range(ord('a'),ord('z'))]
latin_upper = [chr(x) for x in range(ord('A'),ord('Z'))]
digits = [chr(x) for x in range(ord('0'),ord('9'))]
level = [ latin_lower, latin_upper, digits ]

app = QApplication([])
application = PGenerator()
application.show()

sys.exit(app.exec_())
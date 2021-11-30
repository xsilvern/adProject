from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from MineSweeper import MineSweeper
class Button(QToolButton):

    def __init__(self, text, callback,x,y):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)
        self.x=x
        self.y=y
    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class MineSweeperGame(QWidget):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.mineSweeperMapLayout = QGridLayout()
        statusLayout = QGridLayout()

        self.clearText = QLineEdit()
        self.clearText.setReadOnly(True)
        self.clearText.setText("...")
        self.clearText.setAlignment(Qt.AlignCenter)
        statusLayout.addWidget(self.clearText,0,0)

        self.exSizeText = QLineEdit()
        self.exSizeText.setReadOnly(True)
        self.exSizeText.setText("크기 설정(20 이하 권장)")
        self.exSizeText.setAlignment(Qt.AlignCenter)
        statusLayout.addWidget(self.exSizeText,1,0)

        self.sizeText = QLineEdit()
        self.sizeText.setAlignment(Qt.AlignCenter)
        statusLayout.addWidget(self.sizeText,2,0)

        self.exMCountText = QLineEdit()
        self.exMCountText.setReadOnly(True)
        self.exMCountText.setText("지뢰 개수 설정")
        self.exMCountText.setAlignment(Qt.AlignCenter)
        statusLayout.addWidget(self.exMCountText,3,0)

        self.mCountText = QLineEdit()
        self.mCountText.setAlignment(Qt.AlignCenter)
        statusLayout.addWidget(self.mCountText,4,0)
                
        self.restartButton = QToolButton()
        self.restartButton.setText("시작")
        self.restartButton.clicked.connect(self.startGame)
        self.restartButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        statusLayout.addWidget(self.restartButton,5,0)
        
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(self.mineSweeperMapLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 1, 0)

        self.setLayout(mainLayout)
        
        self.setWindowTitle('MineSweeper Game')
        
    def startGame(self):
        self.size = 0
        self.mCount = 0
        try:
            self.size=int(self.sizeText.text())
            self.mCount=int(self.mCountText.text())
        except:
            QMessageBox.warning(self,"경고","크기와 지뢰 개수에는 정수만 입력해주십시오")
            return
        if self.size**2<=self.mCount:
            QMessageBox.warning(self,"경고","지뢰 개수가 크기의 제곱보다 크면 안됩니다.")
            return
        if self.mCount<=1 or self.size<=1:
            QMessageBox.warning(self,"경고","지뢰 개수와 크기는 1보다 커야 합니다")
            return
        self.clearText.setText("...")
        
        self.gameOver=False
        self.ButtonList=[[0 for i in range(self.size)]for j in range(self.size)]
        for y in range(self.size):
            for x in range(self.size):
                button=Button('□',self.buttonClicked,x,y)
                self.ButtonList[y][x]=button
                self.mineSweeperMapLayout.addWidget(button,x,y)
        
        self.mineSweeper=MineSweeper(self.size,self.mCount)
                
    def buttonClicked(self):
        if not self.gameOver:
            button=self.sender()
            blockList=self.mineSweeper.chooseBlock(button.x,button.y)
            for b in blockList:
                x, y = b
                num = self.mineSweeper.showBlock(x,y)
                if num == 0:
                    self.ButtonList[y][x].setText(' ')
                elif num == -1:
                    self.ButtonList[y][x].setText('*')
                else:
                    self.ButtonList[y][x].setText(str(num))
            c = self.mineSweeper.isClear()
            print(c)
            if c == 1:
                self.clearText.setText("클리어")
                self.gameOver = True
                self.showAll()
            elif c == 2 :
                self.clearText.setText("사망")
                self.gameOver = True
                self.showAll()
                
    def showAll(self):
        m=self.mineSweeper.getMap()
        for y in range(self.size):
            for x in range(self.size):
                num = m[y][x]
                if num == 0:
                    self.ButtonList[y][x].setText(' ')
                elif num == -1:
                    self.ButtonList[y][x].setText('*')
                else:
                    self.ButtonList[y][x].setText(str(num))
                    
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    game=MineSweeperGame()
    game.show()
    sys.exit()

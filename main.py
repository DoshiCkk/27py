from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QLineEdit
import requests



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')



        self.widget= QWidget()
        self.layout = QVBoxLayout()

    
        self.label= QLabel('Выводит json файл и сохраняет')
        self.input = QLineEdit()
        self.button = QPushButton('сохранить')
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)
   

        self.widget.setLayout(self.layout)


        self.button.clicked.connect(self.click)
        self.setCentralWidget(self.widget)

    def click(self):
        integ = int(self.input.text())
        url = f'https://jsonplaceholder.typicode.com/todos/{integ}'
        req = requests.get(url)
        with open(f'data{integ}.json', 'w') as file:
            file.write(req.text)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
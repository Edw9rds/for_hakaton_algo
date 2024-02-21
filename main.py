import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class SpaceQuizApp(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Викторина о космосе") 
        self.setGeometry(100, 100, 400, 300) 

        self.questions = [
            {
                "question": "Какая планета является самой большой в Солнечной системе?",
                "correct_answer": "Юпитер"
            },
            {
                "question": "Как называется спутник земли?",
                "correct_answer": "Луна"
            },
            {
                "question": "Какая планета является самой близкой к Солнцу?",
                "correct_answer": "Меркурий"
            }
        ]

        self.current_question = 0

        self.layout = QVBoxLayout()

        self.question_label = QLabel(self.questions[self.current_question]["question"])
        self.layout.addWidget(self.question_label)

        self.btn_answer1 = QPushButton("Марс")
        self.btn_answer1.clicked.connect(self.check_answer)
        self.layout.addWidget(self.btn_answer1)

        self.btn_answer2 = QPushButton("Юпитер")
        self.btn_answer2.clicked.connect(self.check_answer)
        self.layout.addWidget(self.btn_answer2)

        self.btn_answer3 = QPushButton("Земля")
        self.btn_answer3.clicked.connect(self.check_answer)
        self.layout.addWidget(self.btn_answer3)

        self.correct_answer = self.questions[self.current_question]["correct_answer"]

        self.setLayout(self.layout)

    def check_answer(self):
        sender = self.sender()
        if sender.text() == self.correct_answer:
            self.question_label.setText("Верно! Правильный ответ: " + self.correct_answer)
        else:
            self.question_label.setText("Неверно. Попробуйте еще раз.")

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.question_label.setText(self.questions[self.current_question]["question"])
            self.correct_answer = self.questions[self.current_question]["correct_answer"]
        else:
            self.question_label.setText("Вопросы закончились.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpaceQuizApp()
    window.show()
    sys.exit(app.exec_())

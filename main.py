import sys 
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtCore import QTimer, Qt, QTime
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создание и настройка QLabel для отображения времени
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        font = QFont("Arial", 15, QFont.Weight.Bold)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: white")
        self.time_label.setFixedSize(150, 30)

        # Создание и настройка таймера для обновления времени
        self.timer = QTimer()
        self.timer.setInterval(1000) # Обновление каждую секунду

        self.timer.timeout.connect(self.update_time)

        # Показ окна и запуск таймера
        self.show()
        self.timer.start()

        self.move(0, 0)

    def update_time(self):
        current_time = QTime.currentTime()
        time_text = current_time.toString("hh:mm:ss")
        self.time_label.setText(time_text)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_M:
            sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

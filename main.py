from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("TIMER")
        self.setGeometry(50, 50, 300, 200)  # Adjusted window size for better layout

        # Ask user input
        seconds, ok = QInputDialog.getInt(self, "Set Timer", "Enter countdown time in seconds:")
        if not ok or seconds <= 0:
            seconds = 10

        self.remaining_time = seconds
        self.timer_running = True
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Buttons
        pause_button = QPushButton('Pause')
        pause_button.clicked.connect(self.pause_time)

        stop_button = QPushButton('Stop')
        stop_button.clicked.connect(self.stop_time)

        resume_button = QPushButton("Resume")
        resume_button.clicked.connect(self.resume_time)

        new_timer = QPushButton('Set New Timer')
        new_timer.clicked.connect(self.new_timer)

        # Layout and label
        layout = QVBoxLayout()
        self.label = QLabel(f"Time Remaining: {self.remaining_time} seconds")
        layout.addWidget(self.label)
        layout.addWidget(pause_button)
        layout.addWidget(resume_button)
        layout.addWidget(stop_button)
        layout.addWidget(new_timer)

        # Layout for central widget
        central_widget.setLayout(layout)

        # Initialize QTimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1-second interval

    def update_time(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.label.setText("Time's up!")
            self.timer.stop()
        else:
            self.label.setText(f"Time Remaining: {self.remaining_time} seconds")
    
    def pause_time(self):
        if self.timer_running:
            self.timer.stop()
            self.timer_running = False

    def stop_time(self):
        self.timer.stop()
        self.label.setText("00:00:00")
        self.remaining_time = 0

    def resume_time(self):
        if not self.timer_running and self.remaining_time > 0:
            self.timer.start(1000)
            self.timer_running = True

    def new_timer(self):
        seconds, ok = QInputDialog.getInt(self, "Set Timer", "Enter countdown time in seconds:")
        if ok and seconds > 0:
            self.timer.stop()
            self.remaining_time = seconds
            self.label.setText(f"Time Remaining: {self.remaining_time} seconds")
            self.timer_running = True
            self.timer.start(1000)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

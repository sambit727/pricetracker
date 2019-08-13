import sys
import os

from PyQt5.QtWidgets import QApplication

from src.setup_mainwindow import MainWindow

dirpath = os.path.dirname(__file__)
db_path = os.path.join(dirpath, "data", "saveddata.db")

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    w = MainWindow(db_path=db_path)
    w.show()
    sys.exit(app.exec_())
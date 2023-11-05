from src.Controller import controller
from PyQt5 import QtWidgets
import sys

#No changes to be made to this file
def main():
	try:
		app=QtWidgets.QApplication(sys.argv)
		main_window=controller()
		main_window.window.show()
		sys.exit(app.exec_())
  
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == '__main__':
	main()
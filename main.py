from src.Controller import controller
from PyQt5 import QtWidgets
import sys
from src.styles.custom_palettes import darkPalette
from src.WPmainWindow import MainClass
import os

stylesheet = os.path.join(os.path.dirname(__file__),'src','styles','css','style.css')
#No changes to be made to this file
def main():
	try:
		darkpalette = darkPalette()
		app=QtWidgets.QApplication(sys.argv)
		app.setPalette(darkpalette)
		with open(stylesheet,'r') as file:
			app.setStyleSheet(file.read())
		main_window=controller()
		main_window.showMaximized()
		sys.exit(app.exec_())
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == '__main__':
	main()

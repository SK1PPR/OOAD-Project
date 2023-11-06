from src.Controller import controller
from PyQt5 import QtWidgets
import sys
from src.styles.custom_palettes import darkPalette
from src.WPmainWindow import MainClass

#No changes to be made to this file
def main():
	try:
		darkpalette = darkPalette()
		app=QtWidgets.QApplication(sys.argv)
		app.setPalette(darkpalette)
		# app.setStyle('Fusion')
		main_window=controller()
		main_window.show()
		sys.exit(app.exec_())
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == '__main__':
	main()

from gui import AppGUI
from functions import *

def main():
    # create the GUI object and connect it to the functions module
    app = AppGUI()
    app.set_functions(add_sandwich, add_drink, add_meal, clear_cart, get_invoice)
    app.run()

if __name__ == '__main__':
    main()
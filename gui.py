import tkinter as tk

class AppGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('McDonald\'s Order App')
        self.window.geometry('600x400')

        # create the sandwich options
        tk.Label(self.window, text='Select sandwich:').grid(row=0, column=0)
        self.sandwich_var = tk.StringVar()
        self.sandwich_var.set('Big Mac')
        sandwiches = ['Big Mac', 'Quarter Pounder', 'McChicken', 'Filet-O-Fish']
        for i, sandwich in enumerate(sandwiches):
            tk.Radiobutton(self.window, text=sandwich, variable=self.sandwich_var, value=sandwich).grid(row=1, column=i)

        # create the meal options
        tk.Label(self.window, text='Select meal size:').grid(row=2, column=0)
        self.meal_var = tk.StringVar()
        self.meal_var.set('Medium')
        meals = ['Small', 'Medium', 'Large']
        for i, meal in enumerate(meals):
            tk.Radiobutton(self.window, text=meal, variable=self.meal_var, value=meal).grid(row=3, column=i)

        # create the drink options
        tk.Label(self.window, text='Select drink:').grid(row=4, column=0)
        self.drink_var = tk.StringVar()
        self.drink_var.set('Coca-Cola')
        drinks = ['Coca-Cola', 'Sprite', 'Fanta', 'Water']
        for i, drink in enumerate(drinks):
            tk.Radiobutton(self.window, text=drink, variable=self.drink_var, value=drink).grid(row=5, column=i)

        # create the buttons
        tk.Button(self.window, text='Add to cart', command=self.add_to_cart).grid(row=6, column=0)
        tk.Button(self.window, text='Clear cart', command=self.clear_cart).grid(row=6, column=1)
        tk.Button(self.window, text='Get invoice', command=self.get_invoice).grid(row=6, column=2)

        # create the cart items listbox
        tk.Label(self.window, text='Cart items:').grid(row=7, column=0, sticky='w')
        self.cart_listbox = tk.Listbox(self.window, width=50)
        self.cart_listbox.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

    def set_functions(self, add_sandwich_func, add_drink_func, add_meal_func, clear_cart_func, get_invoice_func):
        self.add_sandwich = add_sandwich_func
        self.add_drink = add_drink_func
        self.add_meal = add_meal_func
        self.clear_cart = clear_cart_func
        self.get_invoice = get_invoice_func

    def add_to_cart(self):
        sandwich = self.sandwich_var.get()
        meal_size = self.meal_var.get()
        drink = self.drink_var.get()
        item = f'{sandwich} {meal_size} meal with {drink}'
        self.add_meal(sandwich, meal_size, drink)
        self.cart_listbox.insert(tk.END, item)

    def clear_cart(self):
        self.cart_listbox.delete(0, tk.END)
        self.clear_cart()

    def get_invoice(self):
        invoice = self.get_invoice()
        with open('invoice.csv', 'w') as file:
            file.write(invoice)
        self.cart_listbox.delete(0, tk.END)
        self.clear_cart()

    def run(self):
        self.window.mainloop()
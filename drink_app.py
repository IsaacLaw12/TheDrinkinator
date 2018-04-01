from tkinter import ttk
from tkinter import *
import tkinter as tk

class recipe:
    def __init__(self, recipe_name, option_one, option_two, option_three=None, option_four=None):
        options = [option_one, option_two, option_three, option_four]
        self.recipe_name = recipe_name
        self.ingredients = {}
        for opt in options:
            if opt:
                # Set the ingredient name in the dictionary and assign it the percentage
                self.ingredients[opt[0]] = opt[1]
        

class State:
    inventory = {
        "slot_one": "Vodka",
        "slot_two": "Cherry Flavor",
        "slot_three": "Sprite",
        "slot_four": None,
        }
    recipes = {
        "Oooorange Boogie": recipe("Oooorange Boogie",("Cherry Flavor",1),("Sprite",1)),
        "Russain Mechanic": recipe("Russain Mechanic",("Vodka",1),("Elbow Grease",1)),
        "White death": recipe("White death",("Vodka",1),("Bleach",1))
        }
    possible_drinks = ["Orange Juice", "Vodka"]
    def set_inventory(slot_name, new_value):
        if slot_name in inventory:
            inventory[slot_name] = new_value
    def load_inventory():
        # TODO load the list of drinks from a stored file or...
        # possible_drinks = saved_drinks
        pass
    def load_recipes():
        # TODO load the list of recipes from a stored file or...
        # recipes = saved_recipes
        pass
    def new_recipe(recipe_name, new_recipe):
        if recipe_name in recipes:
            print("Recipe " + recipe_name+ "already exists")
            return
        recipes[recipe_name] = new_recipe
        # TODO SAVE THIS STATE TO THE FILE?
        
    def set_recipe(recipe_name, new_recipe):
        if recipe_name in recipes:
            recipes[recipe_name] = new_recipe
        else:
            print("No recipe found with name: " + recipe_name)

    def delete_recipe(recipe_name):
        if recipe_name in recipes:
            recipes.pop(recipe_name)
        # TODO SAVE THIS NEW STATE TO FILE?

class DrinkApp():
    def __init__(self):
        # Setup main window
        self.root = tk.Tk()
        self.root.title("The Drinkinator")
        self.root.geometry('{}x{}'.format(500, 500))
        self.notebook = ttk.Notebook(self.root)
        
        # Setup main pages
        self.home = ttk.Frame(self.notebook)
        self.settings = ttk.Frame(self.notebook)
        
        self.home.grid_rowconfigure(1, weight=1)
        self.home.grid_columnconfigure(0, weight=1)
        
        # Setup home page
        
        # Setup drink name frame
        self.home_drink_name_frame = tk.Frame(self.home, bg="cyan", padx=5, pady=5)
        self.home_drink_name_frame.grid(row=0, pady = 10, padx = 20)
        
        # Setup drink labels
        self.home_drink_one = tk.Label(self.home_drink_name_frame, text="Slot #1: Drink one")
        self.home_drink_one.pack()
        self.home_drink_two = tk.Label(self.home_drink_name_frame, text="Slot #2: Drink two")
        self.home_drink_two.pack()
        self.home_drink_three = tk.Label(self.home_drink_name_frame, text="Slot #3: Drink three")
        self.home_drink_three.pack()
        self.home_drink_four = tk.Label(self.home_drink_name_frame, text="Slot #4: Drink four")
        self.home_drink_four.pack()
        
        # Setup drink select frame
        self.home_drink_select_frame = tk.Frame(self.home, bg="lavender", padx=5, pady=5)
        self.home_drink_select_frame.grid(row=1)
        
        # Setup drink select
        self.home_drink_options = ["Wow", "some good drinks here", "this one looks pretty good huh?", "nice"]
        self.home_drink_selected = tk.StringVar(self.home_drink_select_frame)
        self.home_drink_selected.set(self.home_drink_options[0])
        
        self.home_drink_select = tk.OptionMenu(self.home_drink_select_frame, self.home_drink_selected, *self.home_drink_options)
        self.home_drink_select.pack()
        
        # Setup drink slider frame
        self.home_drink_slider_frame = tk.Frame(self.home, bg="white", padx=5, pady=5)
        self.home_drink_slider_frame.grid(row=2)
        
        # Setup drink sliders
        self.home_slider_one = Scale(self.home_drink_slider_frame, from_=0, to=100, orient=HORIZONTAL)
        self.home_slider_one.pack()
        self.home_slider_two = Scale(self.home_drink_slider_frame, from_=0, to=100, orient=HORIZONTAL)
        self.home_slider_two.pack()
        self.home_slider_three = Scale(self.home_drink_slider_frame, from_=0, to=100, orient=HORIZONTAL)
        self.home_slider_three.pack()
        self.home_slider_four = Scale(self.home_drink_slider_frame, from_=0, to=100, orient=HORIZONTAL)
        self.home_slider_four.pack()
        
        # Setup start frame
        self.home_start_frame = tk.Frame(self.home, bg="white", padx=5, pady=5)
        self.home_start_frame.grid(row=3)
        
        # Setup start button
        self.home_start_button = tk.Button(self.home_start_frame, text = "!START!", command = self.start_activated)
        self.home_start_button.pack()
        
        # Add tabs to notebook
        self.notebook.add(self.home, text="Home")
        self.notebook.add(self.settings, text="Settings")
        self.notebook.pack(expand=1, fill="both")
        
        # Start main loop
        self.full_update()
        self.root.mainloop()
    def full_update(self):
        avalible_ingrediants = []
        self.home_drink_one.pack_forget()
        self.home_drink_two.pack_forget()
        self.home_drink_three.pack_forget()
        self.home_drink_four.pack_forget()
        self.home_slider_one.pack_forget()
        self.home_slider_two.pack_forget()
        self.home_slider_three.pack_forget()
        self.home_slider_four.pack_forget()
        if (State.inventory["slot_one"] != None):
            self.home_drink_one.config(text=("Slot #1: "+State.inventory["slot_one"]))
            self.home_drink_one.pack()
            self.home_slider_one.pack()
            avalible_ingrediants.append(State.inventory["slot_one"])
        if (State.inventory["slot_two"] != None):
            self.home_drink_two.config(text=("Slot #2: "+State.inventory["slot_two"]))
            self.home_drink_two.pack()
            self.home_slider_two.pack()
            avalible_ingrediants.append(State.inventory["slot_two"])
        if (State.inventory["slot_three"] != None):
            self.home_drink_three.config(text=("Slot #3: "+State.inventory["slot_three"]))
            self.home_drink_three.pack()
            self.home_slider_three.pack()
            avalible_ingrediants.append(State.inventory["slot_three"])
        if (State.inventory["slot_four"] != None):
            self.home_drink_four.config(text=("Slot #4: "+State.inventory["slot_four"]))
            self.home_drink_four.pack()
            self.home_slider_four.pack()
            avalible_ingrediants.append(State.inventory["slot_four"])
        self.home_drink_options = []
        for recipe in State.recipes:
            avalible = True
            for value in State.recipes[recipe].ingredients:
                if (value != None):
                    if not (value in avalible_ingrediants):
                        avalible = False
            if (avalible == True):
                self.home_drink_options.append(State.recipes[recipe].recipe_name);
        #self.home_drink_selected.set(self.home_drink_options[0])
        print(self.home_drink_options);
    def start_activated(self):
        print("DRINK UP BABY")


if __name__== "__main__":
    app = DrinkApp()

'''
This file starts a desktop GUI to interact with the Drinkinator 9000
running on a raspberry pi.  The commands are sent through PubNub.
Authors:
    Alex Undy
    Isaac Law
    Sabrina White
'''
from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class recipe:
    def __init__(self, recipe_name, option_one, option_two, option_three=None, option_four=None):
        '''
        Initialize the recipe. A recipe only requires two drinks, the other two are optional
        Options are tuples and have the format (drink_name, percentage). Percentage is an integer
        from 0-100
        '''
        options = [option_one, option_two, option_three, option_four]
        self.recipe_name = recipe_name
        self.ingredients = {}
        for opt in options:
            if opt:
                # Set the ingredient name in the dictionary and assign it the percentage
                ingredients[opt[0]] = opt[1]
        

class state:
    '''
    A class to hold the current state of the program.  This class is static
    and not intended to be instantiated.  Reference attributes and methods
    using state.foo or state.bar()
    '''
    inventory = {
        "slot_one": None,
        "slot_two": None,
        "slot_three": None,
        "slot_four": None,
        }
    @staticmethod
    def set_inventory(slot_name, new_value):
        if slot_name in inventory:
            inventory[slot_name] = new_value

    # A list of the potential drinks that could be in the machine/ recipes
    possible_drinks = ["Orange Juice", "Vodka"]
    @staticmethod
    def load_inventory():
        # TODO load the list of drinks from a stored file or...
        # possible_drinks = saved_drinks
        pass

    recipes = {
        "recipe name": "actual recipe object",
        }
    @staticmethod
    def load_recipes():
        # TODO load the list of recipes from a stored file or...
        # recipes = saved_recipes
        pass

    @staticmethod
    def new_recipe(recipe_name, new_recipe):
        if recipe_name in recipes:
            print("Recipe " + recipe_name+ "already exists")
            return
        recipes[recipe_name] = new_recipe
        # TODO SAVE THIS STATE TO THE FILE?
        
    @staticmethod
    def set_recipe(recipe_name, new_recipe):
        if recipe_name in recipes:
            recipes[recipe_name] = new_recipe
        else:
            print("No recipe found with name: " + recipe_name)

    @staticmethod
    def delete_recipe(recipe_name):
        if recipe_name in recipes:
            recipes.pop(recipe_name)
        # TODO SAVE THIS NEW STATE TO FILE?
    
class drink_sliders(Frame):
    '''
    A frame that provides sliders to adjust the varying amounts of each drink
    Check settings to see which ingredients are currently available
    and display only the relevant sliders.
    '''
    pass
    # IDK it seems like it would be nice to have a frame that has the sliders in it?
    # It will be used in two different places
    

def run_interface():
    # Root is the parent element of the whole interface
    root = tk.Tk()
    root.title("The Drinkinator")

    nb = ttk.Notebook(root)
    # Make two frames that will eventually be the two different tabs, their parent element is nb
    home = ttk.Frame(nb)
    settings = ttk.Frame(nb)



    
    # ALL OF THESE ELEMENTS ARE CURRENTLY PLACEHOLDERS, THEY SHOULD BE REPLACED
    # Fill in the home tab with its elements
    
    lb = tk.Label(home, text="Hello Tkinter!")
    lb.pack()
    w = Scale(home, from_=0, to=100, orient=HORIZONTAL)
    w.pack()
    # Fill in the settings tab with its elements
    text = ScrolledText(settings)
    text.pack(expand=1, fill="both")




    # This is where the frames are added into the Notebook tab manager 
    nb.add(home, text="Home")
    nb.add(settings, text="Settings")

    nb.pack(expand=1, fill="both")

    root.mainloop()


if __name__ == "__main__":
    run_interface()


'''
This file starts a desktop GUI to interact with the Drinkinator 9000
running on a raspberry pi.  The commands are sent through PubNub.
Authors:
    Alex Undy
    Isaac Law
    Sabrina White
'''
import pickle

class Recipe:
    def __init__(self, recipe_name, option_one, option_two, option_three=None, option_four=None):
        '''
        Initialize the recipe. A recipe only requires two drinks, the other two are optional
        Options are tuples and have the format (drink_name, amount). Amount is an integer
        value. 1 amount = 10 seconds of pumping or about 15 mL of fluid.
        '''
        
        # A temporaray list of drink options to loop over
        options = [option_one, option_two, option_three, option_four]
        
        self.recipe_name = recipe_name
        self.ingredients = {}
        for opt in options:
            if opt:
                # Set the ingredient name in the dictionary and assign it the amount
                self.ingredients[opt[0]] = opt[1]
    
    def __repr__(self):
        print_string = "\n" + self.recipe_name + ": \n"
        for ingr in self.ingredients:
            print_string += "    " + ingr + " - " + str(self.ingredients[ingr]) + "\n"
        return print_string
        
        

class State:
    '''
    A class to hold the current state of the program.  This class is static
    and not intended to be instantiated.  Reference attributes and methods
    using state.foo or state.bar()
    '''
    saved_state_fn = "state.pkl"
    
    # The only values should be strings that are also found in ingredients
    inventory = {
        "slot_one": None,
        "slot_two": None,
        "slot_three": None,
        "slot_four": None,
        }
    
    # Format: "ingredient name" just a string
    ingredients = []
    # Format "recipe_name":  actual recipe object
    recipes = {}
    
    @staticmethod
    def load_state():
        with open(State.saved_state_fn, "rb") as input:
            State.inventory = pickle.load(input)
            State.ingredients = pickle.load(input)
            State.recipes = pickle.load(input)

    @staticmethod
    def save_state():
        with open(State.saved_state_fn, "wb") as output:
            pickle.dump(State.inventory, output)
            pickle.dump(State.ingredients, output)
            pickle.dump(State.recipes, output)

    @staticmethod
    def set_inventory(slot_name, new_value):
        # Specify which ingredient is in slot_name
        if slot_name in State.inventory:
            State.inventory[slot_name] = new_value
        else:
            print("Error incorrect slot name")
        State.save_state()

    @staticmethod
    def add_recipe(new_recipe):
        recipe_name = new_recipe.recipe_name
        # Add a recipe, if it already exists then update it
        if recipe_name in State.recipes:
            State.recipes[recipe_name] = new_recipe
        else:
            State.recipes[recipe_name] = new_recipe
        State.save_state()

    @staticmethod
    def delete_recipe(recipe_name):
        # Remove the recipe and save changes
        if recipe_name in State.recipes:
            State.recipes.pop(recipe_name)
        State.save_state()

    @staticmethod
    def add_ingredient(ingredient_name):
        # Add an ingredient, should just be a string aka "Orange juice"
        State.ingredients.append(ingredient_name)
        State.save_state()

    @staticmethod
    def delete_ingredient(ingredient_name):
        State.ingredients.remove(ingredient_name)
        State.save_state()


